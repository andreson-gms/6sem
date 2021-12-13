from tkinter import *
from tkinter import ttk
from modulos.banco import dql


class L_cliente():
    def cls(self,tela):#limpa o frame da tela
        for items in tela.winfo_children():
            items.destroy()

    def R_lista(self):
        lista = []
        try:
            vquery = 'SELECT * FROM tb_Clientes LIMIT 50'
            lista = dql(vquery)
            for (cod, nome, cidade) in lista:
                if cidade == "0":
                    self.tv.insert("","end", values=(cod, nome, "EXTERIOR (FORA DO BRASIL)"))
                else:
                    self.tv.insert("","end", values=(cod, nome, cidade))
        finally:
            return


    def Pesquisar(self):
        lista = []
        pes = self.et_pes.get()
        try:
            vquery = f"SELECT * FROM tb_Clientes WHERE cod_cliente LIKE '%{pes}%' OR cliente LIKE '%{pes}%'"
            lista = dql(vquery)
            self.tv.delete(*self.tv.get_children())
            for (cod, nome, cidade) in lista:
                if cidade == "0":
                    self.tv.insert("","end", values=(cod, nome, "EXTERIOR (FORA DO BRASIL)"))
                else:
                    self.tv.insert("","end", values=(cod, nome, cidade))
        finally:
            return
    
    def Editar(self, tela):
        try:
            itemSelecionado = self.tv.selection()[0]
            valores = self.tv.item(itemSelecionado, "values")
            from modulos.Editar_Cliente import Edita_C
            novo = Edita_C(tela, *valores)
    
        except Exception as ex:
            print(ex)
        finally:
            pass


    def __init__(self, tela):
        
        self.cls(tela)
        self.tv = ttk.Treeview(tela, columns= ('cod', 'nome', 'cidade'), show='headings', height=26)
        self.tv.column('cod', minwidth=0, width=90)
        self.tv.column('nome', minwidth=0, width=250)
        self.tv.column('cidade', minwidth=0, width=250)
        

        self.tv.heading('cod', text='Cod cliente')
        self.tv.heading('nome', text='Cliente')
        self.tv.heading('cidade', text='cidade')
        
        self.listaNomes = self.R_lista()

        self.lb_pes = Label(tela, text='Pesquisar', width=20)
        self.et_pes = Entry(tela, width=56)
        self.btn_pes = Button(tela,command=self.Pesquisar, text='Buscar', width=15)
        self.btn_edit = Button(tela,command=lambda tl=tela: self.Editar(tl), text='Editar', width=5)

        self.lb_pes.grid(column=0, row=0, pady=10)
        self.et_pes.grid(column=1,row=0, sticky='w')
        self.btn_pes.grid(column=2,row=0, sticky='w')
        self.btn_edit.grid(column=3,row=0, sticky='e')
        self.tv.grid(column=1, row=1, columnspan=3, sticky='w')

        
