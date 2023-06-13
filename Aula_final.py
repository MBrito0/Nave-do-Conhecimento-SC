#Criando uma tela de cadastro

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'nave'
)
  #criando as funções
def atualizar_treeview():
    treeview.delete(* treeview.get_children())

    cursor = conexao.cursor()
    comando = 'select* from tb_login'
    cursor.execute(comando)

    for row in cursor:
        treeview.insert("","end", text= row[0], values=(row[1], row[2]))

    cursor.close()


def cadastrar():
    conexao._open_connection()
    nome = campo_nome.get()
    login = campo_login.get()
    senha = campo_senha.get()

    cursor = conexao.cursor()
    comando = f'insert into tb_login(nome,login,senha) values("{nome}", "{login}", "{senha}")'
    cursor.execute(comando)
    conexao.commit()
    atualizar_treeview()

    cursor.close()
    conexao.close()
    #Funçaõ limpar
    campo_nome.delete(0,END)
    campo_login.delete(0,END)
    campo_senha.delete(0,END)

def pesquisar():
    conexao._open_connection()
    nome = campo_nome.get()
    cursor = conexao.cursor()
    comando = f'select * from tb_login where nome = "{nome}"'
    cursor.execute(comando)
    resultado = cursor.fetchone()

    if resultado: 
        campo_nome.delete(0,END)
        campo_nome.insert(0,resultado[1])
        campo_login.delete(0,END)
        campo_login.insert(0,resultado[2])
        campo_senha.delete(0,END)
        campo_senha.insert(0,resultado[3])
    else:
        messagebox.showinfo("pesquisa", "Nenhum registro encontrado!")

    cursor.close()
    conexao.close()



  #Criando campos para o acesso,   # criando campo de texto com as informações
janela = Tk()
janela.title("-Tela de cadastro")
janela.geometry("900x500")

frame_esquerda = Frame(janela)
frame_esquerda.pack(side=LEFT, padx=10,pady=10)

label_nome = Label(frame_esquerda, text="nome: ")
label_nome.pack()
campo_nome = Entry(frame_esquerda)
campo_nome.pack()

label_login = Label(frame_esquerda, text="login: ")
label_login.pack()
campo_login = Entry(frame_esquerda)
campo_login.pack()

label_senha = Label(frame_esquerda, text="senha: ")
label_senha.pack()
campo_senha = Entry(frame_esquerda, show= "*")
campo_senha.pack()

   #criando um botão no top
frame_direita = Frame(janela)
frame_direita.pack(side=TOP, padx=10, pady=10)

botao_cadastrar = Button(frame_direita, text="cadastrar", command=cadastrar, width=10)
botao_cadastrar.pack(side=TOP, padx=5)

botao_editar = Button(frame_direita, text="editar", command="", width=10)
botao_editar.pack(side=TOP, padx=5)

botao_excluir = Button(frame_direita, text="excluir", command="", width=10)
botao_excluir.pack(side=TOP, padx=5)

botao_pesquisar = Button(frame_direita, text="pesquisar", command=pesquisar, width=10)
botao_pesquisar.pack(side=TOP, padx=5)

botao_cancelar = Button(frame_direita, text="cancelar", command="", width=10)
botao_cancelar.pack(side=TOP, padx=5)

#criando uma estrutura treeview
treeview = Treeview (frame_esquerda,columns=("nome","login"))
treeview.heading("#0", text= "ID")
treeview.heading("nome", text= "nome")
treeview.heading("login", text= "login")
treeview.pack(fill = "both", expand= True, padx=10, pady=10)

#criar um comando
atualizar_treeview()




janela.mainloop()