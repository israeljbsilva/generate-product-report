from modelo.arquivo_entrada_csv import ArquivoEntrada
from tradutor.relatorio_html import renderizar_template, escrever_relatorio_html


if __name__ == '__main__':
    objeto_arquivo_entrada = ArquivoEntrada()
    objeto_arquivo_entrada.construir_arquivo_entrada()

    template_texto_pronto = renderizar_template(objeto_arquivo_entrada)

    escrever_relatorio_html(template_texto_pronto)
