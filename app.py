import requests
import json
import pandas as pd

'''"[{"key":"chave-api-dados","value":"1b15c5e21b0a77d753cdca5570bffa24"}]
nomedoAutor' : 'value1', 'localidadeDoGasto' : 'value2', 'tipoEmenda':'value3', 'valorEmpenhado':'value4', 'valorPago':'value5'

'''

headers = {"chave-api-dados":"1b15c5e21b0a77d753cdca5570bffa24"}
payload = {'key1':'value1'}
apiURL = "https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2020&pagina=1" 
response_API = requests.get(apiURL, params=payload, headers=headers)
print(response_API.status_code)

printable1 = response_API.json()
printable2 = response_API.text
printable3 = json.dumps(response_API.json(), sort_keys=True, indent=4)

df = pd.read_json(printable3)

nomeAutor = df['nomeAutor']


nomeAutor_valorPago = df[['nomeAutor','valorPago']].shape
print(nomeAutor_valorPago)

valorPago_1000 = df[df['valorPago'] > 1000]
print(valorPago_1000)






