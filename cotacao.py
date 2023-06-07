import requests

requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_a = requisicao.json()
cotacao_dolar = requisicao_a ["USDBRL"] ["bid"]
cotacao_euro = requisicao_a["EURBRL"] ["bid"]
cotacao_btc = requisicao_a["BTCBRL"] ["bid"]

print(cotacao_dolar)
print(cotacao_euro)
print(cotacao_btc)
