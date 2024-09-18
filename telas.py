import customtkinter
from model.clientes import Clientes
from model.veiculos import Veiculos
from model.locacao import Locacao
from controller.clienteController import receberDadosC
from controller.veiculoController import receberDadosV


class Frame0(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Sistema Principal')
        self.tituloPrincipal.pack(padx=50, pady=25)

        self.botaoClientes = customtkinter.CTkButton(self, width=200, height=50, text='Sistema de Clientes',
                                                           command=self.buttonCliente)
        self.botaoClientes.pack(padx=75, pady=10)

        self.botaoVeiculos = customtkinter.CTkButton(self, width=200, height=50, text='Sistema de Veiculos',
                                                           command=self.buttonVeiculo)
        self.botaoVeiculos.pack(padx=75, pady=10)

        self.botaoLocacao = customtkinter.CTkButton(self, width=200, height=50, text='Sistema de Locacao',
                                                          command=self.buttonLocacao)
        self.botaoLocacao.pack(padx=75, pady=10)

        self.botaoSair = customtkinter.CTkButton(self, width=200, height=50, text='Fechar Sistema',
                                                       command=self.buttonSair)
        self.botaoSair.pack(padx=75, pady=30)

    def buttonCliente(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame1(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)

    def buttonVeiculo(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame2(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)

    def buttonLocacao(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame3(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)

    def buttonSair(self):
        self.master.destroy()
        return


class Frame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Sistema Clientes')
        self.tituloPrincipal.pack(padx=50, pady=15)

        self.botaoNewClientes = customtkinter.CTkButton(self, width=200, height=40, text='Novo Cliente',
                                                           command=self.buttonNew)
        self.botaoNewClientes.pack(padx=75, pady=10)

        self.botaoShowCliente = customtkinter.CTkButton(self, width=200, height=40, text='Mostrar Clientes',
                                                           command=self.buttonShow)
        self.botaoShowCliente.pack(padx=75, pady=10)

        self.botaoEditCliente = customtkinter.CTkButton(self, width=200, height=40, text='Editar Clientes',
                                                          command=self.buttonEdit)
        self.botaoEditCliente.pack(padx=75, pady=10)

        self.botaoDelCliente = customtkinter.CTkButton(self, width=200, height=40, text='Deletar Clientes',
                                                    command=self.buttonDel)
        self.botaoDelCliente.pack(padx=75, pady=10)

        self.botaoSair = customtkinter.CTkButton(self, width=200, height=40, text='Fechar Sistema de Clientes',
                                                       command=self.buttonSair)
        self.botaoSair.pack(padx=75, pady=30)

    def buttonNew(self):
        janela = JanelaNewCliente()
        janela.mainloop()

    def buttonShow(self):
        janela = JanelaShowCliente()
        janela.mainloop()

    def buttonEdit(self):
        janela = JanelaEditCliente()
        janela.mainloop()

    def buttonDel(self):
        janela = JanelaDelCliente()
        janela.mainloop()

    def buttonSair(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame0(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Sistema Veiculos')
        self.tituloPrincipal.pack(padx=50, pady=15)

        self.botaoNewVeiculo = customtkinter.CTkButton(self, width=200, height=40, text='Novo Veiculos',
                                                           command=self.buttonNew)
        self.botaoNewVeiculo.pack(padx=75, pady=10)

        self.botaoShowVeiculo = customtkinter.CTkButton(self, width=200, height=40, text='Mostrar Veiculos',
                                                           command=self.buttonShow)
        self.botaoShowVeiculo.pack(padx=75, pady=10)

        self.botaoEditVeiculo = customtkinter.CTkButton(self, width=200, height=40, text='Editar Veiculos',
                                                          command=self.buttonEdit)
        self.botaoEditVeiculo.pack(padx=75, pady=10)

        self.botaoDelVeiculo = customtkinter.CTkButton(self, width=200, height=40, text='Deletar Veiculos',
                                                    command=self.buttonDel)
        self.botaoDelVeiculo.pack(padx=75, pady=10)

        self.botaoSair = customtkinter.CTkButton(self, width=200, height=40, text='Fechar Sistema de Veiculos',
                                                       command=self.buttonSair)
        self.botaoSair.pack(padx=75, pady=30)

    def buttonNew(self):
        janela = JanelaNewVeiculo()
        janela.mainloop()

    def buttonShow(self):
        janela = JanelaShowVeiculo()
        janela.mainloop()

    def buttonEdit(self):
        janela = JanelaEditVeiculo()
        janela.mainloop()

    def buttonDel(self):
        janela = JanelaDelVeiculo()
        janela.mainloop()

    def buttonSair(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame0(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame3(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Sistema Locacão')
        self.tituloPrincipal.pack(padx=50, pady=15)

        self.botaoNewLocacao = customtkinter.CTkButton(self, width=200, height=40, text='Novo Locação',
                                                           command=self.buttonNew)
        self.botaoNewLocacao.pack(padx=75, pady=10)

        self.botaoShowLocacao = customtkinter.CTkButton(self, width=200, height=40, text='Mostrar Locações',
                                                           command=self.buttonShow)
        self.botaoShowLocacao.pack(padx=75, pady=10)

        self.botaoEditLocacao = customtkinter.CTkButton(self, width=200, height=40, text='Editar Locações',
                                                          command=self.buttonEdit)
        self.botaoEditLocacao.pack(padx=75, pady=10)

        self.botaoDelLocacao = customtkinter.CTkButton(self, width=200, height=40, text='Deletar Locações',
                                                    command=self.buttonDel)
        self.botaoDelLocacao.pack(padx=75, pady=10)

        self.botaoSair = customtkinter.CTkButton(self, width=200, height=40, text='Fechar Sistema de Locação',
                                                       command=self.buttonSair)
        self.botaoSair.pack(padx=75, pady=30)

    def buttonNew(self):
        janela = JanelaNewLocacao()
        janela.mainloop()

    def buttonShow(self):
        janela = JanelaShowLocacao()
        janela.mainloop()

    def buttonEdit(self):
        janela = JanelaEditLocacao()
        janela.mainloop()

    def buttonDel(self):
        janela = JanelaDelLocacao()
        janela.mainloop()

    def buttonSair(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame0(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame5(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Clientes')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Clientes().showClientes())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Editar Cliente:   (Somenete Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Editar Cliente', command=self.buttonEdit)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonEdit(self):
        cliente = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame6(self.master, cliente, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame6(customtkinter.CTkFrame):

    def __init__(self, master, cliente=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Clientes().showClientes(cliente)
        self.dadosCliente = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados do Clientes')
        self.tituloPrincipal.grid(row=0, column=0, padx=25, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Nome Atual')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox1.insert("0.0", self.dadosCliente[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Nome Cliente')
        self.label2.grid(row=2, column=0, padx=10, pady=5)

        self.entry1 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Novo Nome: ")
        self.entry1.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Idade Atual')
        self.label3.grid(row=3, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox2.insert("0.0", self.dadosCliente[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=3, column=1, padx=10, pady=5)

        self.label4 = customtkinter.CTkLabel(self, text='Idade Cliente')
        self.label4.grid(row=4, column=0, padx=10, pady=5)

        self.entry2 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Nova Idade: ")
        self.entry2.grid(row=4, column=1, padx=10, pady=5)

        self.label5 = customtkinter.CTkLabel(self, text='Sexo atual')
        self.label5.grid(row=5, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox3.insert("0.0", self.dadosCliente[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=5, column=1, padx=10, pady=5)

        self.label6 = customtkinter.CTkLabel(self, text='Sexo Cliente')
        self.label6.grid(row=6, column=0, padx=10, pady=5)

        self.entry3 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Novo Sexo: ")
        self.entry3.grid(row=6, column=1, padx=10, pady=5)

        self.label7 = customtkinter.CTkLabel(self, text='CPF Atual')
        self.label7.grid(row=7, column=0, padx=10, pady=5)

        self.textBox4 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox4.insert("0.0", self.dadosCliente[3])
        self.textBox4.configure(state='disabled')
        self.textBox4.grid(row=7, column=1, padx=10, pady=5)

        self.label8 = customtkinter.CTkLabel(self, text='CPF Cliente')
        self.label8.grid(row=8, column=0, padx=10, pady=5)

        self.entry4 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Novo CPF: ")
        self.entry4.grid(row=8, column=1, padx=10, pady=5)

        self.label9 = customtkinter.CTkLabel(self, text='Endereco atual')
        self.label9.grid(row=9, column=0, padx=10, pady=5)

        self.textBox5 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox5.insert("0.0", self.dadosCliente[4])
        self.textBox5.configure(state='disabled')
        self.textBox5.grid(row=9, column=1, padx=10, pady=5)

        self.label10 = customtkinter.CTkLabel(self, text='Endereço Cliente')
        self.label10.grid(row=10, column=0, padx=10, pady=5)

        self.entry5 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text="Novo Endereço: ")
        self.entry5.grid(row=10, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=50, text='Atualizar Informações',
                                               command=self.updateCliente())
        self.button1.grid(row=11, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=50, text='Cancelar', command=self.master.destroy)
        self.button2.grid(row=11, column=1, padx=10, pady=10)

    def updateCliente(self):
        newDados1 = self.entry1.get()
        newDados2 = self.entry2.get()
        mewDados3 = self.entry3.get()
        mewDados4 = self.entry4.get()
        mewDados5 = self.entry5.get()


class Frame7(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Clientes')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Clientes().showClientes())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Apagar Cliente:   (Apenas o Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Apagar Cliente',
                                               command=self.buttonConfirm)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonConfirm(self):
        cliente = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame8(self.master, cliente, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame8(customtkinter.CTkFrame):

    def __init__(self, master, cliente=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Clientes().showClientes(cliente)
        self.dadosCliente = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados do Cliente')
        self.tituloPrincipal.grid(row=0, column=1, padx=25, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Nome Cliente')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox1.insert("0.0", self.dadosCliente[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Idade Cliente')
        self.label2.grid(row=3, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox2.insert("0.0", self.dadosCliente[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=3, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Sexo Cliente')
        self.label3.grid(row=5, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox3.insert("0.0", self.dadosCliente[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=5, column=1, padx=10, pady=5)

        self.label4 = customtkinter.CTkLabel(self, text='CPF Cliente')
        self.label4.grid(row=7, column=0, padx=10, pady=5)

        self.textBox4 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox4.insert("0.0", self.dadosCliente[3])
        self.textBox4.configure(state='disabled')
        self.textBox4.grid(row=7, column=1, padx=10, pady=5)

        self.label5 = customtkinter.CTkLabel(self, text='Endereco Cliente')
        self.label5.grid(row=9, column=0, padx=10, pady=5)

        self.textBox5 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox5.insert("0.0", self.dadosCliente[4])
        self.textBox5.configure(state='disabled')
        self.textBox5.grid(row=9, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=50, text='Confirmar Cliente',
                                               command=self.deleteCliente)
        self.button1.grid(row=11, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=50, text='Voltar', command=self.cancelCliente)
        self.button2.grid(row=12, column=0, padx=10, pady=30)

    def deleteCliente(self):
        print("Apertou comfirmar!")

    def cancelCliente(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame7(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame10(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Veiculos')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Veiculos().showVeiculos())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Editar Veiculo:   (Somenete Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Editar Veiculo',
                                               command=self.buttonEdit)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonEdit(self):
        veiculo = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame11(self.master, veiculo, width=350, height=400)
        self.master.frameAtual.place(x=25, y=15)


class Frame11(customtkinter.CTkFrame):

    def __init__(self, master, veiculo=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Veiculos().showVeiculos(veiculo)
        self.dadosVeiculo = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados do Veiculo')
        self.tituloPrincipal.grid(row=0, column=0, padx=20, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Marca Atual')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox1.insert("0.0", self.dadosVeiculo[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Marca Veiculo')
        self.label2.grid(row=2, column=0, padx=10, pady=5)

        self.entry1 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Nova Marca: ")
        self.entry1.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Modelo Atual')
        self.label3.grid(row=3, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox2.insert("0.0", self.dadosVeiculo[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=3, column=1, padx=10, pady=5)

        self.label4 = customtkinter.CTkLabel(self, text='Modelo Veiculo')
        self.label4.grid(row=4, column=0, padx=10, pady=5)

        self.entry2 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Novo Modelo: ")
        self.entry2.grid(row=4, column=1, padx=10, pady=5)

        self.label5 = customtkinter.CTkLabel(self, text='Versão atual')
        self.label5.grid(row=5, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox3.insert("0.0", self.dadosVeiculo[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=5, column=1, padx=10, pady=5)

        self.label6 = customtkinter.CTkLabel(self, text='Versão Veiculo')
        self.label6.grid(row=6, column=0, padx=10, pady=5)

        self.entry3 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Nova Versão: ")
        self.entry3.grid(row=6, column=1, padx=10, pady=5)

        self.label7 = customtkinter.CTkLabel(self, text='Motor Atual')
        self.label7.grid(row=7, column=0, padx=10, pady=5)

        self.textBox4 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox4.insert("0.0", self.dadosVeiculo[3])
        self.textBox4.configure(state='disabled')
        self.textBox4.grid(row=7, column=1, padx=10, pady=5)

        self.label8 = customtkinter.CTkLabel(self, text='Motor Veiculo')
        self.label8.grid(row=8, column=0, padx=10, pady=5)

        self.entry4 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Novo Motor: ")
        self.entry4.grid(row=8, column=1, padx=10, pady=5)

        self.label9 = customtkinter.CTkLabel(self, text='Cor atual')
        self.label9.grid(row=9, column=0, padx=10, pady=5)

        self.textBox5 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox5.insert("0.0", self.dadosVeiculo[4])
        self.textBox5.configure(state='disabled')
        self.textBox5.grid(row=9, column=1, padx=10, pady=5)

        self.label10 = customtkinter.CTkLabel(self, text='Cor Veiculo')
        self.label10.grid(row=10, column=0, padx=10, pady=5)

        self.entry5 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Nova Cor: ")
        self.entry5.grid(row=10, column=1, padx=10, pady=5)

        self.label11 = customtkinter.CTkLabel(self, text='Placa Atual')
        self.label11.grid(row=11, column=0, padx=10, pady=5)

        self.textBox6 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox6.insert("0.0", self.dadosVeiculo[5])
        self.textBox6.configure(state='disabled')
        self.textBox6.grid(row=11, column=1, padx=10, pady=5)

        self.label12 = customtkinter.CTkLabel(self, text='Placa Veiculo')
        self.label12.grid(row=12, column=0, padx=10, pady=5)

        self.entry6 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Nova Placa: ")
        self.entry6.grid(row=12, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=35, text='Atualizar Informações',
                                               command=self.updateVeiculo)
        self.button1.grid(row=13, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=35, text='Cancelar', command=self.master.destroy)
        self.button2.grid(row=13, column=1, padx=10, pady=10)

    def updateVeiculo(self):
        newDados1 = self.entry1.get()
        newDados2 = self.entry2.get()
        mewDados3 = self.entry3.get()
        mewDados4 = self.entry4.get()
        mewDados5 = self.entry5.get()
        newDados6 = self.entry6.get()


class Frame12(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Veiculos')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Veiculos().showVeiculos())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Apagar Veiculo:   (Apenas o Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Apagar Veiculo',
                                               command=self.buttonConfirm)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonConfirm(self):
        veiculo = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame13(self.master, veiculo, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame13(customtkinter.CTkFrame):

    def __init__(self, master, veiculo=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Veiculos().showVeiculos(veiculo)
        self.dadosVeiculo = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados do Veiculo')
        self.tituloPrincipal.grid(row=0, column=1, padx=25, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Marca Veiculo')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox1.insert("0.0", self.dadosVeiculo[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Modelo Veiculo')
        self.label2.grid(row=2, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox2.insert("0.0", self.dadosVeiculo[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Versão Veiculo')
        self.label3.grid(row=3, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox3.insert("0.0", self.dadosVeiculo[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=3, column=1, padx=10, pady=5)

        self.label4 = customtkinter.CTkLabel(self, text='Motor Veiculo')
        self.label4.grid(row=4, column=0, padx=10, pady=5)

        self.textBox4 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox4.insert("0.0", self.dadosVeiculo[3])
        self.textBox4.configure(state='disabled')
        self.textBox4.grid(row=4, column=1, padx=10, pady=5)

        self.label5 = customtkinter.CTkLabel(self, text='Cor Veiculo')
        self.label5.grid(row=5, column=0, padx=10, pady=5)

        self.textBox5 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox5.insert("0.0", self.dadosVeiculo[4])
        self.textBox5.configure(state='disabled')
        self.textBox5.grid(row=5, column=1, padx=10, pady=5)

        self.label6 = customtkinter.CTkLabel(self, text='Placa Veiculo')
        self.label6.grid(row=6, column=0, padx=10, pady=5)

        self.textBox6 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox6.insert("0.0", self.dadosVeiculo[5])
        self.textBox6.configure(state='disabled')
        self.textBox6.grid(row=6, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=50, text='Confirmar Veiculo',
                                               command=self.deleteVeiculo)
        self.button1.grid(row=8, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=50, text='Voltar', command=self.cancelVeiculo)
        self.button2.grid(row=9, column=0, padx=10, pady=30)

    def deleteVeiculo(self):
        print("Apertou comfirmar!")

    def cancelVeiculo(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame12(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame15(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Locações')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Locacao().showLocacao())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Editar Locação:   (Somenete Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Editar Veiculo',
                                               command=self.buttonEdit)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonEdit(self):
        locacao = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame16(self.master, locacao, width=350, height=400)
        self.master.frameAtual.place(x=25, y=15)


class Frame16(customtkinter.CTkFrame):

    def __init__(self, master, locacao=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Locacao().showLocacao(locacao)
        self.dadosLocaco = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados da Locação')
        self.tituloPrincipal.grid(row=0, column=0, padx=20, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Data Atual')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox1.insert("0.0", self.dadosLocaco[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Data da Locação')
        self.label2.grid(row=2, column=0, padx=10, pady=5)

        self.entry1 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Nova Data: ")
        self.entry1.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Cliente Atual')
        self.label3.grid(row=3, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox2.insert("0.0", self.dadosLocaco[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=3, column=1, padx=10, pady=5)

        self.label4 = customtkinter.CTkLabel(self, text='Cliente Locatario')
        self.label4.grid(row=4, column=0, padx=10, pady=5)

        self.entry2 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Novo Cliente: ")
        self.entry2.grid(row=4, column=1, padx=10, pady=5)

        self.label5 = customtkinter.CTkLabel(self, text='Veiculo atual')
        self.label5.grid(row=5, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=25)
        self.textBox3.insert("0.0", self.dadosLocaco[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=5, column=1, padx=10, pady=5)

        self.label6 = customtkinter.CTkLabel(self, text='Veiculo Locado')
        self.label6.grid(row=6, column=0, padx=10, pady=5)

        self.entry3 = customtkinter.CTkEntry(self, width=150, height=25, placeholder_text="Novo Veiculo: ")
        self.entry3.grid(row=6, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=35, text='Atualizar Informações',
                                               command=self.updateLocacao)
        self.button1.grid(row=13, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=35, text='Cancelar', command=self.master.destroy)
        self.button2.grid(row=13, column=1, padx=10, pady=10)

    def updateLocacao(self):
        newDados1 = self.entry1.get()
        newDados2 = self.entry2.get()
        mewDados3 = self.entry3.get()


class Frame17(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tituloPrinciopal = customtkinter.CTkLabel(self, text='Lista de Locações')
        self.tituloPrinciopal.pack(padx=50, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Locacao().showLocacao())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30,
                                             placeholder_text="Apagar Locação:   (Apenas o Número  ex: 1)")
        self.entry1.pack(padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=200, height=40, text='Apagar Locação',
                                               command=self.buttonConfirm)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=200, height=40, text="Cancelar", command=self.master.destroy)
        self.button2.pack(padx=10, pady=30)

    def buttonConfirm(self):
        locacao = int(self.entry1.get().lstrip())
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame18(self.master, locacao, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)


class Frame18(customtkinter.CTkFrame):

    def __init__(self, master, locacao=0, **kwargs):
        super().__init__(master, **kwargs)

        key, values = Locacao().showLocacao(locacao)
        self.dadosLocacao = values

        self.tituloPrincipal = customtkinter.CTkLabel(self, text='Dados da Locação')
        self.tituloPrincipal.grid(row=0, column=1, padx=25, pady=10)

        self.label1 = customtkinter.CTkLabel(self, text='Data da Locação')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.textBox1 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox1.insert("0.0", self.dadosLocacao[0])
        self.textBox1.configure(state='disabled')
        self.textBox1.grid(row=1, column=1, padx=10, pady=5)

        self.label2 = customtkinter.CTkLabel(self, text='Cliente Locatario')
        self.label2.grid(row=2, column=0, padx=10, pady=5)

        self.textBox2 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox2.insert("0.0", self.dadosLocacao[1])
        self.textBox2.configure(state='disabled')
        self.textBox2.grid(row=2, column=1, padx=10, pady=5)

        self.label3 = customtkinter.CTkLabel(self, text='Veiculo Locatado')
        self.label3.grid(row=3, column=0, padx=10, pady=5)

        self.textBox3 = customtkinter.CTkTextbox(self, width=150, height=30)
        self.textBox3.insert("0.0", self.dadosLocacao[2])
        self.textBox3.configure(state='disabled')
        self.textBox3.grid(row=3, column=1, padx=10, pady=5)

        self.button1 = customtkinter.CTkButton(self, width=150, height=50, text='Confirmar Locação',
                                               command=self.deleteLocacao)
        self.button1.grid(row=8, column=0, padx=15, pady=10)

        self.button2 = customtkinter.CTkButton(self, width=100, height=50, text='Voltar', command=self.cancelLocacao)
        self.button2.grid(row=9, column=0, padx=10, pady=30)

    def deleteLocacao(self):
        print("Apertou comfirmar!")

    def cancelLocacao(self):
        self.master.frameAtual.place_forget()
        self.master.frameAtual = Frame17(self.master, width=350, height=400)
        self.master.frameAtual.place(x=25, y=25)






class JanelaNewCliente(customtkinter.CTk):

    def __init__(self):    #, master, **kwargs):
        super().__init__()       #master, **kwargs)

        self.title('Novo Cliente')
        self.geometry('450x500')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Nome')
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Mario')
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(self, text='Idade')
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='18')
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        self.label3 = customtkinter.CTkLabel(self, text='Sexo')
        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.entry3 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='M/F')
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        self.label4 = customtkinter.CTkLabel(self, text='CPF')
        self.label4.grid(row=3, column=0, padx=10, pady=10)
        self.entry4 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='123.456.789-00')
        self.entry4.grid(row=3, column=1, padx=10, pady=10)

        self.label5 = customtkinter.CTkLabel(self, text='Endereco')
        self.label5.grid(row=4, column=0, padx=10, pady=10)
        self.entry5 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Uast, Bloco2, Sala12')
        self.entry5.grid(row=4, column=1, padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Adicionar Novo Cliente',
                                               command=self.receberDados)
        self.button1.grid(row=6, column=1, padx=10, pady=10)
        self.button2 = customtkinter.CTkButton(self, width=150, height=40, text='Cancelar', command=self.destroy)
        self.button2.grid(row=7, column=1, padx=10, pady=50)

    def receberDados(self):
        dados1 = self.entry1.get()
        dados2 = self.entry2.get()
        dados3 = self.entry3.get()
        dados4 = self.entry4.get()
        dados5 = self.entry5.get()
        listaDados = [dados1, dados2, dados3, dados4, dados5]
        receberDadosC(listaDados) 


class JanelaShowCliente(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Exibir Clientes')
        self.geometry('350x500')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Lista Clientes')
        self.label1.pack(padx=10, pady=10)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Clientes().showClientes())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Voltar', command=self.destroy)
        self.button1.pack(padx=10, pady=10)


class JanelaEditCliente(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Editar Cliente')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame5(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)


class JanelaDelCliente(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Deletar Cliente')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame7(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)


class JanelaNewVeiculo(customtkinter.CTk):

    def __init__(self):    #, master, **kwargs):
        super().__init__()       #master, **kwargs)

        self.title('Novo Veiculo')
        self.geometry('450x500')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Marca')
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Fiat')
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(self, text='Modelo')
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Uno Mille')
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        self.label3 = customtkinter.CTkLabel(self, text='Versao')
        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.entry3 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Way')
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        self.label4 = customtkinter.CTkLabel(self, text='Motor')
        self.label4.grid(row=3, column=0, padx=10, pady=10)
        self.entry4 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='1.4')
        self.entry4.grid(row=3, column=1, padx=10, pady=10)

        self.label5 = customtkinter.CTkLabel(self, text='Cor')
        self.label5.grid(row=4, column=0, padx=10, pady=10)
        self.entry5 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='Cinza')
        self.entry5.grid(row=4, column=1, padx=10, pady=10)

        self.label6 = customtkinter.CTkLabel(self, text='Placa')
        self.label6.grid(row=5, column=0, padx=10, pady=10)
        self.entry6 = customtkinter.CTkEntry(self, width=250, height=30, placeholder_text='UNO-1234')
        self.entry6.grid(row=5, column=1, padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Adicionar Novo Veiculo',
                                               command=self.receberDados)
        self.button1.grid(row=6, column=1, padx=10, pady=10)
        self.button2 = customtkinter.CTkButton(self, width=150, height=40, text='Cancelar', command=self.destroy)
        self.button2.grid(row=7, column=1, padx=10, pady=50)

    def receberDados(self):
        dados1 = self.entry1.get()
        dados2 = self.entry2.get()
        dados3 = self.entry3.get()
        dados4 = self.entry4.get()
        dados5 = self.entry5.get()
        dados6 = self.entry6.get()
        listaDados = [dados1, dados2, dados3, dados4, dados5, dados6]
        receberDadosV(listaDados)


class JanelaShowVeiculo(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Exibir Clientes')
        self.geometry('350x500')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Lista Veiculo')
        self.label1.pack(padx=10, pady=10)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Veiculos().showVeiculos())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Voltar', command=self.destroy)
        self.button1.pack(padx=10, pady=10)


class JanelaEditVeiculo(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Editar Veiculo')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame10(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)


class JanelaDelVeiculo(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Deletar Veiculo')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame12(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)


class JanelaNewLocacao(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Nova Locacao')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Data Nova locação')
        self.label1.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(self, text='Insira a Data: ')
        self.label2.grid(row=1, column=0, padx=10, pady=15)

        self.entry1 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text='01/01/1001')
        self.entry1.grid(row=1, column=1, padx=10, pady=15)

        self.label3 = customtkinter.CTkLabel(self, text='Insira o CPF do Cliente: ')
        self.label3.grid(row=3, column=0, padx=10, pady=15)

        self.entry2 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text='123.456.789-00')
        self.entry2.grid(row=3, column=1, padx=10, pady=15)

        self.label4 = customtkinter.CTkLabel(self, text='Insira a Placa do veiculo: ')
        self.label4.grid(row=5, column=0, padx=10, pady=15)

        self.entry3 = customtkinter.CTkEntry(self, width=150, height=30, placeholder_text='ABC-1234')
        self.entry3.grid(row=5, column=1, padx=10, pady=15)

        self.button1 = customtkinter.CTkButton(self, width=120, height=30, text='Mostrar Clientes',
                                               command=self.mostrarJanelaCliente)
        self.button1.grid(row=2, column=1, padx=10, pady=15)

        self.button2 = customtkinter.CTkButton(self, width=120, height=30, text='Mostrar Veiculos',
                                               command=self.mostrarJanelaVeiculo)
        self.button2.grid(row=4, column=1, padx=10, pady=15)

        self.button3 = customtkinter.CTkButton(self, width=150, height=50, text='Confirmar Locação',
                                               command=self.receberLocacao)
        self.button3.grid(row=6, column=0, padx=10, pady=25)

        self.button4 = customtkinter.CTkButton(self, width=150, height=50, text='Cancelar', command=self.destroy)
        self.button4.grid(row=7, column=0, padx=10, pady=25)

    def mostrarJanelaCliente(self):
        janela = JanelaShowCliente()
        janela.mainloop()

    def mostrarJanelaVeiculo(self):
        janela = JanelaShowVeiculo()
        janela.mainloop()

    def receberLocacao(self):
        dados1 = self.entry1.get()
        dados2 = self.entry2.get()
        dados3 = self.entry3.get()
        listaDados = [dados1, dados2, dados3]
        print("Apertou comfirmar!")


class JanelaShowLocacao(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Exibir Locações')
        self.geometry('350x500')
        self.resizable(width=False, height=False)

        self.label1 = customtkinter.CTkLabel(self, text='Lista Locações')
        self.label1.pack(padx=10, pady=10)

        self.textBox1 = customtkinter.CTkTextbox(self, width=250, height=300)
        self.textBox1.insert("0.0", Locacao().showLocacao())
        self.textBox1.configure(state='disabled')
        self.textBox1.pack(padx=10, pady=10)

        self.button1 = customtkinter.CTkButton(self, width=150, height=40, text='Voltar', command=self.destroy)
        self.button1.pack(padx=10, pady=10)


class JanelaEditLocacao(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Editar Locacao')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame15(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)



class JanelaDelLocacao(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Deletar Locacao')
        self.geometry('400x600')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame17(self, width=350, height=400)
        self.frameAtual.place(x=65, y=25)





class JanelaInicial(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title('Sistema Principal')
        self.geometry('400x450')
        self.resizable(width=False, height=False)

        self.frameAtual = Frame0(self, width=350, height=400)
        self.frameAtual.place(x=25, y=25)



telaInicial = JanelaInicial()

telaInicial.mainloop()

# telaCadastro = JanelaNewCliente()

# telaCadastro.mainloop()


