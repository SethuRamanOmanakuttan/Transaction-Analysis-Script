#this file deals with fetching data using ethscan apis

from scanner.util import *
import time

#get the uniswap staker address(V3)
Uniswap_Address = fetchValueFromConfig("UNISWAP_STAKER_ADDRESS")
# Uniswap_Address = fetchValueFromConfig("UNISWAP__POOL_ADDRESS")
EthScan_Key = fetchValueFromConfig("ETHSCAN_API_KEY") #get the EtherScan Api Key 



"""
function retrives the latest block number and
the block number of the block that was mined 24 hours ago.

"""
def get24HrBlockNumber():
    timeStamp_24hr = str(int(time.time())-86400) #minus 24 hours(in seconds)
    blockNumber_24hr = str(getBlockNumberByTimestamp(timeStamp_24hr))
    blockNumber_current = str(getBlockNumberByTimestamp())
    return blockNumber_24hr,blockNumber_current

"""
function to get the block based on timestamp
args : timestamp in unix format
returns : block number
"""
def getBlockNumberByTimestamp(_unixTimestamp =None):
    if(not _unixTimestamp):#if no timestamp is provided
        _unixTimestamp = str(int(time.time())) #set the timestamp to now
    blockCountUrl =  URL_BlockCount.format(_unixTimestamp,EthScan_Key) #set the url
    result = getDataUsingUrl(blockCountUrl)
    return result



"""
function to handle the requests
returns : list of transactions
"""
def getDataUsingUrl(_url):
    addressContent = getRequest(_url)
    result =  addressContent.get("result")
    try:
        validateResult(result)
    except ValueError as e:
        print(e)
        exit()
    return result #returns list of transactions

"""
iterate through the 24 hour intervel block numbers and
find the transactions made using the uniswap contract address
returns : list of normal transactions
"""
def get24HrNormalTxnsByAddress():
    lastBlock,currentBlock = get24HrBlockNumber()
    txListUrl = URL_TxnList.format(Uniswap_Address,lastBlock,currentBlock,EthScan_Key)
    print("Fetching normal transactions from the past 24 hours ....")
    result = getDataUsingUrl(txListUrl)
    return result

"""
iterate through the 24 hour intervel block numbers and
find the token transactions made using the uniswap contract address
args : specify if it is ERC-20 token or ERC-721
returns : list of token transactions
"""

def get24HrTokenTxnsByAddress(_ERC=20): #default is set to 20
    action = 'tokentx'
    if _ERC == 721:
        action = 'tokennfttx'
    lastBlock,currentBlock = get24HrBlockNumber() #get the 24 hour interval block numbers
    tokenTxnURL = URL_TokenTxn.format(action,Uniswap_Address,lastBlock,currentBlock,EthScan_Key)
    print(f"Fetching ERC-{_ERC} transactions from the past 24 hours ....")
    result = getDataUsingUrl(tokenTxnURL)
    return result
