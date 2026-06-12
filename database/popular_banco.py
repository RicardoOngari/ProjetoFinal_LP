import sqlite3
from database.perguntas import perguntas

# Conecta ao banco
conexao = sqlite3.connect("database/quiz.db")
cursor = conexao.cursor()

# Percorre a lista de perguntas
for questao in perguntas:

    cursor.execute("""
        INSERT INTO perguntas (
            pergunta,
            alternativa_a,
            alternativa_b,
            alternativa_c,
            alternativa_d,
            correta
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        questao["pergunta"],

        # Remove "A) "
        questao["opcoes"][0][3:],

        # Remove "B) "
        questao["opcoes"][1][3:],

        # Remove "C) "
        questao["opcoes"][2][3:],

        # Remove "D) "
        questao["opcoes"][3][3:],

        questao["resposta"]
    ))

# Salva alterações
conexao.commit()

# Fecha conexão
conexao.close()

print("Perguntas inseridas com sucesso!")