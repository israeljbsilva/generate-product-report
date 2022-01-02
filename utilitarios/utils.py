def remover_caracteres_e_transformar_inteiro(produto):
    preco_formatado = int(produto.preco.replace('.', '').replace(',', ''))
    return preco_formatado
