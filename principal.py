import logging
import os
import traceback

from modelo.arquivo_entrada_csv import ArquivoEntrada
from tradutor.relatorio_html import renderizar_template, escrever_relatorio_html
from utilitarios.utils import buscar_argumentos


if __name__ == '__main__':
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler("processo.log"),
                logging.StreamHandler()
            ]
        )

        argumentos = buscar_argumentos()
        nome_arquivo_entrada = argumentos.entrada
        nome_arquivo_saida = argumentos.saida

        logging.info(f'Iniciando leitura do arquivo: {nome_arquivo_entrada}...')
        objeto_arquivo_entrada = ArquivoEntrada()
        objeto_arquivo_entrada.construir_arquivo_entrada(nome_arquivo_entrada)

        logging.info('Iniciando renderização com os dados do arquivo .csv...')
        template_texto_pronto = renderizar_template(objeto_arquivo_entrada)

        logging.info(f'Iniciando escrita do template {os.path.basename(nome_arquivo_saida)} de saída...')
        escrever_relatorio_html(nome_arquivo_saida, template_texto_pronto)

    except Exception as erro:
        logging.error(erro)
        logging.error(f'[principal.py] {traceback.format_exc()}')
