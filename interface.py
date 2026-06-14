# -------------INTERFACE E LÓGICA DO QUIZ--------------


# =====================================================
# IMPORTAÇÕES
# =====================================================

# Biblioteca de interface gráfica (CustomTkinter)
import customtkinter as ctk

# Biblioteca responsável por embaralhar as perguntas
import random

# Biblioteca responsável por controlar tempo de exibição
import time

# Funções do banco de dados
from database.banco import (buscar_perguntas, salvar_resultado, buscar_ranking
)


# =====================================================
# DADOS DO QUIZ
# =====================================================

# Busca todas as perguntas cadastradas no banco
perguntas = buscar_perguntas()

# Variáveis de controle do quiz
indice_pergunta = 0
pontuacao = 0
nome_jogador = ""


# =====================================================
# CONFIGURAÇÕES DA INTERFACE
# =====================================================

# Define o tema da aplicação
ctk.set_appearance_mode("dark")

# Define a cor principal da interface
ctk.set_default_color_theme("blue")


# =====================================================
# JANELA PRINCIPAL
# =====================================================

janela = ctk.CTk()
janela.title("Quiz")
janela.geometry("900x650")


# =====================================================
# FUNÇÕES DO QUIZ
# =====================================================

def mostrar_pergunta():
    """
    Exibe a pergunta atual e suas alternativas.
    """

    # Limpa mensagens de feedback anteriores
    feedback_label.configure(text="")

    # Obtém a pergunta atual
    pergunta = perguntas[indice_pergunta]

    # Atualiza contador de perguntas
    numero_pergunta_label.configure(
        text=f"Pergunta {indice_pergunta + 1} de {len(perguntas)}"
    )

    # Exibe o enunciado da pergunta
    pergunta_label.configure(
        text=pergunta["pergunta"]
    )

    # Atualiza as alternativas nos botões
    btn_a.configure(text=pergunta["opcoes"][0])
    btn_b.configure(text=pergunta["opcoes"][1])
    btn_c.configure(text=pergunta["opcoes"][2])
    btn_d.configure(text=pergunta["opcoes"][3])


def finalizar_quiz():
    """
    Executada quando todas as perguntas forem respondidas.
    Exibe a pontuação final e o ranking.
    """

    # Esconde os componentes do quiz
    numero_pergunta_label.pack_forget()
    pergunta_label.pack_forget()
    feedback_label.pack_forget()
    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()

    # Salva o resultado no banco de dados
    salvar_resultado(nome_jogador, pontuacao)

    # Busca ranking atualizado
    ranking = buscar_ranking()

    # Monta texto do ranking
    ranking_texto = "\n\nRANKING\n\n"

    for posicao, jogador in enumerate(ranking, start=1):

        ranking_texto += (
            f"{posicao}º Lugar - "
            f"{jogador[0]} "
            f"({jogador[1]} pontos)\n"
        )

    # Exibe resultado final
    pergunta_label.configure(
        text=
        f"QUIZ FINALIZADO!\n\n"
        f"Pontuação: {pontuacao}/{len(perguntas)}"
        + ranking_texto
    )

    pergunta_label.pack(pady=100)

    # Exibe botão para reiniciar
    btn_reiniciar.pack(pady=20)


def reiniciar_quiz():
    """
    Reinicia o quiz e retorna para a tela inicial.
    """

    global indice_pergunta
    global pontuacao
    global nome_jogador

    # Reinicia variáveis do jogo
    indice_pergunta = 0
    pontuacao = 0
    nome_jogador = ""

    # Oculta componentes do quiz
    pergunta_label.pack_forget()
    numero_pergunta_label.pack_forget()
    feedback_label.pack_forget()

    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()

    btn_reiniciar.pack_forget()

    # Limpa o campo de nome
    entrada_nome.delete(0, "end")

    # Exibe novamente a tela inicial
    titulo.pack(pady=20)
    entrada_nome.pack(pady=10)
    btn_comecar.pack(pady=100)


def responder(alternativa):
    """
    Verifica a resposta do usuário e avança para
    a próxima pergunta.
    """

    global indice_pergunta
    global pontuacao

    # Obtém a pergunta atual
    pergunta_atual = perguntas[indice_pergunta]

    # Verifica se a resposta está correta
    if alternativa == pergunta_atual["resposta"]:

        feedback_label.configure(
            text="PARABENS, RESPOSTA CORRETA!"
        )

        pontuacao += 1

    else:

        feedback_label.configure(
            text=f"RESPOSTA ERRADA, CORRETA: {pergunta_atual['resposta']}"
        )

    # Atualiza a interface para exibir o feedback
    janela.update()

    # Aguarda 1 segundo
    time.sleep(2)

    # Avança para a próxima pergunta
    indice_pergunta += 1

    # Verifica se ainda existem perguntas
    if indice_pergunta < len(perguntas):
        mostrar_pergunta()
    else:
        finalizar_quiz()


def iniciar_quiz():
    """
    Inicia o quiz após o usuário clicar em
    'COMEÇAR QUIZ'.
    """

    global nome_jogador

    # Obtém o nome digitado
    nome_jogador = entrada_nome.get()

    # Caso nenhum nome seja informado
    if nome_jogador == "":
        nome_jogador = "Jogador"

    # Oculta elementos da tela inicial
    titulo.pack_forget()
    entrada_nome.pack_forget()
    btn_comecar.pack_forget()

    # Embaralha as perguntas
    random.shuffle(perguntas)

    # Exibe componentes do quiz
    numero_pergunta_label.pack(pady=10)
    

    # Mostra primeira pergunta
    mostrar_pergunta()

    pergunta_label.pack(pady=30)

    btn_a.pack(pady=5)
    btn_b.pack(pady=5)
    btn_c.pack(pady=5)
    btn_d.pack(pady=5)

    feedback_label.pack(pady=15)


# =====================================================
# COMPONENTES DA INTERFACE
# =====================================================

# Título principal
titulo = ctk.CTkLabel(janela, text="PROJETO QUIZ", font=("Arial", 20, "bold")
)

titulo.pack(pady=20)

# Campo para digitar o nome
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Digite seu nome", width=300, height=40)

entrada_nome.pack(pady=100)

# Botão para iniciar o quiz
btn_comecar = ctk.CTkButton(janela, text="COMEÇAR QUIZ", width=150, height=40, command=iniciar_quiz)

btn_comecar.pack(pady=50)

# Label responsável por exibir a pergunta
pergunta_label = ctk.CTkLabel(janela, text="", font=("Arial", 18, "bold"), wraplength=700)

# Label responsável por exibir o número da pergunta
numero_pergunta_label = ctk.CTkLabel(janela, text="", font=("Arial", 14))

# Label responsável pelo feedback
feedback_label = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"))

# =====================================================
# BOTÕES DAS ALTERNATIVAS
# =====================================================

btn_a = ctk.CTkButton(janela, text="A)", command=lambda: responder("A"))

btn_b = ctk.CTkButton(janela, text="B)", command=lambda: responder("B"))

btn_c = ctk.CTkButton(janela, text="C)", command=lambda: responder("C"))

btn_d = ctk.CTkButton(janela, text="D)", command=lambda: responder("D"))

# Botão para reiniciar o quiz
btn_reiniciar = ctk.CTkButton(janela, text="JOGAR NOVAMENTE", command=reiniciar_quiz)


# =====================================================
# EXECUÇÃO DA APLICAÇÃO
# =====================================================

# Mantém a janela aberta
janela.mainloop()