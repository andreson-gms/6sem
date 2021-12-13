from tkinter import *
from tkinter import messagebox
from modulos.banco import dml
from modulos.Form_cliente import Cadastra_cliente


class Edita_C(Cadastra_cliente):

    def bc_cliente(self):
        try:
            numero = self.et_numero.get()
            nome = self.et_cliente.get().title()
            cidade = self.et_cidade.get().upper()
            vquery = f"UPDATE `tb_Clientes` SET `cod_cliente`='{numero}',`cliente`='{nome}',`cidade`='{cidade}' WHERE `cod_cliente`='{self.id}'"
            dml(vquery)
        except Exception as ex:
            messagebox.showerror('ERROR!!', ex)
        finally:
            messagebox.showinfo("Concluido", 'Vendedor alterado com sucesso')
            from modulos import Lista_cliente as lc
            lista = lc.L_cliente(self.win)


    def __init__(self, tela, *dados):
        self.win = tela
        self.id = dados[0]
        super().__init__(tela)
        self.et_numero.insert(END,dados[0])      
        self.et_cliente.insert(END,dados[1])
        self.et_cidade.insert(END,dados[2])