def cls(tela):#limpa o frame da tela
    for items in tela.winfo_children():
        items.destroy()


def t_home(tela):
    try:
        from modulos.home import h_home
    except Exception as ex:
        print(f'ERROR: {ex}')
    else:
        h = h_home(tela)

#==============================      CLIENTE  =========================================================
def t_cliente(tela, edt=False, *args):#frame para novo cliente
    try:
        from modulos.C_cliente import C_cliente
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        c = C_cliente(tela, edt, args)


def c_cliente(tela):
    try:
        from modulos.L_cliente import L_cliente
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        v = L_cliente(tela)
    



#============================    PEDIDOS       =====================================================

def t_pedido(tela):#frame para novo pedido
    
    try:
        from modulos.C_pedido import C_pedido
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        p = C_pedido(tela)


def c_pedido(tela):
    
    try:
        from modulos.L_pedido import L_pedido
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        v = L_pedido(tela)






#======================================  VENDEDOR   ====================================================

def t_vendedor(tela, edt=False, *args):#inicia a janela de cadastro para novo vendedor
    
    try:
        from modulos.C_vendedor import C_vendedor
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        v = C_vendedor(tela, edt, args)


def c_vendedor(tela):#inicia a janela de listagen de vendedores
    
    try:
        from modulos.L_vendedor import L_vendedor
    except Exception as ex:
        print(f'ERRO:   {ex}')
    else:
        v = L_vendedor(tela)

def t_sobre():
    try:
        from modulos.sobre import s_cobre
    except Exception as ex:
        print(f'ERROR: {ex}')
    else:
        s = s_cobre()