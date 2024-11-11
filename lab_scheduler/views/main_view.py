# views/main_view.py
from .templates.main_template import BaseView

class MainView(BaseView):
    """Main application view."""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.create_main_page()

    def create_main_page(self):
        # Main Section (no title)
        self.create_button(self, "Cadastrar Usuário", self.controller.register_user)
        self.create_button(self, "Reservar Laboratório", self.controller.reserve_lab)

        # Reports Section
        reports_section = self.create_section("Relatórios")
        self.create_button(reports_section, "Gerar Cronograma semanal", self.controller.generate_schedule)

        # Management Section
        management_section = self.create_section("Gerenciamento")
        self.create_button(management_section, "Gerenciar usuários", self.controller.manage_users)
        self.create_button(management_section, "Gerenciar reservas", self.controller.manage_reservations)
        self.create_button(management_section, "Gerenciar laboratórios", self.controller.manage_labs)
        self.create_button(management_section, "Gerenciar horários", self.controller.manage_time_slots)
