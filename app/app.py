from tkinter import *

def home():
    from modulos import home
    h = home.TelaHome(tela)

def Novo_cliente():
    from modulos import Form_cliente as fc
    novo = fc.Cadastra_cliente(tela)

def clientes():
    from modulos import Lista_cliente as lc
    lista = lc.L_cliente(tela)

def Novo_pedido():
    from modulos import Form_pedido as fp
    novo = fp.Cadastra_pedido(tela)

def pedidos():
    from modulos import Lista_pedido as lp
    lista = lp.L_pedido(tela)

def Novo_vendedor():
    from modulos import Form_vendedor as fv
    Novo = fv.Cadastra_vendedor(tela)

def vendedor():
    from modulos import Lista_vendedor as lv
    lista = lv.L_vendedor(tela)

def sobre():
    from modulos import sobre
    s = sobre.web_sobre()

#=========define tamanho da janela===========

xis = 1024
ipsilom = 720
geometria = str(xis + 2) + 'x' + str(ipsilom + 2)
#-----------------------------------------------------


#========Cria a janela principal=================
app = Tk()
app.title('6sem')
app.geometry(geometria)
#-----------------------------------------------------


#========Define componentes da barra de menus============
menuBar = Menu(app)


#-------home------------
Home = Menu(menuBar, tearoff=0)
Home.add_command(label='Home', command=home)


#-------Cliente----------
Cliente = Menu(menuBar, tearoff=0)
Cliente.add_command(label='Cliente', command=clientes)
Cliente.add_command(label='Novo Cliente', command=Novo_cliente)


#-------Pedido----------
Pedido = Menu(menuBar, tearoff=0)
Pedido.add_command(label='Pedido', command=pedidos)
Pedido.add_command(label='Novo Pedido', command=Novo_pedido)


#-------Vendedor---------
Vendedor = Menu(menuBar, tearoff=0)
Vendedor.add_command(label='Vendedor', command=vendedor)
Vendedor.add_command(label='Novo Vendedor', command=Novo_vendedor)


#------Sobre---------
Sobre = Menu(menuBar, tearoff=0)
Sobre.add_command(label='Sobre', command=sobre)


#------Adiciona os botoes-
menuBar.add_cascade(label= 'Home', menu=Home)
menuBar.add_cascade(label= 'Clientes', menu=Cliente)
menuBar.add_cascade(label='Pedidos', menu=Pedido)
menuBar.add_cascade(label='Vendedores', menu=Vendedor)
menuBar.add_cascade(label= 'Sobre', menu=Sobre)

app.config(menu = menuBar)


#=========Define a tela auxiliar============
tela =Frame(app, borderwidth=1,relief='solid')
tela.place(x=1,y = 1,width=xis,height=ipsilom)


#=====carrega a pagina inicial=====
home()


#======roda o Progama
app.mainloop()