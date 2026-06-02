# biblioteca para limpar o terminal
import os 

# biblioteca para pausar o programa por um tempo
import time




# Lista Perguntas contendo dicionários com as perguntas, opções e respostas corretas
perguntas = [
    # dicionarios
    {
        # chaves e valores
        "pergunta": "Qual palavra-chave é usada para criar uma função em Python?",
        "opcoes": ["A) function", "B) create", "C) def", "D) func"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual estrutura de dados utiliza chaves e valores?",
        "opcoes": ["A) Lista", "B) Tupla", "C) String", "D) Dicionário"],
        "resposta": "D"
    },
    {
        "pergunta": "Qual operador é usado para comparar igualdade em Python?",
        "opcoes": ["A) =", "B) ==", "C) !=", "D) ==="],
        "resposta": "B"
    },
    {
        "pergunta": "Qual destes tipos de dados é imutável?",
        "opcoes": ["A) Lista", "B) Dicionário", "C) Tupla", "D) Conjunto"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual comando exibe algo na tela em Python?",
        "opcoes": ["A) show()", "B) display()", "C) print()", "D) output()"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual laço é usado para percorrer uma lista?",
        "opcoes": ["A) while", "B) if", "C) for", "D) switch"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual método adiciona um elemento ao final de uma lista?",
        "opcoes": ["A) add()", "B) append()", "C) insert()", "D) push()"],
        "resposta": "B"
    },
    {
        "pergunta": "O que significa HTML?",
        "opcoes": [
            "A) Hyper Text Markup Language",
            "B) High Transfer Machine Language",
            "C) Hyper Tool Machine Language",
            "D) Home Text Markup Language"
        ],
        "resposta": "A"
    },
    {
        "pergunta": "Qual linguagem é utilizada para estilizar páginas web?",
        "opcoes": ["A) HTML", "B) Python", "C) CSS", "D) SQL"],
        "resposta": "C"
    },
    {
    "pergunta": "Qual estrutura de repetição executa enquanto uma condição for verdadeira?",
    "opcoes": ["A) if", "B) for", "C) while", "D) def"],
    "resposta": "C"
    }
]


pontuacao = 0  # Variável para armazenar a pontuação do usuário



# for para percorrer nossa lista perguntas
# enumerate é uma função em python que retorna o índice "0, 1, 2..." e o valor
# for cria duas variaveis, index para guardar o índice do enumerate e questao para guardar o valor do dicionário
for index, questao in enumerate(perguntas):
    os.system("cls" if os.name == "nt" else "clear")  #limpar terminal em todos sistemas operacionais


    print(f"--- Pergunta {index + 1} de {len(perguntas)} ---")
    print(f"\n{questao['pergunta']}\n")  # Imprime a pergunta
    
    for opcao in questao["opcoes"]:
        print(opcao)  # Imprime as opções de resposta

    resposta = input("\nDigite a sua resposta: ").strip().upper()  # Lê a resposta do usuário, remove espaços e converte para maiúscula

    if resposta == questao["resposta"]:
        print("✅ PARABENS, VOCÊ ACERTOU!\n")
        pontuacao += 1  # Incrementa a pontuação em 1
    else:
        print(f"❌ RESPOSTA ERRADA!, A RESPOSTA CORRETA É: {questao['resposta']}")

    time.sleep(2)  # Pausa por 2 segundos antes de mostrar a próxima pergunta

    

os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal novamente
print("=" * 30)
print("--- FIM DE JOGO ---")
print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas")
print("=" * 30)
   