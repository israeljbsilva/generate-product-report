import argparse


def remover_caracteres_e_transformar_inteiro(produto):
    if produto.preco == '':
        raise ValueError(f'O produto {produto.nome} está sem preço')
    preco_formatado = int(produto.preco.replace('.', '').replace(',', ''))
    return preco_formatado


def buscar_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--entrada", help="Nome do arquivo de entrada .csv", required=True)
    parser.add_argument('-s', '--saida', help='Nome do arquivo de saída', required=True)
    argumentos = parser.parse_args()
    return argumentos
