import re

url = 'bytebank.com/cambio'

padraoURL = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padraoURL.match(url)

if not match:
    raise ValueError('A URL não é válida.')

print('A URL é válida')
