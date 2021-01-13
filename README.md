# Whatsextract
Controle de entrada e saída de pessoas do grupo WhatsApp

# Grupos possuem:
    - Arquivo
    - Nome
    - Numero
    - Alunos

# Alunos Possuem:
    - Numero
    - Data de Entrada
    - Data de saída
    - Status => (Saiu/Continua)
    - Alterar o número

# Grupo Precisará :
    - Importar os Grupos
    - Exportar os contatos
    - Extrair o Nome e Número
    - Remover duplicados

# Aluno precisa:
    - Extrair alunos
    - Controlar data de entrada 
    - Controlar data de saída
    - Criar contato
    - Exportar contato
    - Remover duplicados

# Operações
    - Entrada do grupo
    - Saída do grupo
    - Mudança de número

# Regex Capturar Alunos com Data
[\d/ :]* - *(\+55 [\d\s-]*) (entrou|saiu)(\+55 [\d\s-]*$)?
# Regex Nome e Número do grupo
Conversa do WhatsApp com (\[(\d{1,})].*)
