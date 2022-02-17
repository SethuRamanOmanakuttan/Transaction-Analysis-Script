#file to handle some generic operations and constants


import json
import requests

#urls
URL_BlockCount = "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={}&closest=before&apikey={}"
URL_TxnList = "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock={}&endblock={}&page=1&offset=10&sort=asc&apikey={}"
URL_TokenTxn = "https://api.etherscan.io/api?module=account&action={}&address={}&page=1&offset=100&startblock={}&endblock={}&sort=asc&apikey={}"

#get the contract addresses and api keys from config file
#provide the key as argument to get the corresponding value
def fetchValueFromConfig(_key):
    with open('config.json') as config:
        configData = json.load(config)
        return  configData[_key]

#handle the request and the errors, if any
def getRequest(_url):
    try:
        resp = requests.get(_url)
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(e)
        exit(0)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
        print("Please try again in a couple of seconds !")
        exit(0)

#validating the request result
def validateResult(_result):
    if(len(_result) == 0): #if the result is empty
        raise ValueError("There are no normal transactions available from the past 24 hr! you may confirm it using etherscan explorer")
    if (type(_result[-1]) == "Invalid API Key"):
        errorStr = f"There seems to be an issue with the api key"
        raise ValueError(errorStr)


    
