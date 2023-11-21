import pandas as pd
from web3 import Web3

datafiles = { v : f'../data/uniswap_{v}_pools.csv' for v in ['v1','v2','v3'] }

def get_pool_addresses(version='v3'):
	df = pd.read_csv( datafiles[version] )
	return list( df['pool'].unique() )

def get_pool_deploy_block(pool_address,version='v3'):
	df = pd.read_csv( datafiles[version], dtype={'pool':str, 'blockNumber': int} )
	df['pool'] = df['pool'].apply(Web3.to_checksum_address)

	blockNumbers = df[df.pool == Web3.to_checksum_address(pool_address)].blockNumber
	if blockNumbers.empty:
		print( f"No records found for pool {Web3.to_checksum_address(pool_address)} in file {datafiles[version]}" )
		return 0
	else:
		try:
			block_number = blockNumbers.iloc[0]
		except Exception as e:
			print( f"Error getting block" )
			print( e )
			print( blockNumbers.head() )
			block_number = 0

		if block_number == 0:
			print( "Error getting deploy block!" )
			print( blockNumbers.head() )	
		else:
			print( f"Pool {Web3.to_checksum_address(pool_address)} deployed at Block {block_number}" )
		return block_number

def get_tokens_addresses(version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return list(df['token'].unique())
	else:
		return list(set(df['token0'].unique()).union( df['token1'].unique() ))

def get_pool_by_symbol(symbol,version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return df.loc[df['token_symbol'] == symbol]
	else:
		return df.loc[(df['token0_symbol'] == symbol) | (df['token1_symbol'] == symbol) ]

def get_pool_by_symbols(symbolA,symbolB=None,version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return df.loc[df['token_symbol'] == symbolA]
	else:
		return df.loc[((df['token0_symbol'] == symbolA) & (df['token1_symbol'] == symbolB)) | ((df['token1_symbol'] == symbolA) & (df['token0_symbol'] == symbolB)) ]

def get_pool_by_tokens(addressA,addressB=None,version='v3'):
	df = pd.read_csv( datafiles[version] )
	
	if version == 'v1':
		return df.loc[df['token'] == addressA]
	else:
		return df.loc[((df['token0'] == addressA) & (df['token1'] == addressB)) | ((df['token1'] == addressA) & (df['token0'] == addressB)) ]



if __name__ == '__main__':

#	pools = get_pool_by_symbol('USDC',version='v1')
#	print( f"{pools.shape[0]} pools found (v1)" )
#	print( pools )

	print( "=================" )

	pools = get_pool_by_symbols('WETH','USDC',version='v3')
	print( f"{pools.shape[0]} pools found (v3)" )
	pools = pools[['pool','token0_symbol','token1_symbol','fee']]
	print( pools )
	
