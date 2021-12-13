#modulo Frame do cadastro de novo pedido
from tkinter import *
from tkinter import ttk


class Cadastra_pedido():
    def cls(self,tela):#limpa o frame da tela
        for items in tela.winfo_children():
            items.destroy()

    def bc_pedido(self):
        pass


    def __init__(self, tela):
        self.cls(tela)
        self.lb_titulo = Label(tela, text= 'Novo Pedido: ')
        self.lb_data = Label(tela, text= 'Data: ')
        self.lb_nf = Label(tela, text= 'NF: ')
        self.lb_categoria = Label(tela, text= 'Categoria: ')
        self.lb_grupo = Label(tela, text= 'Grupo: ')
        self.lb_cliente = Label(tela, text= 'Cliente: ')
        self.lb_vendedor = Label(tela, text= 'Vendedor: ')
        self.lb_quantidade = Label(tela, text= 'Quantidade: ')
        self.lb_valorT = Label(tela, text= 'Valor Total: ')

        self.et_data = Entry(tela)
        self.et_nf = Entry(tela)
        self.et_categoria = Entry(tela)
        self.et_grupo = Entry(tela)
        self.et_cliente = Entry(tela)
        self.et_vendedor = Entry(tela)
        self.et_quantidade = Entry(tela)
        self.et_valorT = Entry(tela)

        self.btn_enviar = Button(tela, text='Venviar', command=self.bc_pedido)


        self.lb_titulo.grid(row=0, column=0, pady=10, columnspan=4)

        self.lb_data.grid(row=1, column=0, pady=10, sticky='e')
        self.et_data.grid(row=1, column=1, pady=10)

        self.lb_nf.grid(row=1, column=2, pady=10, sticky='e')
        self.et_nf.grid(row=1, column=3, pady=10)

        self.lb_categoria.grid(row=2, column=0, pady=10, sticky='e')
        self.et_categoria.grid(row=2, column=1, pady=10)

        self.lb_grupo.grid(row=2, column=2, pady=10, sticky='e')
        self.et_grupo.grid(row=2, column=3, pady=10)

        self.lb_cliente.grid(row=3, column=0, pady=10, sticky='e')
        self.et_cliente.grid(row=3, column=1, pady=10)

        self.lb_vendedor.grid(row=3, column=2, pady=10, sticky='e')
        self.et_vendedor.grid(row=3, column=3, pady=10)

        self.lb_quantidade.grid(row=4, column=0, pady=10, sticky='e')
        self.et_quantidade.grid(row=4, column=1, pady=10)

        self.lb_valorT.grid(row=4, column=2, pady=10, sticky='e')
        self.et_valorT.grid(row=4, column=3, pady=10)

        self.btn_enviar.grid(row=5, column=3, sticky='e', pady=10)