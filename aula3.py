from tkinter import *

def click():
    text.configure(text = "ligado")

janela = Tk()

janela.title("Minha Janela")

#janela.iconbitmap() #imagem peguena na aba ao do titulo

janela.geometry("400x300") #lagura x altura

janela.resizable(True,True) #permite redmensionar em largura e comprimento

text = Label(janela, text= "desligar")
text.pack() #centraliar o texto

Button = Button(janela, text = "ligar", command=click)
Button.pack()


janela.mainloop()
