from modelos.valor import Valor

class Roupas:
    roupas = []

    def __init__(self, nome, tipo, tamanho, local):
        self._nome = nome.upper()
        self._tipo = tipo.title()
        self._tamanho = tamanho
        self._local = local.title()
        self._estoque = False
        self._valor = []
        Roupas.roupas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._tipo} | {self._tamanho} | {self._local} | {self._estoque}'

    @classmethod
    def listar_roupas(cls):
        print('''

██╗░░░██╗░█████╗░██╗░░░██╗░██████╗░██╗░░░░░░█████╗░
██║░░░██║██╔══██╗██║░░░██║██╔════╝░██║░░░░░██╔══██╗
╚██╗░██╔╝██║░░██║██║░░░██║██║░░██╗░██║░░░░░███████║
░╚████╔╝░██║░░██║██║░░░██║██║░░╚██╗██║░░░░░██╔══██║
░░╚██╔╝░░╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
░░░╚═╝░░░░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝

██╗░░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░███████╗██████╗░
██║░░░██║██╔══██╗██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔══██╗
╚██╗░██╔╝███████║██████╦╝██║░░░██║██║░░██║█████╗░░██████╦╝
░╚████╔╝░██╔══██║██╔══██╗██║░░░██║██║░░██║██╔══╝░░██╔══██╗
░░╚██╔╝░░██║░░██║██████╦╝╚██████╔╝██████╔╝███████╗██████╦╝
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═════╝░╚══════╝╚═════╝░
        ''')

        print(f'{"Nome da peça".ljust(20)} | {"Tipo".ljust(20)} | {"Tamanho".ljust(20)} | {"Local".ljust(20)} | {"Estoque".ljust(20)}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for roupa in cls.roupas:
            print(f'{roupa._nome.ljust(20)} | {roupa._tipo.ljust(20)} | {roupa._tamanho.ljust(20)} | {roupa._local.ljust(20)} | {roupa.estoque.ljust(20)} | {roupa.media_preço}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def estoque(self):
        return '❌ fora de estoque' if self._estoque else '✔️ em estoque'

    def alterar_estado(self):
        self._estoque = not self._estoque        

    def receber_preço(self, loja, preço):
        preço = Valor(loja, preço)
        self._valor.append(preço)

    @property
    def media_preço(self):
        if not self._valor:
            return 0 
        somas_dos_preços = sum(valor._preço for valor in self._valor)
        quantidade_lojas = len(self._valor)
        media = round(somas_dos_preços/quantidade_lojas, 1)
        return media
