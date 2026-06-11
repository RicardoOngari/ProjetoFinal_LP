# Importa a biblioteca sqlite3, utilizada para criar e manipular bancos de dados SQLite
import sqlite3

# Cria um novo banco de dados chamado "quiz.db" caso ele não exista.
# Se já existir, apenas abre a conexão com ele.
conexao = sqlite3.connect("quiz.db")

# Cria um cursor, responsável por executar comandos SQL no banco de dados.
cursor = conexao.cursor()

# Cria a tabela "perguntas" caso ela ainda não exista.
# Essa tabela armazenará todas as perguntas do quiz e suas alternativas.
cursor.execute("""
CREATE TABLE IF NOT EXISTS perguntas (
    # Identificador único da pergunta (incrementado automaticamente)
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    # Texto da pergunta
    pergunta TEXT NOT NULL,

    # Alternativas de resposta
    alternativa_a TEXT NOT NULL,
    alternativa_b TEXT NOT NULL,
    alternativa_c TEXT NOT NULL,
    alternativa_d TEXT NOT NULL,

    # Alternativa correta (ex.: "A", "B", "C" ou "D")
    correta TEXT NOT NULL
)
""")

# Cria a tabela "ranking" caso ela ainda não exista.
# Essa tabela armazenará a pontuação dos jogadores.
cursor.execute("""
CREATE TABLE IF NOT EXISTS ranking (
    # Identificador único do registro
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    # Nome do jogador
    nome TEXT NOT NULL,

    # Quantidade de pontos obtidos
    pontos INTEGER NOT NULL,

    # Data e horário em que o jogo foi realizado.
    # CURRENT_TIMESTAMP insere automaticamente o momento da gravação.
    data_jogo DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Salva definitivamente todas as alterações feitas no banco de dados.
conexao.commit()

# Fecha a conexão com o banco para liberar recursos.
conexao.close()

# Exibe uma mensagem informando que o banco foi criado (ou aberto) com sucesso.
print("Banco criado com sucesso!")