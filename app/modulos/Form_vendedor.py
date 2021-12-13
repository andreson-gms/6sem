#modulo Frame do cadastro de novo vendedor
from tkinter import *
from tkinter import messagebox
from modulos.banco import dml,dql


class Cadastra_vendedor():

    def cls(self,tela):#limpa o frame da tela
        for items in tela.winfo_children():
            items.destroy()

    def bc_vendedor(self):
        lista = []
        numero = self.E_numero.get()
        nome = self.E_vendedor.get()

        vquery = f"SELECT cod_vendedor FROM tb_vendedor WHERE cod_vendedor LIKE '{numero}'"
        lista = dql(vquery)

        if lista != []:
            messagebox.showwarning("atenção", "codigo do vendedor ja cadastrado")
            return

        else:
            vquery = f'INSERT INTO tb_vendedor VALUES("{numero}","{nome}");'
            dml(vquery)

            messagebox.showinfo("Concluido", 'Vendedor cadastrado com sucesso')
            
            self.E_numero.delete(0,END)
            self.E_vendedor.delete(0,END)
            self.E_numero.focus_set()


    def __init__(self, tela):
        self.cls(tela)
        self.lb_titulo = Label(tela, text= 'Cadastrar Novo vendedor')
        self.lb_numero = Label(tela, text= 'N° do vendedor: ')
        self.lb_Vendedor = Label(tela, text= 'Nome do Vendedor: ')

        self.E_numero = Entry(tela)
        self.E_vendedor = Entry(tela)

        self.btn = Button(tela, text='Salvar',command= self.bc_vendedor)

        
        self.lb_titulo.grid(column = 0, row = 0, columnspan=2)

        self.lb_numero.grid(column=0, row=1, pady=10, sticky='e')
        self.E_numero.grid(column=1, row=1,columnspan=2, pady=10)

        self.lb_Vendedor.grid(column=0, row=2, pady=10, sticky='e')
        self.E_vendedor.grid(column=1, row=2, columnspan=2, pady=10)

        self.btn.grid(column=2, row=3, sticky='e')