from tkinter import *
from modulos import cls





class h_home():
    def pre(self,tela):
        try:
            from modulos.copula.copula import copu
        except Exception as ex:
            print(ex)
        else:
            c = copu(tela)

    def __init__(self,tela):
        cls(tela)
        self.label = Label(tela, text='Bem Vindo', font=("Arial", 45)).pack()
        self.label2 = Label(tela, text='Primeira vez?', font=("Arial", 25)).pack()
        self.label3 = Label(tela, text='Clique no botao para inserir os dados iniciais no banco de dados').pack()
        self.btn_gera = Button(tela,command= lambda :self.pre(tela), text='Copular BD', font=("Arial", 15)).pack()
