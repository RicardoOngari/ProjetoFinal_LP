# biblioteca para limpar o terminal
import os 
# biblioteca para pausar o programa por um tempo
import time
# Biblioteca para podermos embaralhar as perguntas
import random
# Importa a função que lê as perguntas da tabela perguntas do banco
from banco import buscar_perguntas
# Busca as perguntas do banco de dados e armazena na variável perguntas
perguntas = buscar_perguntas()


# Função para para limpar o terminal em sistemas Windows e Unix/Linux
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")  



# Funcção para exibir cada pergunta e suas opções
def exibir_pergunta(questao, numero):
    #  "--- Pergunta 1 de 10 ---"
    print(f"--- Pergunta {numero} de {len(perguntas)} ---")
    # Imprime a pergunta
    print(f"\n{questao['pergunta']}\n")  
    # percorre a lista de opções da pergunta
    for opcao in questao["opcoes"]:
        print(opcao)  # Imprime as opções de resposta



def verificar_resposta(resposta_usuario, resposta_correta):
    # Retorna True se a resposta estiver correta, caso contrário, retorna False
    return resposta_usuario == resposta_correta 


def comecar_jogo():
    # iniciando a pontuação
    pontuacao = 0  
    # Embaralha a lista de perguntas
    random.shuffle(perguntas)  

    # for para percorrer nossa lista perguntas
    # enumerate é uma função em python que retorna o índice "0, 1, 2..." e o valor
    # for cria duas variaveis, index para guardar o índice do enumerate e questao para guardar o valor do dicionário
    for index, questao in enumerate(perguntas):
        # Limpa o terminal antes de exibir cada pergunta
        limpar_terminal()  
        # chama a função de exibir a pergunta e suas opçoes passando a questao e o número da pergunta (index + 1)
        exibir_pergunta(questao, index + 1)  

        # verificação da resposta do usuario
        while True:
            # Lê a resposta do usuário, remove espaços e converte para maiúscula
            resposta = input("\nDigite a sua resposta: ").strip().upper()  
            # if in, verifica se a resposta esta dentro desta lista de opçoes esperadas
            if resposta in ["A", "B", "C", "D"]:
                break  # Sai do loop se a resposta for válida
            else:
                print("Por favor, digite A, B, C ou D.") 
        

        if verificar_resposta(resposta, questao["resposta"]):
            print("✅ PARABENS, VOCÊ ACERTOU!\n")
            pontuacao += 1  # Incrementa a pontuação em 1
        else:
            print(f"❌ RESPOSTA ERRADA!, A RESPOSTA CORRETA É: {questao['resposta']}")

        time.sleep(2)  # Pausa por 2 segundos antes de mostrar a próxima pergunta

    # Apos o quiz retorna a pontuação do jogador
    return pontuacao  




# AQUI COMEÇA NOSSO CODIGO PRINCIPAL
# Inicia o jogo chamando a função comecar_jogo()
# atri
pontuacao = comecar_jogo()  


limpar_terminal()

print("=" * 30)
print("--- FIM DE JOGO ---")
print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas")
print("=" * 30)


   