"""
Get balance information from a handful of interesting Uniswap pools
This requires a full archive node 
"""

from web3.providers.rpc import HTTPProvider
from web3 import Web3
import json
import datetime
import sys
import pandas as pd
import sys
from tqdm import tqdm
from search_pools import get_pool_deploy_block

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
POOL_MINIMAL_ABI = json.loads('''[{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[],"name":"token0","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[],"name":"token1","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]''')

#FULL_ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]') 

MINIMAL_ERC20_ABI = json.loads('''[{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},
	{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]''')

def get_balance_history( pool_address, start_block, end_block, step = 1000, version='v2' ):

	if version == "v1":
		print( f"V1 is different" )
		return
	else:
		pool_address = Web3.to_checksum_address(pool_address)
		pool_contract = web3.eth.contract(address=pool_address,abi=POOL_MINIMAL_ABI) #We only need to call balanceOf and totalSupply on the pool

		token0_address = pool_contract.functions.token0().call()	
		token1_address = pool_contract.functions.token1().call()	

		token0 = web3.eth.contract(address=token0_address,abi=MINIMAL_ERC20_ABI)
		token1 = web3.eth.contract(address=token1_address,abi=MINIMAL_ERC20_ABI)

		token0_symbol = token0.functions.symbol().call()
		token1_symbol = token1.functions.symbol().call()

		print( f"Grabbing pool {token0_symbol} - {token1_symbol}" )

		try:
			token0_dec = token0.functions.decimals().call()
		except Exception as e:
			print( f"Failed to get decimals for {token0_address}" )
			print( e )
			return None
		try:
			token1_dec = token1.functions.decimals().call()
		except Exception as e:
			print( f"Failed to get decimals for {token1_address}" )
			print( e )
			return None

		blocks = range( start_block, end_block, step )
		rows = []

		for block in tqdm(blocks):
			try:
				token0_bal = token0.functions.balanceOf(pool_address).call(block_identifier=block)
				token1_bal = token1.functions.balanceOf(pool_address).call(block_identifier=block)
				lp_supply = pool_contract.functions.totalSupply().call(block_identifier=block)
			except Exception as e:
				print( f"Failed!" )
				print( f"Block num = {block}" )
				print( f"pool_address = {pool_address}" )
				print( e )
				continue
			lp_supply = float(lp_supply)/10**18
			token0_bal = float(token0_bal)/10**token0_dec
			token1_bal = float(token1_bal)/10**token1_dec
			block_ts = web3.eth.get_block(block)['timestamp']
			ts = datetime.datetime.fromtimestamp(block_ts)
			rows.append({ 'pool_address': pool_address,
					'token0_address': token0_address,
					'token1_address': token1_address,
					'token0_bal': token0_bal,
					'token1_bal': token1_bal,
					'lp_supply': lp_supply,
					'token0_symbol': token0_symbol,
					'token1_symbol': token1_symbol,
					'block': block,
					'ts': block_ts } )

	historical_df = pd.DataFrame(rows)
	return historical_df


if __name__ == '__main__':
	usdc_eth = "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc"
	dai_usdc = "0xae461ca67b15dc8dc81ce7615e0320da1a9ab8d5"
	wise_eth = "0x21b8065d10f73ee2e260e5b47d3344d3ced7596e"
	fei_tribe = "0x9928e4046d7c6513326ccea028cd3e7a91c7590a"
	weth_usdt = "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852"
	fxs_frax = "0xe1573b9d29e2183b1af0e743dc2754979a40d237"
	fnk_usdt = "0x61b62c5d56ccd158a38367ef2f539668a06356ab"
	wbtc_weth = "0xbb2b8038a1640196fbe3e38816f3e67cba72d940"
	usdc_usdt = "0x3041cbd36888becc7bbcbc0045e3b1f144466f5f"
	dai_eth = "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"
	dai_usdt = "0xb20bd5d04be54f870d5c0d3ca85d82b34b836405"
	eth_usdt = "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852"

	interesting_pools = [usdc_eth,eth_usdt,dai_usdc,wise_eth,fei_tribe,weth_usdt,fxs_frax,fnk_usdt,wbtc_weth,usdc_usdt,dai_eth,dai_usdt]

	step_size = 100 
	version = 'v2'
	#outfile = "../data/interesting_pool_stats.csv"

	for i,pool in enumerate(interesting_pools):
		current_block = web3.eth.block_number
		start_block = get_pool_deploy_block( pool, version )
		pool_history = get_balance_history( pool, start_block, current_block, step_size, version=version )
		if pool_history is not None:
			token0_symbol = pool_history.token0_symbol[0]
			token1_symbol = pool_history.token1_symbol[0]
			pool_history.to_csv( f"../data/{version}-{pool}-{token0_symbol}-{token1_symbol}.csv", index=False )


