class ArquivoEntrada:

    def __init__(self):
        self.cabecalho = None
        self.produtos = []


class Cabecalho:

    def __init__(self):
        self.identificador = 'H'
        self.titulo = None
        self.data = None


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
