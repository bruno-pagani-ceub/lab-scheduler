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
- Não exceder o limite máximo de 30 caracteres para os nomes das tabelas ou colunas

---

### 3.2. Nomenclatura de atributos
Para garantir consistência e facilitar a identificação do tipo de dado, as colunas devem incluir os seguintes prefixos:

| Tipo de Dado          | Prefixo      | Exemplo               |
|-----------------------|--------------|-----------------------|
| Data                  | `dt_`        | `dt_reserva`          |
| Hora                  | `hr_`        | `hr_reserva`          |
| Minuto                | `min_`       | `min_reserva`         |
| Segundos              | `seg_`       | `seg_reserva`         |
| Número                | `nr_`        | `nr_quantidade`       |
| Nome                  | `nm_`        | `nm_usuario`          |
| Indicador (Booleano)  | `is_`        | `is_reservado`        |
| Descrição/Texto       | `ds_`        | `ds_laboratorio`      |
| Telefone              | `tel_`       | `tel_contato`         |
| Valor Monetário       | `vl_`        | `vl_reserva`          |
| Chave estrangeira (FK)| `id_`        | `id_reserva`          |
| Senha                 | `pwd_`       | `pwd_usuario`         |
| Tipo                  | `tp_`        | `tp_usuario`          |
| Quantidade            | `qtd_`       | `qtd_computadores`    |
| Data e Hora           | `dti_`       | `dti_reserva`         |
| Endereço              | `end_`       | `end_usuario`         |
| Imagem                | `img_`       | `img_perfil`          |
| Observação            | `obs_`       | `obs_reserva`         |
| Percentual            | `pct_`       | `pct_reservas`        |
| Status                | `sts_`       | `sts_reserva`         |
| Tipo                  | `tp_`        | `tp_usuario`          |
| Total                 | `tot_`       | `tot_reservas`        |
| Usuário               | `usr_`       | `usr_reserva`         |

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
