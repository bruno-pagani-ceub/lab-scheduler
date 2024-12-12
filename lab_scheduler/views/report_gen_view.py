import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ScheduleGenerationView:
    def __init__(self, parent, schedule_data):
        self.parent = parent
        self.schedule_data = schedule_data
        self.filtered_data = schedule_data
        self.setup_view()

    def setup_view(self):
        window = tk.Toplevel(self.parent)
        window.title("Cronograma Semestral")
        window.geometry("1000x600")

        search_frame = tk.Frame(window)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Pesquisar por data:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", padx=5)

        tk.Label(search_frame, text="Horário (Início):").pack(side="left", padx=5)
        self.search_time_var = tk.StringVar()
        time_entry = ttk.Entry(search_frame, textvariable=self.search_time_var)
        time_entry.pack(side="left", padx=5)

        tk.Label(search_frame, text="Laboratório:").pack(side="left", padx=5)
        self.search_lab_var = tk.StringVar()
        lab_entry = ttk.Entry(search_frame, textvariable=self.search_lab_var)
        lab_entry.pack(side="left", padx=5)

        search_button = ttk.Button(search_frame, text="Pesquisar", command=self.search_by_criteria)
        search_button.pack(side="left", padx=5)

        reset_button = ttk.Button(search_frame, text="Resetar", command=self.reset_table)
        reset_button.pack(side="left", padx=5)

        table_frame = tk.Frame(window)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.table = ttk.Treeview(
            table_frame,
            columns=("Data", "Início", "Fim", "Atividade", "Laboratório"),
            show='headings'
        )
        self.table.heading("#1", text="Data")
        self.table.heading("#2", text="Início")
        self.table.heading("#3", text="Fim")
        self.table.heading("#4", text="Atividade")
        self.table.heading("#5", text="Laboratório")
        self.table.column("#1", anchor="center", width=150)
        self.table.column("#2", anchor="center", width=100)
        self.table.column("#3", anchor="center", width=100)
        self.table.column("#4", anchor="center", width=200)
        self.table.column("#5", anchor="center", width=150)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.populate_table(self.schedule_data)

        close_button = ttk.Button(window, text="Fechar", command=window.destroy)
        close_button.pack(pady=10)

    def populate_table(self, data):
        self.table.delete(*self.table.get_children())
        for item in data:
            try:
                if isinstance(item['data'], str):
                    formatted_date = item['data']
                else:
                    formatted_date = datetime.strptime(str(item['data']), "%Y-%m-%d").strftime("%d-%m-%Y")
            except (ValueError, TypeError):
                formatted_date = "Data Inválida"

            laboratorio = item.get('laboratorio', 'Desconhecido')

            self.table.insert("", "end", values=(
                formatted_date, item['inicio'], item['fim'], item['atividade'], laboratorio
            ))

    def search_by_criteria(self):
        query_date = self.search_var.get().strip()
        query_time = self.search_time_var.get().strip()
        query_lab = self.search_lab_var.get().strip()

        self.filtered_data = self.schedule_data

        if query_date:
            try:
                formatted_date = datetime.strptime(query_date, "%d-%m-%Y").strftime("%d-%m-%Y")
                self.filtered_data = [item for item in self.filtered_data if item['data'] == formatted_date]
            except ValueError:
                messagebox.showerror("Erro", "Formato de data inválido. Use dd-mm-yyyy.")
                return

        if query_time:
            self.filtered_data = [item for item in self.filtered_data if item['inicio'] <= query_time <= item['fim']]

        if query_lab:
            self.filtered_data = [item for item in self.filtered_data if str(item['laboratorio']) == query_lab]

        if not self.filtered_data:
            messagebox.showinfo("Nenhum resultado", "Nenhum horário encontrado.")
        self.populate_table(self.filtered_data)

    def reset_table(self):

        self.search_var.set("")
        self.search_time_var.set("")
        self.search_lab_var.set("")
        self.filtered_data = self.schedule_data
        self.populate_table(self.schedule_data)
