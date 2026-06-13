# importando a biblioteca de interface. ctk é nosso apelido
import customtkinter as ctk
# importando biblioteca responsavel por embaralhar
import random
# biblioteca responsavel para controlar tempo de exibição
import time

from database.banco import (buscar_perguntas,salvar_resultado,buscar_ranking)

# busca as perguntas que estão cadastradas no banco
perguntas = buscar_perguntas()

# variaveis que vão conterolar o quiz
indice_pergunta = 0
pontuacao = 0
nome_jogador = ""


# Configurações iniciais
# tema da nossa interface
ctk.set_appearance_mode("dark")
# cor princpal
ctk.set_default_color_theme("blue")


# Criando nossa janela
janela = ctk.CTk()
janela.title("Quiz")
janela.geometry("900x650")

# função que serve para exibir a pergunta atual
def mostrar_pergunta():

    feedback_label.configure(text="")

    pergunta = perguntas[indice_pergunta]

    numero_pergunta_label.configure(text=f"Pergunta {indice_pergunta + 1} de {len(perguntas)}")

    pergunta_label.configure(
        text=pergunta["pergunta"]
    )

    btn_a.configure(text=pergunta["opcoes"][0])
    btn_b.configure(text=pergunta["opcoes"][1])
    btn_c.configure(text=pergunta["opcoes"][2])
    btn_d.configure(text=pergunta["opcoes"][3])

# função quando o quiz termina
def finalizar_quiz():

    # Esconde os componentes do quiz
    numero_pergunta_label.pack_forget()
    pergunta_label.pack_forget()
    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()
    
    # salva o resultado do jogo no banco
    salvar_resultado(nome_jogador, pontuacao)

    # Busca o ranking do quiz
    ranking = buscar_ranking()

    # mostra o texto do ranking
    ranking_texto = "\n\n RANKING \n\n"

    for posicao, jogador in enumerate(ranking, start=1):

        ranking_texto += (
        f"{posicao}º Lugar - "
        f"{jogador[0]} "
        f"({jogador[1]} pontos)\n"
    )

    # Mostra resultado final
    pergunta_label.configure(
      text= f"QUIZ FINALIZADO!\n\n" f"Pontuação: {pontuacao}/{len(perguntas)}" + ranking_texto )

    pergunta_label.pack(pady=100)

    btn_reiniciar.pack(pady=20)

def reiniciar_quiz():

    global indice_pergunta
    global pontuacao
    global nome_jogador

    # Reinicia as variáveis
    indice_pergunta = 0
    pontuacao = 0
    nome_jogador = ""

    pergunta_label.pack_forget()
    numero_pergunta_label.pack_forget()
    feedback_label.pack_forget()
    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()
    btn_reiniciar.pack_forget()

    # Limpa campo nome
    entrada_nome.delete(0, "end")

    # Mostra tela inicial novamente
    titulo.pack(pady=20)
    entrada_nome.pack(pady=10)
    btn_comecar.pack(pady=100)


# funcao executada quando o usuario responde
def responder(alternativa):

    # Permite alterar as variáveis globais
    global indice_pergunta
    global pontuacao

    # Guarda a pergunta atual
    pergunta_atual = perguntas[indice_pergunta]

    # Verifica se o usuário acertou
    if alternativa == pergunta_atual["resposta"]:
        feedback_label.configure(text="PARABENS, RESPOSTA CORRETA!")
        pontuacao += 1
    else:
        feedback_label.configure(text=f"RESPOSTA ERRADA, CORRETA: {pergunta_atual['resposta']}")

    # Atualiza a interface para mostrar a mensagem
    janela.update()

    # Espera 1 segundo
    time.sleep(1)

    # vai para a próxima pergunta
    indice_pergunta += 1

    # Verifica se ainda existem perguntas
    if indice_pergunta < len(perguntas):
        mostrar_pergunta()
    else:
        finalizar_quiz()

   
# funcao executada ao clicar no botao de comecar o quiz
def iniciar_quiz():

    global nome_jogador

    # pega o nome digitado
    nome_jogador = entrada_nome.get()
    
    # se a pessoa n digitar nada, o nome vai ser "Jogador"
    if nome_jogador == "":
        nome_jogador = "Jogador"

    # esconde as coisas da tela inicial
    titulo.pack_forget()
    entrada_nome.pack_forget()
    btn_comecar.pack_forget()


    # embaralha as perguntas antes de serem exibidas
    random.shuffle(perguntas)

    numero_pergunta_label.pack(pady=10)
    feedback_label.pack(pady=5)
    # mostra a pergunta
    mostrar_pergunta()

    pergunta_label.pack(pady=30)

    btn_a.pack(pady=5)
    btn_b.pack(pady=5)
    btn_c.pack(pady=5)
    btn_d.pack(pady=5)

    

# criando o titulo
# parametro janela é para informar que esse componente pertence a janela
titulo = ctk.CTkLabel(janela, text="PROJETO QUIZ", font=("Arial", 20, "bold"))
# pack faz que nosso componente titulo seja exibido
titulo.pack(pady=20)

# campo para digitar o nome
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome")

entrada_nome.pack(pady=10)


# criando nosso botao de começar quiz para o nosso usuario interagir 
# parametro janela é para informar que esse componente pertence a janela
# command é para passar pro botao a funcao que ele deve executar
btn_comecar = ctk.CTkButton(janela, text="COMEÇAR QUIZ", width=150, height=40, command=iniciar_quiz)
#pady é espaço vertical
btn_comecar.pack(pady=100)

# Label responsavel para exibir a pergunta
pergunta_label = ctk.CTkLabel(janela, text="", font=("Arial", 18, "bold"), wraplength=700)
# Label para mostrar o numero da pergunta
numero_pergunta_label = ctk.CTkLabel(janela, text="", font=("Arial", 14))

feedback_label = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"))

# Botões das alternativas
btn_a = ctk.CTkButton(janela, text="A)", command=lambda: responder("A"))

btn_b = ctk.CTkButton(janela, text="B)", command=lambda: responder("B"))

btn_c = ctk.CTkButton(janela, text="C)", command=lambda: responder("C"))

btn_d = ctk.CTkButton(janela, text="D)", command=lambda: responder("D"))

btn_reiniciar = ctk.CTkButton(janela, text="JOGAR NOVAMENTE", command=reiniciar_quiz
)



# Inicia a aplicação
# mainloop vai manter nossa janela aberta
janela.mainloop()