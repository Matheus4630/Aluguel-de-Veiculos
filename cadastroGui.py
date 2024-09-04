import customtkinter
from clientes import Clientes

janela = customtkinter.CTk()

janela.title('Clientes')
janela.geometry('350x300')

textoExibicao = customtkinter.CTkLabel(janela, text = 'Operações de Cliente')
textoExibicao.pack(padx = 10, pady = 10)

botao1 = customtkinter.CTkButton(janela, text='Criar', command=Clientes.newCliente)
botao1.pack(padx = 10, pady = 10)

botao2 = customtkinter.CTkButton(janela, text = 'Mostrar', command=Clientes.showClientes)
botao2.pack(padx=10, pady=10)

botao3 = customtkinter.CTkButton(janela, text = 'Editar', command=Clientes.editCliente)
botao3.pack(padx = 10, pady=10)

botao4 = customtkinter.CTkButton(janela, text = 'Deletar', command=Clientes.delCliente)
botao4.pack(padx=10, pady=10)

janela.mainloop()