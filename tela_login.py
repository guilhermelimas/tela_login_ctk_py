import customtkinter as ctk
from tkinter import *


class LoginPanel:
    def __init__(self):
        self.janela = ctk.CTk()
        self.executar_tela_login()
    
    def executar_tela_login(self):
        self.tema()
        self.criar_tela_login()
        self.janela.mainloop()
    
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    
    def criar_tela_login(self):
        self.janela.geometry("800x400") #tamanho da janela
        self.janela.title("AIWhisperBot") #titulo da janela
        self.janela.iconbitmap("img/icon_png.ico")
        self.janela.resizable(False, False) #resizable na janela para não ser redimensionável
        self.criar_interface_login() #chama a função que cria a interface
        
    def criar_interface_login(self): #função que cria a interface do login
        self.tela_login() #chama a função que cria a tela

    
    def tela_login(self):
        # Imagem do login
        img = PhotoImage(file="img/1.png")
        Label_img = ctk.CTkLabel(master=self.janela, image=img, text=None)
        Label_img.place(x=1, y=0)
        
        # Login container
        login_frame = ctk.CTkFrame(master=self.janela, height=396, width=320)
        login_frame.pack(side=RIGHT)

        # título do texto
        label = ctk.CTkLabel(master=login_frame, text='Faça o Login', font=('Roboto', 20, 'bold'), text_color='white')
        label.place(x=100, y=30)

        # campo de login
        login = ctk.CTkEntry(master=login_frame, placeholder_text="Usuário", width=300, font=("Roboto", 14))
        login.place(x=10, y=105)
        label1 = ctk.CTkLabel(master=login_frame, text="* O Usuário é obrigatório", text_color="#F14E09", font=("Roboto", 10))
        label1.place(x=25, y=133)

        # campo de senha
        senha = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*")
        senha.place(x=10, y=165)
        label2 = ctk.CTkLabel(master=login_frame, text="* A senha é obrigatória", text_color="#F14E09", font=("Roboto", 10))
        label2.place(x=25, y=193)

        # Relembrar login
        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar do Login")
        checkbox.place(x=25, y=225)
        
        # Botão de login
        botao_login = ctk.CTkButton(master=login_frame, text="Login", width=300, fg_color="#F14E09")
        botao_login.place(x=10, y=285)
        creditos = ctk.CTkLabel(master=login_frame, text="Criado por srzero.dev", text_color="white", font=("Roboto", 10))
        creditos.place(x=113, y=370)

LoginPanel()
