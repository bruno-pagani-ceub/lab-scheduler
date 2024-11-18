# Regras de Nomenclatura do Projeto - LabScheduler

## 1. Introdução
Este documento descreve as regras de nomenclatura adotadas no projeto para tabelas, colunas, chaves estrangeiras, variáveis e outros elementos, garantindo consistência e clareza em todas as camadas do sistema.

---

## 2. Diretrizes Gerais
- **Idioma**: Todos os nomes serão em português.
- **Estilo**:
  - Tabelas: `snake_case`, singular.
  - Colunas: `snake_case`.
  - Variáveis no código: `camelCase`.
- **Semântica**: Utilizar nomes claros e descritivos, evitando abreviações desnecessárias.
- **Acrônimos**: Devem estar em minúsculas (ex.: `id_laboratorio`, não `id_LABORATORIO`).

---

## 3. Banco de Dados

### 3.1. Regras Gerais
- As tabelas devem sempre estar no singular.
- Colunas que representam chaves primárias devem ser nomeadas como `id`.
- Colunas que representam chaves estrangeiras devem incluir o nome da tabela referenciada no singular com o prefixo `id_` (ex.: `id_usuario`).
- Colunas booleanas devem ter nomes iniciados por `is_` (ex.: `is_reservado`).
- Não exceder o limite máximo de 30 caracteres para os nomes das tabelas ou colunas

---

### 3.2. Regras por Entidade

#### Tabela: `laboratorio`
- **Descrição**: Contém informações sobre os laboratórios.
- **Colunas**:
  - `id` (PK): Identificador único do laboratório.
  - `bloco`: Bloco onde o laboratório está localizado.
  - `sala`: Número da sala.
  - `qtde_pcs`: Quantidade de computadores disponíveis.

#### Tabela: `horario`
- **Descrição**: Representa horários selecionados.
- **Colunas**:
  - `id` (PK): Identificador único do horário.
  - `dt_dia`: Data específica do horário.
  - `dia_semana`: Dia da semana.
  - `hr_inicio`: Hora de início.
  - `hr_fim`: Hora de término.
  - `semestre`: Semestre correspondente.
  - `ano`: Ano correspondente.

#### Tabela: `laboratorio_horario`
- **Descrição**: Tabela de associação entre laboratórios e horários.
- **Colunas**:
  - `id` (PK): Identificador único da associação.
  - `id_laboratorio` (FK): Referência ao laboratório.
  - `id_horario` (FK): Referência ao horário.
  - `is_reservado`: Indica se o horário está reservado.

#### Tabela: `reserva`
- **Descrição**: Contém informações sobre as reservas realizadas.
- **Colunas**:
  - `id` (PK): Identificador único da reserva.
  - `id_usuario` (FK): Referência ao usuário.
  - `id_laboratorio_horario` (FK): Referência ao laboratório-horário reservado.
  - `status`: Status da reserva (ex.: ativo, cancelado).
  - `tipo`: Tipo de reserva.

#### Tabela: `usuario`
- **Descrição**: Informações sobre os usuários do sistema.
- **Colunas**:
  - `id` (PK): Identificador único do usuário.
  - `nome`: Nome completo.
  - `posicao`: Posição ou cargo do usuário.
  - `identificacao`: Documento ou matrícula.

---

### 3.3. Regras para Índices e Constraints
- Índices: Nomear como `idx_<tabela>_<coluna>` (ex.: `idx_laboratorio_bloco`).
- Chaves estrangeiras: Nomear como `id_<tabela_referenciada>` (ex.: `id_usuario`).

---

## 4. Regras para Código

### 4.1. Variáveis
- Nomes de variáveis: `camelCase` (ex.: `qtdePcs`, `statusReserva`).
- Constantes: `UPPER_SNAKE_CASE` (ex.: `RESERVA_ATIVA`).

### 4.2. Funções
- **Padrão**: Nomear com verbos no infinitivo para indicar ação.
- Exemplos:
  - `criarReserva`
  - `atualizarLaboratorio`
  - `listarUsuarios`

### 4.3. Classes
- Nomes em `PascalCase`.
- Exemplo:
  - `LaboratorioService`
  - `ReservaController`

---
