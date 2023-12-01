# Scripts

## [get_factory_events.py](get_factory_events.py)

This script gets all the events emitted by the Uniswap Factory contracts, and saves them to the csvs.

* The events from the [Uniswap v1 Factory](https://etherscan.io/address/0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95) are saved in [uniswap_v1_factory_events.csv](../data/uniswap_v1_factory_events.csv).
* The events from the [Uniswap v2 Factory](https://etherscan.io/address/0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f) are saved in [uniswap_v2_factory_events.csv](../data/uniswap_v2_factory_events.csv).
* The events from the [Uniswap v3 Factory](https://etherscan.io/address/0x1F98431c8aD98523631AE4a59f267346ea31F984) are saved in [uniswap_v3_factory_events.csv](../data/uniswap_v3_factory_events.csv).

The main value of these files is that they provide a complete list of all the Uniswap pool contracts  The Uniswap v1 Factory emits a "NewExchange" event every time a v1 pool is created.  The Uniswap v2 Factory emits a "PairCreated" event every time a v2 pool is created.  The Uniswap v3 Factory emits a "PoolCreated" event every time a v3 pool is created.
