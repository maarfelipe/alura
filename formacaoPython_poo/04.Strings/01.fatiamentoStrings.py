url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# sanitização e validação da URL
if url == ''.strip():
    raise ValueError('A URL está vazia')

# varre a URL até o valor em .find
indiceInterrogacao = url.find('?')
# guarda na variável urlBase o valor do início da string até o índice informado
urlBase = url[:indiceInterrogacao]
# parte do índice informado até o final da string e guarda o conteúdo na variável urlParametros
urlParametros = url[indiceInterrogacao+1:]

# a string informada é guardada na variável parametroBusca
parametroBusca = 'quantidade'
# busca o parâmetro informado acima dentro da parte de parâmetros da URL
indiceParametro = urlParametros.find(parametroBusca)
# ao encontrar o parâmetro informado, soma seu length + 1 para guardar o valor do parâmetro da URL
indiceValor = indiceParametro + len(parametroBusca) + 1

# na parte de parâmetros da URL, .find busca a partir do indiceValor um &
eComercial = urlParametros.find('&', indiceValor)
# se não encontrar o &
if eComercial == -1:
    # a variável recebe o valor do parâmetro até o final da string (quer dizer que é está no final da string)
    valor = urlParametros[indiceValor:]
else:
    # se encontrar o & a variável salva o valor do parâmetro até o & (o valor da busca está no meio da string)
    valor = urlParametros[indiceValor:eComercial]
print(valor)
