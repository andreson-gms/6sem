import csv, sys
nome_ficheiro = '/home/ticonnecting/Documentos/GitHub/6sem/app/arquivos/Pedidos.csv'
with open(nome_ficheiro, 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    # reader.__next__()
    try:
        for linha in reader:
            print(linha)
    except csv.Error as e:
        sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))