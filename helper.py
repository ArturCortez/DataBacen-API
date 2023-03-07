import re
import requests

def ObjectToFloat(dataframe, column_name):
    dataframe[column_name] = dataframe[column_name].str.replace(".", "")
    dataframe[column_name] = dataframe[column_name].str.replace(",", ".")
    return dataframe[column_name]

def valToFloat(value):

#[,]{1}[\d]{2}
    x_match = re.sub("[.]*", "", value)
    x_match = re.sub("[,]{1}", "." , x_match)

    return x_match

def requestAPI(pagenumber = 1):
    headers = {"chave-api-dados":"1b15c5e21b0a77d753cdca5570bffa24"}
    pagenumber = pagenumber
    apiURL = f"https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2020&pagina={pagenumber}" 
    response_API = requests.get(apiURL, headers=headers)
    
    return response_API

    
    