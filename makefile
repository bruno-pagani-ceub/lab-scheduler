VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
MYSQL_HOST := localhost
MYSQL_USER := root
MYSQL_PASSWORD := senha123
MYSQL_DATABASE := lab_scheduler
MYSQL_PORT_TEST := 3307


venv:
	@echo "Creating virtual environment and installing dependencies..."
	if [ ! -d $(VENV_DIR) ]; then \
		python3 -m venv $(VENV_DIR); \
	fi
	$(VENV_DIR)/bin/pip install -r requirements.txt

db:
	@echo "Starting MySQL database container for $(ENVIRONMENT) environment..."
	docker compose -f $(COMPOSE_FILE) up -d db
	@echo "Waiting for MySQL to be ready..."
	MAX_RETRIES=30; \
	RETRY_COUNT=0; \
	until docker exec $(DB_CONTAINER_NAME) mysqladmin ping -h "localhost" --silent; do \
		RETRY_COUNT=$$((RETRY_COUNT+1)); \
		if [ $$RETRY_COUNT -ge $$MAX_RETRIES ]; then \
			echo "MySQL did not become ready in time. Exiting."; \
			exit 1; \
		fi; \
		echo "Waiting for MySQL to be ready... (Attempt $$RETRY_COUNT)"; \
		sleep 2; \
	done
	@echo "MySQL is ready."

dev: venv
	@$(MAKE) db ENVIRONMENT=development COMPOSE_FILE=docker-compose.dev.yml DB_CONTAINER_NAME=lab_scheduler_db_dev
	@echo "Running the application locally..."
	export MYSQL_HOST=$(MYSQL_HOST) && \
	export MYSQL_USER=$(MYSQL_USER) && \
	export MYSQL_PASSWORD=$(MYSQL_PASSWORD) && \
	export MYSQL_DATABASE=$(MYSQL_DATABASE) && \
	$(PYTHON) lab_scheduler/main.py

test: venv
	@$(MAKE) db ENVIRONMENT=testing COMPOSE_FILE=docker-compose.test.yml DB_CONTAINER_NAME=lab_scheduler_db_test
	@echo "Running the application in test environment locally..."
	export MYSQL_HOST=$(MYSQL_HOST) && \
	export MYSQL_USER=$(MYSQL_USER) && \
	export MYSQL_PASSWORD=$(MYSQL_PASSWORD) && \
	export MYSQL_DATABASE=$(MYSQL_DATABASE) && \
	export MYSQL_PORT=$(MYSQL_PORT_TEST) && \
	$(PYTHON) lab_scheduler/main.py

clean:
	@echo "Cleaning up..."
	docker compose -f docker-compose.dev.yml down -v
	docker compose -f docker-compose.test.yml down -v
	rm -rf $(VENV_DIR)
