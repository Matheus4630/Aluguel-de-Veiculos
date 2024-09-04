import customtkinter
from clientes import Clientes

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
