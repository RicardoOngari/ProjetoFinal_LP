# ------------OPERAÇOES DO BANCO---------------


# =====================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# =====================================================

# Biblioteca utilizada para trabalhar com banco de dados SQLite
import sqlite3


# =====================================================
# CONEXÃO COM O BANCO DE DADOS
# =====================================================

def conectar_banco():
    """
    Cria e retorna uma conexão com o banco de dados.
    """

    # Conecta ao arquivo do banco de dados
    conexao = sqlite3.connect("database/quiz.db")

    return conexao


# =====================================================
# CONSULTA DE PERGUNTAS
# =====================================================

def buscar_perguntas():
    """
    Busca todas as perguntas cadastradas no banco
    e retorna uma lista formatada para o quiz.
    """

    # Conecta ao banco de dados
    conexao = conectar_banco()

    # Cria cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Busca todas as perguntas cadastradas
    cursor.execute("SELECT * FROM perguntas")

    # Obtém todos os registros encontrados
    registros = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Lista que armazenará as perguntas formatadas
    perguntas = []

    # Percorre todos os registros encontrados
    for registro in registros:

        # Monta o dicionário no formato esperado pelo quiz
        pergunta = {

            # Texto da pergunta
            "pergunta": registro[1],

            # Alternativas disponíveis
            "opcoes": [
                f"A) {registro[2]}",
                f"B) {registro[3]}",
                f"C) {registro[4]}",
                f"D) {registro[5]}"
            ],

            # Alternativa correta
            "resposta": registro[6]
        }

        # Adiciona a pergunta à lista
        perguntas.append(pergunta)

    # Retorna todas as perguntas formatadas
    return perguntas


# =====================================================
# SALVAR RESULTADO DO JOGADOR
# =====================================================

def salvar_resultado(nome, pontos):
    """
    Salva no banco de dados o nome do jogador
    e sua pontuação final.
    """

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor para execução SQL
    cursor = conexao.cursor()

    # Insere o resultado na tabela ranking
    cursor.execute("""
        INSERT INTO ranking (nome, pontos)
        VALUES (?, ?)
    """, (nome, pontos))

    # Salva as alterações realizadas
    conexao.commit()

    # Fecha a conexão
    conexao.close()


# =====================================================
# CONSULTA DO RANKING
# =====================================================

def buscar_ranking():
    """
    Retorna os 10 melhores jogadores
    ordenados pela maior pontuação.
    """

    # Conecta ao banco
    conexao = conectar_banco()

    # Cria cursor para execução SQL
    cursor = conexao.cursor()

    # Busca os 10 melhores jogadores
    cursor.execute("""
        SELECT nome, pontos
        FROM ranking
        ORDER BY pontos DESC
        LIMIT 10
    """)

    # Obtém os resultados encontrados
    ranking = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Retorna o ranking
    return ranking