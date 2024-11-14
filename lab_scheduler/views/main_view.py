from lab_scheduler.views.templates.main_template import MainTemplate

class MainView(MainTemplate):
    """Main application view."""

    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)

    def create_widgets(self):
        main_section = self.add_section(self, "Menu Rápido")
        self.add_button(main_section, "Cadastrar Usuário", self.controller.register_user, row=1, sticky="w")
        self.add_button(main_section, "Reservar Laboratório", self.controller.reserve_lab, row=2, sticky="w")

        # Reports Section
        reports_section = self.add_section(self, "Relatórios")
        self.add_button(reports_section, "Gerar Cronograma semanal", self.controller.generate_schedule, row=3, sticky="w")

        # Management Section
        management_section = self.add_section(self, "Gerenciamento")
        self.add_button(management_section, "Gerenciar usuários", self.controller.manage_users, row=4, sticky="w")
        self.add_button(management_section, "Gerenciar reservas", self.controller.manage_reservations,row=5, sticky="w")
        self.add_button(management_section, "Gerenciar laboratórios", self.controller.manage_labs,row=6, sticky="w")
        self.add_button(management_section, "Gerenciar horários", self.controller.manage_time_slots,row=7, sticky="w")
