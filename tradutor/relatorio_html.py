from jinja2 import Template


def ler_template():
    arquivo_template = open("templates/template.html", "r")
    template_texto = arquivo_template.read()
    arquivo_template.close()
    return template_texto


def renderizar_template(objeto_arquivo_entrada):
    template_texto = ler_template()
    media_preco = calcular_media_preco_produtos(objeto_arquivo_entrada.produtos)
    preco_mais_barato = calcular_preco_mais_barato(objeto_arquivo_entrada.produtos)
    preco_mais_caro = calcular_preco_mais_caro(objeto_arquivo_entrada.produtos)

    template = Template(template_texto)
    template_texto_pronto = template.render(cabecalho=objeto_arquivo_entrada.cabecalho,
                                            produtos=objeto_arquivo_entrada.produtos,
                                            total_produtos=len(objeto_arquivo_entrada.produtos),
                                            media=media_preco,
                                            mais_barato=preco_mais_barato,
                                            mais_caro=preco_mais_caro)
    return template_texto_pronto


def calcular_preco_mais_caro(produtos):
    precos = []
    for produto in produtos:
        precos.append(int(produto.preco.replace('.', '').replace(',', '')))

    preco_mais_caro = max(precos)
    return preco_mais_caro


def calcular_preco_mais_barato(produtos):
    precos = []
    for produto in produtos:
        precos.append(int(produto.preco.replace('.', '').replace(',', '')))

    preco_mais_barato = min(precos)
    return preco_mais_barato


def calcular_media_preco_produtos(produtos):
    total_preco = 0
    for produto in produtos:
        total_preco += int(produto.preco.replace('.', '').replace(',', ''))

    media = int(total_preco / len(produtos))

    return media


def escrever_relatorio_html(template_texto_pronto):
    arquivo_saida = open("templates/template_pronto.html", "w")
    arquivo_saida.write(template_texto_pronto)
