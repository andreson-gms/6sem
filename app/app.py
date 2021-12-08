from tkinter import *
import modulos as md

def home():
    md.t_home(tela)

def c_clientes():
    md.t_cliente(tela)

def clientes():
    md.c_cliente(tela)

def c_pedidos():
    md.t_pedido(tela)

def pedidos():
    md.c_pedido(tela)

def c_vendedor():
    md.t_vendedor(tela)

def vendedor():
    md.c_vendedor(tela)

def sobre():
    md.t_sobre()

xis = 1024
ipsilom = 720
geometria = str(xis + 2) + 'x' + str(ipsilom + 2)

app = Tk()
app.title('6sem')
app.geometry(geometria)


menuBar = Menu(app)
Home = Menu(menuBar, tearoff=0)
Home.add_command(label='Home', command=home)

Cliente = Menu(menuBar, tearoff=0)
Cliente.add_command(label='Cliente', command=clientes)
Cliente.add_command(label='Novo Cliente', command=c_clientes)

Pedido = Menu(menuBar, tearoff=0)
Pedido.add_command(label='Pedido', command=pedidos)
Pedido.add_command(label='Novo Pedido', command=c_pedidos)

Vendedor = Menu(menuBar, tearoff=0)
Vendedor.add_command(label='Vendedor', command=vendedor)
Vendedor.add_command(label='Novo Vendedor', command=c_vendedor)

Sobre = Menu(menuBar, tearoff=0)
Sobre.add_command(label='Sobre', command=sobre)

menuBar.add_cascade(label= 'Home', menu=Home)
menuBar.add_cascade(label= 'Clientes', menu=Cliente)
menuBar.add_cascade(label='Pedidos', menu=Pedido)
menuBar.add_cascade(label='Vendedores', menu=Vendedor)
menuBar.add_cascade(label= 'Sobre', menu=Sobre)

app.config(menu = menuBar)

tela =Frame(app, borderwidth=1,relief='solid')
tela.place(x=1,y = 1,width=xis,height=ipsilom)

home()

app.mainloop()