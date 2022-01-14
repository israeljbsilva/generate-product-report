from jinja2 import Template

from jinja2 import Template
t = Template("Hello {{ something }}!")
t.render(something="World")

arquivo_template = open("templates/template.html", "r")
template_texto = arquivo_template.read()
arquivo_template.close()

template = Template(template_texto)
temploate_texto_pronto = template.render(titulo='Teste', data='30/12/2021')


arquivo_saida = open("templates/template_pronto.html", "w")
arquivo_saida.write(temploate_texto_pronto)
