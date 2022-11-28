import re

url = 'https://www.bytebank.com.br/cambio'

padraoURL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padraoURL.match(url)

if not match:
    raise ValueError('A URL não é válida.')

print('A URL é válida')
