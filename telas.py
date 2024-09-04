import customtkinter
from clientes import Clientes

<<<<<<< Updated upstream
janelaClientes = customtkinter.CTk()

janelaClientes.title('Clientes')
janelaClientes.geometry('350x300')

textoExibicao = customtkinter.CTkLabel(janelaClientes, text = 'Operações de Cliente')
textoExibicao.pack(padx = 10, pady = 10)

botao1 = customtkinter.CTkButton(janelaClientes, text='Criar', command=Clientes.newCliente)
botao1.pack(padx = 10, pady = 10)

botao2 = customtkinter.CTkButton(janelaClientes, text = 'Mostrar', command=Clientes.showClientes)
botao2.pack(padx=10, pady=10)

botao3 = customtkinter.CTkButton(janelaClientes, text = 'Editar', command=Clientes.editCliente)
botao3.pack(padx = 10, pady=10)

botao4 = customtkinter.CTkButton(janelaClientes, text = 'Deletar', command=Clientes.delCliente)
botao4.pack(padx=10, pady=10)

janelaClientes.mainloop()
=======
class TelaCliente:
    
    janelaC = customtkinter.CTk()

    janelaC.title('Clientes')
    janelaC.geometry('350x300')

    textoExibicao = customtkinter.CTkLabel(janelaC, text = 'Operações de Cliente')
    textoExibicao.pack(padx = 10, pady = 10)

    botao1 = customtkinter.CTkButton(janelaC, text='Criar', command=Clientes.newCliente)
    botao1.pack(padx = 10, pady = 10)

    botao2 = customtkinter.CTkButton(janelaC, text = 'Mostrar', command=Clientes.showClientes)
    botao2.pack(padx=10, pady=10)

    botao3 = customtkinter.CTkButton(janelaC, text = 'Editar', command=Clientes.editCliente)
    botao3.pack(padx = 10, pady=10)

    botao4 = customtkinter.CTkButton(janelaC, text = 'Deletar', command=Clientes.delCliente)
    botao4.pack(padx=10, pady=10)

    janelaC.mainloop()


class TelaVeiculo:
    janelaV = customtkinter.CTk()

    janelaV.title('Veiculos')
    janelaV.geometry('400x350')


>>>>>>> Stashed changes
