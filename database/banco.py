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

    # Chama a função que conecta ao banco
    conexao = conectar_banco()

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Executa o comando SQL para buscar todas as perguntas
    cursor.execute("SELECT * FROM perguntas")

    # Armazena todos os registros encontrados em uma lista
    registros = cursor.fetchall()

    # Fecha a conexão com o banco
    conexao.close()

    # Lista que armazenará as perguntas formatadas
    perguntas = []

    # Percorre cada registro retornado pelo banco.
    # Em cada repetição, "registro" representa uma linha da tabela.
    # O loop pega um registro por vez, monta um dicionário com os dados
    # desse registro e adiciona esse dicionário à lista "perguntas".
    for registro in registros:

        # Cria um dicionário no mesmo formato utilizado pelo quiz
        pergunta = {

            # registro[1] corresponde ao enunciado da pergunta
            "pergunta": registro[1],

            # Lista contendo as alternativas da pergunta
            "opcoes": [
                f"A) {registro[2]}",  # alternativa_a
                f"B) {registro[3]}",  # alternativa_b
                f"C) {registro[4]}",  # alternativa_c
                f"D) {registro[5]}"   # alternativa_d
            ],

            # registro[6] corresponde à resposta correta
            "resposta": registro[6]
        }

        # Adiciona o dicionário criado na lista de perguntas.
        # O append não substitui os anteriores, apenas adiciona um novo item.
        perguntas.append(pergunta)

    # Retorna a lista completa de perguntas
    return perguntas


# Função para salvar o resultado do jogador no ranking
def salvar_resultado(nome, pontos):

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Insere o nome e a pontuação na tabela ranking
    cursor.execute("""
        INSERT INTO ranking (nome, pontos)
        VALUES (?, ?)
    """, (nome, pontos))

    # Salva as alterações
    conexao.commit()

    # Fecha a conexão
    conexao.close()



# Função para buscar o ranking dos jogadores
def buscar_ranking():

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Busca os jogadores ordenados pela maior pontuação
    cursor.execute("""
        SELECT nome, pontos, data_jogo
        FROM ranking
        ORDER BY pontos DESC
    """)

    ranking = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Retorna os resultados encontrados
    return ranking

