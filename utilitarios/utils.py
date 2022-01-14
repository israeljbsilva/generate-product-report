def remover_caracteres_e_transformar_inteiro(preco):
    preco_formatado = int(preco.replace('.', '').replace(',', ''))
    return preco_formatado
