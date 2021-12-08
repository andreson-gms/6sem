#modulo Frame do cadastro de novo vendedor
from tkinter import *
from tkinter import messagebox
from modulos.banco import dml,dql
from modulos import cls

class C_vendedor():
    def bc_vendedor(self,bole,confirma):
        lista = []
        numero = self.E_numero.get()
        nome = self.E_vendedor.get()
        if bole:
            vquery = f"UPDATE `tb_vendedor` SET `cod_vendedor`='{numero}',`vendedor`='{nome}' WHERE `cod_vendedor`='{confirma}'"
            dml(vquery)
            messagebox.showinfo("Concluido", 'Vendedor alterado com sucesso')
        else:
            vquery = f"SELECT cod_vendedor FROM tb_vendedor WHERE cod_vendedor LIKE '{numero}'"
            lista = dql(vquery)
            if lista != []:
                messagebox.showwarning("atenção", "codogo do vendedor ja cadastrado")
                return
            else:
                vquery = f'INSERT INTO tb_vendedor VALUES("{numero}","{nome}");'
                dml(vquery)
                messagebox.showinfo("Concluido", 'Vendedor cadastrado com sucesso')
                self.E_numero.delete(0,END)
                self.E_vendedor.delete(0,END)
                self.E_numero.focus_set()


    def __init__(self, tela, Boleano, argumento):
        cls(tela)
        self.lb_titulo = Label(tela, text= 'Cadastrar Novo vendedor')
        self.lb_numero = Label(tela, text= 'N° do vendedor: ')
        self.lb_Vendedor = Label(tela, text= 'Nome do Vendedor: ')

        self.E_numero = Entry(tela)
        self.E_vendedor = Entry(tela)

        self.btn = Button(tela, text='Salvar', command=lambda: self.bc_vendedor(Boleano,argumento[0]))

        if Boleano:
            self.E_numero.insert(END,argumento[0])
            self.E_vendedor.insert(END,argumento[1])

        self.lb_titulo.grid(column = 0, row = 0, columnspan=2)

        self.lb_numero.grid(column=0, row=1, pady=10, sticky='e')
        self.E_numero.grid(column=1, row=1,columnspan=2, pady=10)

        self.lb_Vendedor.grid(column=0, row=2, pady=10, sticky='e')
        self.E_vendedor.grid(column=1, row=2, columnspan=2, pady=10)

        self.btn.grid(column=2, row=3, sticky='e')