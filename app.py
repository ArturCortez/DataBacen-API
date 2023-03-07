import requests
import json
import pandas as pd
import helper

#"[{"key":"chave-api-dados","value":"1b15c5e21b0a77d753cdca5570bffa24"}]
#nomedoAutor' : 'value1', 'localidadeDoGasto' : 'value2', 'tipoEmenda':'value3', 'valorEmpenhado':'value4', 'valorPago':'value5'


for x in range(5, 10):
    first_response = helper.requestAPI(x)
    print(first_response.status_code)
    response_json = first_response.json()
    csv_file = json.dumps(response_json, sort_keys=True, indent=4)
    df = pd.read_json(csv_file)
    df.to_csv(r'./CSV/csv_file.csv', mode='a')











    




