#handles all the data analysis of the given set of transactions

from collections import Counter


"""
Get the count of given properties (like from address)
args : list of transactions to parse , properties that needs to be parsed
returns : dict with properties as key and number of occurrence as value
"""
def countUniqueValue(_transactionList,_properties):
    values = {}
    for property in _properties:
        valueCount = Counter()
        for txn in _transactionList:
            valueCount[txn[property]] += 1
        values[property] = dict(valueCount)
    return values


"""
analyse the transaction by passing it to countUniqueValue function
args : list of transactions to parse , properties that needs to be parsed
returns : dict with properties as key and number of occurrence as value
"""
def transactionAnalysis(_transactionList,_properties):
    result = countUniqueValue(_transactionList,_properties)
    return result

"""
get the total value and avg value of a perticular txn property (like gasUsed)
args : list of transactions to parse , properties that needs to be parsed
returns : totalcount and avarage
"""

def get_Total_Avg_Count(_transactionList,_property):
    numberOfTxn = len(_transactionList)
    countDict = countUniqueValue(_transactionList,[_property])[_property]
    totalValue = 0
    for item in countDict:
        totalValue += int(item) * countDict[item]
    return totalValue,totalValue/numberOfTxn

"""
gets the total value of tokens used in a set of transaction
args : list of transactions
returns : dict with token name as key and total value as value
"""
def getTokenValue(_transactionList):
    tokenValueDict = {}
    for txn in _transactionList:
        tokenName = txn["tokenName"]
        if tokenName not in tokenValueDict: #initialize key-value
            tokenValueDict[tokenName] = 0
        tokenValue = txn["value"]
        tokenValueDict[tokenName] += float(tokenValue)
    return tokenValueDict

