from tkinter import *
from tkinter import ttk
from modulos.banco import dql


class L_vendedor():
    def cls(self,tela):#limpa o frame da tela
        for items in tela.winfo_children():
            items.destroy()

    def R_lista(self):
        lista = []
        try:
            vquery = 'SELECT * FROM tb_vendedor'
            lista = dql(vquery)
            for (id, nome) in lista:
                self.tv.insert("","end", values=(id, nome))
        finally:
            return

    def Pesquisar(self):
        lista = []
        pes = self.et_pes.get()
        vquery = f"SELECT * FROM tb_vendedor WHERE cod_vendedor LIKE '%{pes}%' OR vendedor LIKE '%{pes}%'"
        lista = dql(vquery)
        self.tv.delete(*self.tv.get_children())
        for (id, nome) in lista:
            self.tv.insert("","end", values=(id, nome))
    
    def Editar(self,tela):
        try:
            itemSelecionado = self.tv.selection()[0]
            valores = self.tv.item(itemSelecionado, "values")
            from modulos.Editar_vendedor import Ediat_v
            novo = Ediat_v(tela, *valores)
    
        except Exception as ex:
            print(ex)
        finally:
            pass

    def __init__(self, tela):
        self.cls(tela)
        

        self.tv = ttk.Treeview(tela, columns= ('id', 'nome'), show='headings', height=26)
        self.tv.column('id', minwidth=0, width=90)
        self.tv.column('nome', minwidth=0, width=250)
        
        self.tv.heading('id', text='Cod Vendedor')
        self.tv.heading('nome', text='Vendedor')

        self.listaNomes = self.R_lista()

        self.lb_pes = Label(tela, text='Pesquisar', width=20)
        self.et_pes = Entry(tela, width=56)
        self.btn_pes = Button(tela,command=self.Pesquisar, text='Buscar', width=10)
        self.btn_edit = Button(tela,command= lambda tl=tela: self.Editar(tl) , text='Editar', width=5)

        self.lb_pes.grid(column=0, row=0, pady=10)
        self.et_pes.grid(column=1,row=0, pady=10)
        self.btn_pes.grid(column=2,row=0, pady=10, padx=5)
        self.btn_edit.grid(column=2,row=1, sticky='nw', padx=5)
        self.tv.grid(column=1, row=1, columnspan=3, sticky='w')

        
