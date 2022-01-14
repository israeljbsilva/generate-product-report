class ArquivoEntrada:

    def __init__(self):
        self.cabecalho = None
        self.produtos = []

    @staticmethod
    def ler_arquivo_de_entrada():  # criar sem o with no primeiro momento
        with open("arquivo-entrada-produtos.csv", "r") as arquivo_entrada:
            linhas_arquivo = arquivo_entrada.readlines()
        return linhas_arquivo

    def construir_arquivo_entrada(self):
        linhas_arquivo = self.ler_arquivo_de_entrada()
        for linha in linhas_arquivo:
            linhas_separadas = linha.split(';')

            if linhas_separadas[0] == 'H':
                objeto_cabecalho = Cabecalho()
                objeto_cabecalho.construir_cabecalho(linhas_separadas)
                self.cabecalho = objeto_cabecalho

            elif linhas_separadas[0] == 'P':
                objeto_produto = Produto()
                objeto_produto.construir_produto(linhas_separadas)
                self.produtos.append(objeto_produto)


class Cabecalho:

    def __init__(self):
        self.identificador = 'H'
        self.titulo = None
        self.data = None

    def construir_cabecalho(self, linhas_separadas):
        self.titulo = linhas_separadas[1]
        self.data = linhas_separadas[2]


class Produto:

    def __init__(self):
        self.identificador = 'P'
        self.nome = None
        self.marca = None
        self.tamanho_tela = None
        self.cor = None
        self.processador = None
        self.memoria_ram = None
        self.espaco_interno = None
        self.preco = None
        self.data_lancamento = None
        self.url_imagem = None

    def construir_produto(self, linhas_separadas):
        self.nome = linhas_separadas[1]
        self.marca = linhas_separadas[2]
        self.tamanho_tela = linhas_separadas[3]
        self.cor = linhas_separadas[4]
        self.processador = linhas_separadas[5]
        self.memoria_ram = linhas_separadas[6]
        self.espaco_interno = linhas_separadas[7]
        self.preco = linhas_separadas[8]
        self.data_lancamento = linhas_separadas[9]
        self.url_imagem = linhas_separadas[10]
