# Scripts

## [get_factory_events.py](get_factory_events.py)

This script gets all the events emitted by the Uniswap Factory contracts, and saves them to the csvs.

* The events from the [Uniswap v1 Factory](https://etherscan.io/address/0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95) are saved in [uniswap_v1_factory_events.csv](../data/uniswap_v1_factory_events.csv).
* The events from the [Uniswap v2 Factory](https://etherscan.io/address/0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f) are saved in [uniswap_v2_factory_events.csv](../data/uniswap_v2_factory_events.csv).
* The events from the [Uniswap v3 Factory](https://etherscan.io/address/0x1F98431c8aD98523631AE4a59f267346ea31F984) are saved in [uniswap_v3_factory_events.csv](../data/uniswap_v3_factory_events.csv).

## [add_symbols.py](add_symbols.py)

The Uniswap v1 Factory emits a "NewExchange" event every time a v1 pool is created.  The Uniswap v2 Factory emits a "PairCreated" event every time a v2 pool is created.  The Uniswap v3 Factory emits a "PoolCreated" event every time a v3 pool is created, so the Factory events provide a complete list of all the Uniswap pools and their addresses.

These events include the addresses of the token(s) being traded in the pool, but not the names or symbols of these tokens.  The [add_symbols.py](add_symbols.py) script reads the factory events, and for each token, it adds the name and symbol of the token.  This provides a nice list of all the Uniswap Pools that can be searched by name or symbol.

* [uniswap_v1_pools.csv](../data/uniswap_v1_pools.csv) has all the Uniswap v1 Pools
* [uniswap_v2_pools.csv](../data/uniswap_v2_pools.csv) has all the Uniswap v2 Pools
* [uniswap_v3_pools.csv](../data/uniswap_v3_pools.csv) has all the Uniswap v3 Pools

## [get_specific_pool_info.py](get_specific_pool_info.py)

This script gets the historical balances of specified pools.  The script grabs the pool deploy block (from the relevant uniswap_v?_pools.csv), then queries an Ethereum archive node every 100 blocks to grab three pieces of data

1. The total supply of LP tokens at that block
2. The pool balance of token0 at that block
3. The pool balance of token1 at that block

The output is put into a file with the pool address and the token symbols (e.g. [v2-0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852-WETH-USDT.csv](../data/v2-0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852-WETH-USDT.csv)).

For Uniswap v2, this is enough to track Liquidity Provider earnings.  If the total supply of LP tokens at block $t$ is $N_t$, and the pool balance of token0 is $X_t$, and the pool balance of token1 is $Y_t$, then each LP token is redeemable for $X_t/N_t$ token0 and $Y_t/N_t$ token1.  To calculate a LP's earnings from $t_0$ to $t_1$, we just need to calculate the change in value of an LP token from $t_0$ to $t_1$.

## [search_pools.py](search_pools.py)

This script provides some utilities for searching the factory event logs.  For example, it provides the function get_pool_deploy_block(), which is used by [get_specific_pool_info.py](get_specific_pool_info.py) to easily lookup the block number at which a given pool was deployed.  It also provides functions that allow you to find all the pools that trade a given token.
