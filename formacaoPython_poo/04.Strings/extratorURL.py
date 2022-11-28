import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizarUrl(url)
        self.validarUrl()

    def sanitizarUrl(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validarUrl(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padraoURL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padraoURL.match(self.url)
        if not match:
            raise ValueError('A URL não é válida.')

    def getUrlBase(self):
        indiceInterrogacao = self.url.find('?')
        urlBase = self.url[:indiceInterrogacao]
        return urlBase

    def getUrlParametros(self):
        indiceInterrogacao = self.url.find('?')
        urlParametros = self.url[indiceInterrogacao + 1:]
        return urlParametros

    def getValorParametros(self, parametroBusca):
        indiceParametro = self.getUrlParametros().find(parametroBusca)
        indiceValor = indiceParametro + len(parametroBusca) + 1
        eComercial = self.getUrlParametros().find('&', indiceValor)
        if eComercial == -1:
            valor = self.getUrlParametros()[indiceValor:]
        else:
            valor = self.getUrlParametros()[indiceValor:eComercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}\n' \
               f'Parâmetros: {self.getUrlParametros()}\n' \
               f'URL Base: {self.getUrlBase()}'

    def __eq__(self, other):
        return self.url == other.url


extratorUrl = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
print(f'O tamanho da URL é {len(extratorUrl)}')

# valorQuantidade = extratorUrl.getValorParametros('quantidade')
# print(valorQuantidade)