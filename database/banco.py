# Biblioteca para trabalhar com banco de dados SQLite
import sqlite3


# Função para conectar ao banco de dados
def conectar_banco():

    # Cria uma conexão com o arquivo quiz.db
    conexao = sqlite3.connect("database/quiz.db")

    # Retorna a conexão para ser usada em outras funções
    return conexao


# Função para buscar todas as perguntas cadastradas no banco
def buscar_perguntas():

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Busca todas as perguntas
    cursor.execute("SELECT * FROM perguntas")

    # Guarda todos os registros encontrados
    registros = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Lista que armazenará as perguntas formatadas
    perguntas = []

    # Percorre todos os registros encontrados
    for registro in registros:

        # Cria um dicionário no formato esperado pelo quiz
        pergunta = {

            # Enunciado da pergunta
            "pergunta": registro[1],

            # Lista de alternativas
            "opcoes": [
                f"A) {registro[2]}",
                f"B) {registro[3]}",
                f"C) {registro[4]}",
                f"D) {registro[5]}"
            ],

            # Resposta correta
            "resposta": registro[6]
        }

        # Adiciona a pergunta na lista
        perguntas.append(pergunta)

    # Retorna todas as perguntas
    return perguntas


# Função para salvar o resultado do jogador
def salvar_resultado(nome, pontos):

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor
    cursor = conexao.cursor()

    # Insere nome e pontuação
    cursor.execute("""
        INSERT INTO ranking (nome, pontos)
        VALUES (?, ?)
    """, (nome, pontos))

    # Salva alterações
    conexao.commit()

    # Fecha conexão
    conexao.close()


# Função para buscar os 10 melhores jogadores
def buscar_ranking():

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor
    cursor = conexao.cursor()

    # Busca os jogadores ordenados pela maior pontuação
    cursor.execute("""
        SELECT nome, pontos
        FROM ranking
        ORDER BY pontos DESC
        LIMIT 10
    """)

    # Guarda os resultados encontrados
    ranking = cursor.fetchall()

    # Fecha conexão
    conexao.close()

    # Retorna o ranking
    return ranking