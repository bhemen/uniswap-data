import pandas as pd

datafiles = { v : f'../data/uniswap_{v}_pools.csv' for v in ['v1','v2','v3'] }

def get_pool_addresses(version='v3'):
	df = pd.read_csv( datafiles[version] )
	return list( df['pool'].unique() )

def get_token_addresses(version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return list(df['token0'].unique())
	else:
		return list(set(df['token0'].unique()).union( df['token1'].unique() ))

def get_pool_address_by_symbol(symbol,version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return df.loc[df['token_symbol'] == symbol]
	else:
		return df.loc[(df['token0_symbol'] == symbol) | (df['token1_symbol'] == symbol) ]

def get_pool_address_by_symbols(symbolA,symbolB=None,version='v3'):
	df = pd.read_csv( datafiles[version] )
	if version == 'v1':
		return df.loc[df['token_symbol'] == symbolA]
	else:
		return df.loc[((df['token0_symbol'] == symbolA) & (df['token1_symbol'] == symbolB)) | ((df['token1_symbol'] == symbolA) & (df['token0_symbol'] == symbolB)) ]

def get_pool_address_by_tokens(addressA,addressB=None,version='v3'):
	df = pd.read_csv( datafiles[version] )
	
	if version == 'v1':
		return df.loc[df['token'] == addressA]
	else:
		return df.loc[((df['token0'] == addressA) & (df['token1'] == addressB)) | ((df['token1'] == addressA) & (df['token0'] == addressB)) ]



if __name__ == '__main__':

#	pools = get_pool_address_by_symbol('USDC',version='v1')
#	print( f"{pools.shape[0]} pools found (v1)" )
#	print( pools )

	print( "=================" )

	pools = get_pool_address_by_symbols('WETH','USDC',version='v3')
	print( f"{pools.shape[0]} pools found (v3)" )
	pools = pools[['pool','token0_symbol','token1_symbol','fee']]
	print( pools )
	
