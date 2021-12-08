from tkinter import *
from tkinter import ttk
from modulos.banco import dql
from modulos import cls

class L_pedido():
    def buscar(self):
        lista = []
        vquery = 'SELECT * FROM tb_pedidos ORDER BY RAND () LIMIT 50'
        lista = dql(vquery)
        for (dt, nf, catp, grop, c, v, qt, vt) in lista:
            self.tv.insert("","end", values=(dt, nf, catp, grop, c, v, qt, vt))

    def Pesquisar(self):
        lista = []
        pes = self.et_pes.get()
        op = self.op_select.get()
        if op == 'Data':
            vquery = f"SELECT * FROM tb_pedidos WHERE data LIKE '%{pes}%' ORDER BY RAND () LIMIT 50"
        elif op =='NF':
            vquery = f"SELECT * FROM tb_pedidos WHERE nf LIKE '%{pes}%'"
        elif op == 'Categoria':
            vquery = f"SELECT * FROM tb_pedidos WHERE categoria_produto LIKE '%{pes}%' ORDER BY RAND () LIMIT 50"
        elif op == 'Grupo':
            vquery = f"SELECT * FROM tb_pedidos WHERE grupo_produto LIKE '%{pes}%' ORDER BY RAND () LIMIT 50"
        elif op == 'Cliente':
            vquery = f"SELECT * FROM tb_pedidos WHERE cliente LIKE '%{pes}%' ORDER BY RAND () LIMIT 50"
        elif op == 'Vendedor':
            vquery = f"SELECT * FROM tb_pedidos WHERE vendedor LIKE '%{pes}%' ORDER BY RAND () LIMIT 50"
        self.tv.delete(*self.tv.get_children())
        lista = dql(vquery)
        for (dt, nf, catp, grop, c, v, qt, vt) in lista:
            self.tv.insert("","end", values=(dt, nf, catp, grop, c, v, qt, vt))

    
    def __init__(self, tela):
        cls(tela)
        self.tv = ttk.Treeview(tela, columns= ('dt', 'nf', 'catp', 'grop', 'c', 'v', 'qt', 'vt'), show='headings', height=26)
        self.tv.column('dt', minwidth=0, width=90)
        self.tv.column('nf', minwidth=0, width=80)
        self.tv.column('catp', minwidth=0, width=100)
        self.tv.column('grop', minwidth=0, width=100)
        self.tv.column('c', minwidth=0, width=90)
        self.tv.column('v', minwidth=0, width=90)
        self.tv.column('qt', minwidth=0, width=90)
        self.tv.column('vt', minwidth=0, width=90)
        
        
        self.tv.heading('dt', text='Data')
        self.tv.heading('nf', text='Nota Fiscal')
        self.tv.heading('catp', text='Categoria Produto')
        self.tv.heading('grop', text='Grupo Produto')
        self.tv.heading('c', text='Cliente')
        self.tv.heading('v', text='Vendedor')
        self.tv.heading('qt', text='Qantidade')
        self.tv.heading('vt', text='Valor Total')
        
        self.listaNomes = self.buscar()

        list_op = ['Data', 'NF', 'Categoria', 'Grupo', 'Cliente', 'Vendedor']
        self.op_select = StringVar()
        self.lb_pes = Label(tela, text='Pesquisar',)
        self.op_pes = OptionMenu(tela,self.op_select ,*list_op)
        self.op_pes.configure(width=20)
        self.et_pes = Entry(tela, width=50)
        self.btn_pes = Button(tela,command=self.Pesquisar, text='Buscar')
        

        self.lb_pes.grid(column=0, row=0, pady=10, sticky='e')
        self.op_pes.grid(column=1, row=0)
        self.et_pes.grid(column=2,row=0, pady=10)
        self.btn_pes.grid(column=3,row=0, pady=10, sticky='w')
        
        self.tv.grid(column=0, row=1, columnspan=5)
