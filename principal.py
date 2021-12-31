from jinja2 import Template

from modelo.arquivo_entrada import ArquivoEntrada


# lendo o arquivo de entrada e colocando em objeto
objeto_arquivo_entrada = ArquivoEntrada()
objeto_arquivo_entrada.construir_arquivo_entrada()

# traducao desse arquivo de entrada para o template (.html)
arquivo_template = open("templates/template.html", "r")
template_texto = arquivo_template.read()
arquivo_template.close()

template = Template(template_texto)
temploate_texto_pronto = template.render(cabecalho=objeto_arquivo_entrada.cabecalho, produtos=objeto_arquivo_entrada.produtos)

# escrever um arquivo de saida
arquivo_saida = open("templates/template_pronto.html", "w")
arquivo_saida.write(temploate_texto_pronto)
