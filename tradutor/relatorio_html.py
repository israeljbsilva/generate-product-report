from jinja2 import Template


def ler_template():
    arquivo_template = open("templates/template.html", "r")
    template_texto = arquivo_template.read()
    arquivo_template.close()
    return template_texto


def renderizar_template(objeto_arquivo_entrada):
    template_texto = ler_template()

    template = Template(template_texto)
    template_texto_pronto = template.render(cabecalho=objeto_arquivo_entrada.cabecalho,
                                            produtos=objeto_arquivo_entrada.produtos)
    return template_texto_pronto


def escrever_relatorio_html(template_texto_pronto):
    arquivo_saida = open("templates/template_pronto.html", "w")
    arquivo_saida.write(template_texto_pronto)
