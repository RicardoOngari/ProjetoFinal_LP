# importando a biblioteca de interface. ctk é nosso apelido
import customtkinter as ctk


# Configurações iniciais
# tema da nossa interface
ctk.set_appearance_mode("dark")
# cor princpal
ctk.set_default_color_theme("blue")


# Criando nossa janela
janela = ctk.CTk()
janela.title("Quiz")
janela.geometry("800x500")


def iniciar_quiz():
    print("Quiz iniciado")



# criando o titulo
# parametro janela é para informar que esse componente pertence a janela
titulo = ctk.CTkLabel(janela, text="PROJETO QUIZ", font=("Arial", 20, "bold"))
# pack faz que nosso componente titulo seja exibido
titulo.pack(pady=20)


# criando nosso botao de começar quiz para o nosso usuario interagir 
# parametro janela é para informar que esse componente pertence a janela
# command é para passar pro botao a funcao que ele deve executar
btn_comecar = ctk.CTkButton(janela, text="COMEÇAR QUIZ", width=150, height=40, command=iniciar_quiz)
#pady é espaço vertical
btn_comecar.pack(pady=100)



# Inicia a aplicação
# mainloop vai manter nossa janela aberta
janela.mainloop()