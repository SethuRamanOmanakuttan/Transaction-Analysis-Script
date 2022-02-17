# Transaction-Analysis-Script

A python script that can analyse blockchain transactions based on a given contract address

 

## Prerequisites

- python 3.6
- Etherscan Account

---

## Description

The transaction-Analysis-Script is a python based script that enables easy fetching of transactions based on a particular smart-contract address.  It also enables basic analysis atop the set of transactions. Theoretically the script can work with any given contract address, but currently it is configured to work with the uniswap contracts. The scripts pulls all the transactions that took place within a 24 hour window and provides basic stats on the transactions. The script makes use of the etherscan api in order to fetch the transactions.
Once the transaction is processed, the report of the analysis will be generated in the form of an excel file.
The project is highly modular and at present, basic. There is lot of room for adding more analytics functionalities on to the script with minimal effort.

---

## Getting Started

- Before you start, make sure you have an etherscan account. If you do, then copy the provided api key and paste it in the config.json file
- Make sure you have python version => 3.6
- Once you set up all the prerequisites in your system, go to the base folder of the project and type
  ```
  pip install -r requirements.txt
  ```
- This will install all the required python libraries
- Once you have all the packages installed, you can run
  ```
  python main --output <output_file_name>.xlsx --type <normal | token | nft> 
  ```
- This is will fetch the desired type of transaction based on your choice and result of the analysis will be produced in an excel file in the base directory. The excel file has multiple sheet and each of them provides the data regarding a particular property of the set of transactions.

### Type of transactions

- The script allows you to select from three different types of transaction that you would like to analyse
  - Normal Transaction (--type normal)  :  deals with normal transactions
  - ERC-20 Transaction (--type token )  :  deals with transactions that transfer ERC-20 tokens
  - ERC-721 Transaction (--type nft)    :  deals with transactions that transfer ERC-721 tokens

### Analysis Insights

- The following are some of the major insights that you can get from the script
  - GasUsage
  - token details
  - account details
  - transaction details
  - token values
  
### Sample Reports
- There are some sample reports available in the sample reports folder 

---

## Comments

As mentioned earlier, currently the script is configured to work with uniswap contracts, There are 2 uniswap contract addresses in the config.json file and those addresses are currently being used by the contract. Developers can add any contract address in the config.json file and run the given analysis on its transactions. Note that there are some minor changes required in the scan.py and util.py file [scanner folder], in order for it to take effect.
