from tkinter import *
from tkinter import messagebox
from modulos.banco import dml
from modulos.Form_vendedor import Cadastra_vendedor

class Ediat_v(Cadastra_vendedor):

    def bc_vendedor(self):
        try:
            numero = self.E_numero.get()
            nome = self.E_vendedor.get()
            vquery = f"UPDATE `tb_vendedor` SET `cod_vendedor`='{numero}',`vendedor`='{nome}' WHERE `cod_vendedor`='{self.id}'"
            dml(vquery)
        except Exception as ex:
            messagebox.showerror("ERRO!", ex)
        finally:
            messagebox.showinfo("Concluido", 'Vendedor alterado com sucesso')
            from modulos import Lista_vendedor as lv
            lista = lv.L_vendedor(self.win)


    def __init__(self,tela,*dados):
        self.win = tela
        self.id = dados[0]
        super().__init__(tela)
        self.E_numero.insert(0,dados[0])
        self.E_vendedor.insert(0,dados[1])