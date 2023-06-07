import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    login = entry_login.get()
    password = entry_password.get()

    # Aqui você pode adicionar a lógica para processar os dados do formulário, como verificar a validade do login e senha

    messagebox.showinfo("Formulário enviado", "O formulário foi enviado com sucesso!")

# Criação da janela principal
window = tk.Tk()
window.title("Formulário")
window.geometry("300x200")

# Criação dos rótulos e campos de entrada
label_name = tk.Label(window, text="Nome:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_login = tk.Label(window, text="Login:")
label_login.pack()
entry_login = tk.Entry(window)
entry_login.pack()

label_password = tk.Label(window, text="Senha:")
label_password.pack()
entry_password = tk.Entry(window, show="*")  # O parâmetro show="*" é usado para exibir os caracteres digitados como asteriscos
entry_password.pack()

# Botão de envio do formulário
submit_button = tk.Button(window, text="Enviar", command=submit_form)
submit_button.pack()

# Execução da janela principal
window.mainloop()


