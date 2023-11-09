from web3 import Web3
from web3.providers.rpc import HTTPProvider
import json
import pandas as pd
import csv

#When you want to interact with a contract, you need to know its Application Binary Interface (ABI).
#The ABI is *not* provided on the chain, and you need to get it from somewhere else
#Here is a hard-coded version of a generic interface for an ERC20 contract
ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]') 
MINIMAL_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

api_url = f"http://127.0.0.1:8545"
provider = HTTPProvider(api_url)
web3 = Web3(provider)

token_info = {}

def getSymbolAndName( address ):
	symbol = name = ""
	try:
		address = Web3.to_checksum_address(address)
	except Exception as e:
		return pd.Series( ["", ""] )

	if address in token_info.keys():
		return token_info[address]

	try:
		contract = web3.eth.contract(address=address,abi=MINIMAL_ABI)
	except Exception as e:
		return pd.Series( ["", ""] )
	
	try:
		symbol = contract.functions.symbol().call()
	except Exception as e:
		symbol = ""

	try:
		name = contract.functions.name().call()
	except Exception as e:
		name = ""

	token_info[address] = pd.Series( [symbol,name] )

	return token_info[address]

	
###
#V1
###
	
infile = "../data/uniswap_v1_factory_events.csv"

df = pd.read_csv(infile)
df = df[df.event == 'NewExchange']
df = df[['blockNumber','timestamp','msg.sender','exchange','token','transactionHash']]

#df = df.head(100)

df = df.rename(columns={'exchange': 'pool'})

df[['token_symbol','token_name']] = df.token.apply(getSymbolAndName)

outfile = "../data/uniswap_v1_pools.csv"
df.to_csv( outfile, index=False, escapechar='\\' )

###
#V2
###

infile = "../data/uniswap_v2_factory_events.csv"

df = pd.read_csv(infile)
df = df[df.event == 'PairCreated']
df = df[['blockNumber','timestamp','msg.sender','pair','token0','token1','transactionHash']]

df = df.rename(columns={'exchange': 'pair'})
#df = df.head(100)

df[['token0_symbol','token0_name']] = df.token0.apply(getSymbolAndName)
df[['token1_symbol','token1_name']] = df.token1.apply(getSymbolAndName)

outfile = "../data/uniswap_v2_pools.csv"
df.to_csv( outfile, index=False, escapechar='\\' )
	
###
#V3
###
	
infile = "../data/uniswap_v3_factory_events.csv"

df = pd.read_csv(infile)
df = df[df.event == 'PoolCreated']
df = df[['blockNumber','timestamp','msg.sender','pool','token0','token1','fee','transactionHash']]

#df = df.head(100)

df[['token0_symbol','token0_name']] = df.token0.apply(getSymbolAndName)
df[['token1_symbol','token1_name']] = df.token1.apply(getSymbolAndName)

outfile = "../data/uniswap_v3_pools.csv"
df.to_csv( outfile, index=False, escapechar='\\' )

