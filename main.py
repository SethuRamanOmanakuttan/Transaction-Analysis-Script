from process.record import  dataRecorder
from scanner.scan import get24HrNormalTxnsByAddress, get24HrTokenTxnsByAddress
from process.fetchData import getTokenValue, transactionAnalysis,get_Total_Avg_Count
import argparse



#write the basic data gathered from the set of transactions
def recordBasicAnalysis(_recordObj,_transactionList):
        properties = ["from","to"]
        metadata ={}
        analysisData = transactionAnalysis(_transactionList,properties)
        _recordObj.initialiseNewSheet("From_Address","Number of Transaction From The Address")
        _recordObj.writeToExcel(analysisData["from"],["Address","Number of Transaction"])
        _recordObj.initialiseNewSheet("To_Address","Number of Transaction To The Address")
        _recordObj.writeToExcel(analysisData["to"],["Address","Number of Transaction"])
        totalGasUsage,AvgGasUsage = get_Total_Avg_Count(_transactionList,"gasUsed")
        totalNumber = len(_transactionList)
        metadata["Total Gas Usage"] = totalGasUsage
        metadata["Avg Gas Usage per Txn"] = AvgGasUsage
        metadata["Total Number of Transaction"] = totalNumber
        _recordObj.initialiseNewSheet("Metadata","Meta Information about the set of transactions")
        _recordObj.writeToExcel(metadata,["Properties","Values"])

#process normal transactions
def analyseTransaction(_recordObj):
    transactionList = get24HrNormalTxnsByAddress()
    recordBasicAnalysis(_recordObj,transactionList)

#process token transactions
#args : recorder object and ERC value :- 20 | 721
def analyseTokenTransaction(_recordObj,_ERC=20):
    transactionList = get24HrTokenTxnsByAddress(_ERC)
    recordBasicAnalysis(_recordObj,transactionList)
    analysisData = transactionAnalysis(transactionList,["tokenName"])
    _recordObj.initialiseNewSheet("Token","Number of transactions using the given tokens")
    _recordObj.writeToExcel(analysisData["tokenName"],["Token Name","Number of Transaction"])
    if(_ERC == 20):
        value = getTokenValue(transactionList)
        _recordObj.initialiseNewSheet("Value","Total value of token exchanged")
        _recordObj.writeToExcel(value,["Token Name","Total Value"])





    
    
#argument parseing
parser = argparse.ArgumentParser(description='Process arguments for Uniswap analyser.')
parser.add_argument("--output",type=str, required=True, help="The excel output file name")
parser.add_argument("--type",type=str, required=True, help="Type of Transactions you want to process ;- normal , token , nft")
args = parser.parse_args()
recorder = dataRecorder(args.output)

print("Processing the transactions...")
#determine the type of transactions that we need to process
if(args.type == 'normal'):
    analyseTransaction(recorder)
elif(args.type == 'token'):
    analyseTokenTransaction(recorder)
elif(args.type == 'nft'):
    analyseTokenTransaction(recorder,721)     
else:
    print(f"We do not support the following transaction type {args.type} ! please select one of the following : normal | token | nft")

print("Report almost done ....")
recorder.saveFile()
print(f"Allright ! you can now view the report from {args.output} file in the base directory!")

