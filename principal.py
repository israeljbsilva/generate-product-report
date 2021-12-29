from modelo.arquivo_entrada import Cabecalho, Produto, ArquivoEntrada

arquivo_entrada = open("arquivo-entrada-produtos.csv", "r")
linhas_arquivo = arquivo_entrada.readlines()


objeto_arquivo_entrada = ArquivoEntrada()

for linha in linhas_arquivo:
    linhas_separadas = linha.split(';')

    if linhas_separadas[0] == 'H':
        objeto_cabecalho = Cabecalho()
        objeto_cabecalho.titulo = linhas_separadas[1]
        objeto_cabecalho.data = linhas_separadas[2]
        objeto_arquivo_entrada.cabecalho = objeto_cabecalho

    elif linhas_separadas[0] == 'P':
        objeto_produto = Produto()
        objeto_produto.nome = linhas_separadas[1]
        objeto_produto.marca = linhas_separadas[2]
        objeto_produto.tamanho_tela = linhas_separadas[3]
        objeto_produto.cor = linhas_separadas[4]
        objeto_produto.processador = linhas_separadas[5]
        objeto_produto.memoria_ram = linhas_separadas[6]
        objeto_produto.espaco_interno = linhas_separadas[7]
        objeto_produto.preco = linhas_separadas[8]
        objeto_produto.data_lancamento = linhas_separadas[9]
        objeto_produto.url_imagem = linhas_separadas[10]

        objeto_arquivo_entrada.produtos.append(objeto_produto)

arquivo_entrada.close()

print(objeto_arquivo_entrada)
