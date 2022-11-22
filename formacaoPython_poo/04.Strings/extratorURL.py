class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizarUrl(url)
        self.validarUrl()

    def sanitizarUrl(self, url):
        if type(self.url) == str:
            return url.strip()
        else:
            return ''

    def validarUrl(self):
        if not self.url:
            raise ValueError('A URL está vazia')

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


extratorUrl = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')

valorQuantidade = extratorUrl.getValorParametros('quantidade')
print(valorQuantidade)