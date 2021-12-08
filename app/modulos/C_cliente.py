#modulo frame do cadastro de novo cliente
from tkinter import *
from tkinter import messagebox
from modulos.banco import dml
from modulos.banco import dql
from modulos import cls

class C_cliente():
    def bc_cliente(self,bole,confirma):
        lista = []
        numero = self.et_numero.get()
        nome = self.et_cliente.get().title()
        uf = self.vuf.get()
        cidade = self.et_cidade.get().upper()

        if bole:
            vquery = f"UPDATE `tb_Clientes` SET `cod_cliente`='{numero}',`cliente`='{nome}',`cidade`='{cidade}' WHERE `cod_cliente`='{confirma}'"
            dml(vquery)
            messagebox.showinfo("Concluido", 'Vendedor alterado com sucesso')
        else:
            vquery = f"SELECT cod_cliente FROM tb_Clientes WHERE cod_cliente LIKE '{numero}'"
            lista = dql(vquery)
            if lista != []:
                messagebox.showwarning("atencao", "Codigo de cliente informadao ja existe")
                return
            else:
                try:
                    vquery = f"SELECT `cidade` FROM tb_cidade WHERE cidade LIKE '%{cidade}%' AND uf='{uf}'"
                    lista = dql(vquery)
                    if lista != []:
                        l = lista[0][0]
                        vquery = f"INSERT INTO `tb_Clientes`(`cod_cliente`, `cliente`, `cidade`) VALUES ('{numero}','{nome}','{l}')"
                        dml(vquery)
                    else:
                        vquery = f"INSERT INTO `tb_cidade`(`cidade`, `uf`) VALUES ('{cidade}','{uf}')"
                        dml(vquery)
                        vquery = f"INSERT INTO `tb_Clientes`(`cod_cliente`, `cliente`, `cidade`) VALUES ('{numero}','{nome}','{cidade}')"
                        dml(vquery)
                except Exception as ex:
                    messagebox.showerror('erro', ex)
                else:
                    messagebox.showinfo("Concluido", 'Cliente cadastrado com sucesso')
                    self.et_numero.delete(0,END)
                    self.et_cliente.delete(0,END)
                    self.et_cidade.delete(0,END)
                    self.et_numero.focus_set()   

    def busca_r(self):
        lista = []
        vquery = "SELECT regiao FROM tb_regiao;"
        resposta =  dql(vquery)
        for item in resposta:
            for f in item:
                lista.append(f)
        return lista

    def busca_uf(self):
        regiao = self.vregiao.get()
        lista = []
        vquery = f"SELECT uf FROM tb_uf WHERE regiao = '{regiao}';"
        resposta =  dql(vquery)
        for item in resposta:
            for f in item:
                lista.append(f)
        return lista

    def call_back(self, *args):
        lista = self.busca_uf()
        self.vuf.set(lista[0])

        menu = self.op_uf['menu']
        menu.delete(0, 'end')

        for it in lista:
            menu.add_command(label=it, command=lambda op=it: self.vuf.set(op))

    def __init__(self, tela, Boleano, argumento):
        cls(tela)
        #====== Labels =======================
        self.lb_titulo = Label(tela, text= 'Novo cliente')
        self.lb_numero = Label(tela, text= 'N° do cliente: ')
        self.lb_cliente = Label(tela, text= 'Nome do cliente: ')
        self.lb_regiao = Label(tela, text= 'Regiao: ')
        self.lb_uf = Label(tela, text= 'UF: ')
        self.lb_cidade = Label(tela, text= 'Cidade: ')

        #========= Entrys==========================
        self.et_numero = Entry(tela)      
        self.et_cliente = Entry(tela)
        self.et_cidade = Entry(tela, width=60)

        
        self.regiao = self.busca_r()

        self.vregiao = StringVar()
        self.vuf = StringVar()
        

        self.op_regiao = OptionMenu(tela, self.vregiao, *self.regiao)
        
        self.vregiao.trace('w', self.call_back)      
        
        self.op_uf = OptionMenu(tela, self.vuf,'')


        self.btn = Button(tela, text='Salvar', command=lambda: self.bc_cliente(Boleano,argumento[0]))

        if Boleano:
            self.et_numero.insert(END,argumento[0])      
            self.et_cliente.insert(END,argumento[1])
            self.et_cidade.insert(END,argumento[2])


        #======coloca na tela=========================
        self.lb_titulo.grid(column = 0, row = 0, columnspan=4)

        self.lb_numero.grid(column=0, row=1, pady=10, sticky='e')
        self.et_numero.grid(column=1, row=1,pady=10)

        self.lb_cliente.grid(column=2, row=1, pady=10, sticky='e')
        self.et_cliente.grid(column=3, row=1,pady=10)

        self.lb_uf.grid(row=2, column=2, pady=10, sticky='e')
        self.op_uf.grid(row=2, column=3, pady=10)

        self.lb_regiao.grid(row=2, column=0, pady=10, sticky='e')
        self.op_regiao.grid(row=2, column=1, pady=10)
        
        self.lb_cidade.grid(row=3, column=0, pady=10, sticky='e')
        self.et_cidade.grid(row=3, column=1, pady=10, columnspan=3)

        self.btn.grid(column=3, row=4, sticky='e', pady=10)
        
        
