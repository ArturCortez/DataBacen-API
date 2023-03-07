import requests
import json
import pandas as pd


headers = {"chave-api-dados":"1b15c5e21b0a77d753cdca5570bffa24"}
payload = {'key1':'value1'}
apiURL = "https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2020&pagina=1" 
response_API = requests.get(apiURL, headers=headers, timeout=0.001)
print(response_API.status_code)