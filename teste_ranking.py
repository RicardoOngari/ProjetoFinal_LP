import sqlite3

conexao = sqlite3.connect("quiz.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM ranking")

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

conexao.close()