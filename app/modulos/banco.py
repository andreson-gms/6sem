# este modulo realiza a conexao com o banco de dados
import mysql.connector as cnn
from mysql.connector import Error
from tkinter import messagebox

#import os

HOST = "localhost"
DBS = "appdb"
USER = "root"
PASS = "Cloud21!"


def conexaoDB():
    con=None
    try:
        con = cnn.connect(host = HOST,database = DBS, user = USER, password = PASS)
    except Error as ex:
        messagebox.showerror("!!ERROR!!", ex)
    return con


def dql(query):# SELECT
    vcon = conexaoDB()
    c = vcon.cursor()
    c.execute(query)
    res= c.fetchall()
    vcon.close()
    return res


def dml(query):#INSERT, UPDATE, DELETE
    try:
        vcon = conexaoDB()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)

# if __name__ == "__main__":
    
#     vquery = "INSERT INTO tb_vendedor (cod_vendedor, vendedor) VALUES ('00001', 'Andreson Gusmao');"
#     dml(vquery)

#     vquery = "SELECT * FROM tb_vendedor;"
#     resposta = dql(vquery)
#     for items in resposta:
#         print(items)