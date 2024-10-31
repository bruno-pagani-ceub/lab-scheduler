# Lab Scheduler
O projeto consiste em um software de gerenciamento de reservas de laboratórios no CEUB utilizando Python para estruturar o front-end e lógica de inserção e conferência de dados, e MySQL para estruturar o banco de dados.

Proposta com base na seguinte **história de usuário**:
- Sou um funcionário administrativo do CEUB responsável pelas reservas de laboratórios de informática. Preciso de um software que me permita gerenciar as reservas de forma eficiente, em especial:
  - Visualizar rapidamente a disponibilidade de um laboratório em um determinado dia;
  - Filtrar laboratórios pelo número de computadores disponíveis;
  - Permitir que um professor realize uma reserva recorrente de laboratórios ao longo de um semestre;
  - Marcar laboratórios como indisponíveis em caso de manutenção ou algum evento especial;
  - Limitar o total de horas que um aluno pode reservar ao longo do semestre.

# Estrutura do BD
O software terá controle dos seguintes aspectos:
* **Laboratórios (tb-laboratorio)**
  - Proposta de colunas:
    - id INT AUTO_INCREMENT
    - bloco TINYINT
    - sala TINYINT
    - qtde_pcs TINYINT


* **Usuários (tb-usuario)**
  - Proposta de colunas:
    - id INT AUTO_INCREMENT
    - nome VARCHAR(50)
    - posicao ENUM('professor', 'aluno', 'funcionario', 'visitante')
    - registro VARCHAR(14)
  - O campo "posicao" determinaria se quem reservou é professor, aluno, visitante, e o "registro" seria o RA do aluno, matrícula do professor, ou CPF do visitante.
 
- **Reservas (ta-reservas)**
  - Proposta de colunas:
    - id INT AUTO_INCREMENT
    - id_usuario INT, FK ref tb-usuario
    - id_laboratorio INT, FK ref tb-laboratorio
    - horario_inicio DATETIME
    - horario_fim DATETIME
    - status ENUM('ativo','encerrado','cancelado')
      - "ativo" (de antes até o final do horário de reserva), "encerrado" (após fim da reserva), "cancelado" (antes da reserva)
      - usar um trigger para trocar de "ativo" para "encerrado" quando passar do horario_fim, e "cancelado" não muda - deixa registrado se a reserva foi realizada e cumprida, ou se foi cancelada antes da hora.
      - se for cancelada, o horário se torna disponível novamente.
    - manutencao (BOOL)
      - padrão 0, somente pode ser alterado em reserva por funcionário
      - 1 = manutenção, 0 = não

# Funcionamento básico da interface (CRUD)
- TODO