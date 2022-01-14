from jinja2 import Template

from utilitarios.utils import remover_caracteres_e_transformar_inteiro


def ler_template():
    with open("templates/template.html", "r") as arquivo_saida:
        template_texto = arquivo_saida.read()
        return template_texto


def renderizar_template(objeto_arquivo_entrada):
    template_texto = ler_template()
    todos_precos = criar_lista_com_precos_dos_produtos(objeto_arquivo_entrada.produtos)
    media_preco_por_marca = calcular_media_por_marca(objeto_arquivo_entrada.produtos)

    template = Template(template_texto)
    template_texto_pronto = template.render(cabecalho=objeto_arquivo_entrada.cabecalho,
                                            produtos=objeto_arquivo_entrada.produtos,
                                            total_produtos=len(objeto_arquivo_entrada.produtos),
                                            media_preco_por_marca=media_preco_por_marca,
                                            mais_barato=min(todos_precos),
                                            mais_caro=max(todos_precos))
    return template_texto_pronto


def criar_lista_com_precos_dos_produtos(produtos):
    precos = []
    for produto in produtos:
        preco_formatado = remover_caracteres_e_transformar_inteiro(produto.preco)
        precos.append(preco_formatado)

    return precos


def agrupar_precos_por_marca(produtos):
    precos_por_marca = {}

    for produto in produtos:
        preco_formatado = remover_caracteres_e_transformar_inteiro(produto.preco)
        if produto.marca not in precos_por_marca:
            precos_por_marca[produto.marca] = [preco_formatado]
        else:
            precos_por_marca[produto.marca].append(preco_formatado)

    return precos_por_marca


def calcular_media_por_marca(produtos):
    precos_por_marca = agrupar_precos_por_marca(produtos)
    media_por_marca = {}

    for marca, precos, in precos_por_marca.items():
        media_por_marca[marca] = int(sum(precos) / len(precos))

    return media_por_marca


def escrever_relatorio_html(template_texto_pronto):
    arquivo_saida = open("templates/template_pronto.html", "w")
    arquivo_saida.write(template_texto_pronto)
    arquivo_saida.close()
