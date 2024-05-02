# Overview

This folder holds some of the data gathered from Uniswap's Ethereum contracts.
In addition to the data provided here, additional data files (giving the full transaction logs of popular Uniswap v3 pools) are available in our [Box folder](https://upenn.box.com/s/ay5e6tc47pvwauo1kc4fboa17k0zc7ik).

# Data files available in this repository

## Factory events

### Uniswap v1

The Uniswap v1 factory has created over 4000 Uniswap v1 pools.
* [uniswap_v1_factory_events.csv](uniswap_v1_factory_events.csv) - gives a full list of events emitted by the Uniswap v1 Factory.  The only event emitted by the Uniswap v1 factory contract is the "NewExchange" event, which is emitted whenever a new pool ("exchange") is produced.  Recall that in Uniswap v1, each pool holds one ERC-20 token (which can be traded for ETH).  This file is created by [get_factory_events.py](../scripts/get_factory_events.py).
* [uniswap_v1_pools.csv](uniswap_v1_pools.csv) - gives a full list of all the Uniswap v1 pools, together with the token symbol.  This file is created by reading [uniswap_v1_factory_events.csv](uniswap_v1_factory_events.csv) to get the address of each pool, and then looking up the ERC-20 symbol of the token being traded by the pool.  This file is created by [add_symbols.py](../scripts/add_symbols.py).

#### Uniswap v2

The Uniswap v2 factory has created over 160,000 Uniswap v2 pools.
* [uniswap_v2_factory_events.csv](uniswap_v2_factory_events.csv) - gives a full list of events emitted by the Uniswap v2 Factory.  The only event emitted by the Uniswap v2 factory contract is the "PairCreated" event, which is emitted whenever a new pool ("pair") is produced.  Recall that in Uniswap v2, each pool holds a pair of ERC-20 tokens.  This file is created by [get_factory_events.py](../scripts/get_factory_events.py).
* [uniswap_v2_pools.csv](uniswap_v2_pools.csv) - gives a full list of all the Uniswap v2 pools, together with the token symbol.  This file is created by reading [uniswap_v2_factory_events.csv](uniswap_v2_factory_events.csv) to get the address of each pool, and then looking up the ERC-20 symbols of the tokens being traded by the pool.  This file is created by [add_symbols.py](../scripts/add_symbols.py).

#### Uniswap v3

The Uniswap v3 factory has created over 11,000 Uniswap v3 pools.
* [uniswap_v3_factory_events.csv](uniswap_v3_factory_events.csv) - gives a full list of events emitted by the Uniswap v3 Factory.  The factory emits three events "OwnerChanged," "FeeAmountEnabled" and "PoolCreated".  This file is created by [get_factory_events.py](../scripts/get_factory_events.py).
* [uniswap_v3_pools.csv](uniswap_v3_pools.csv) - gives a full list of all the Uniswap v3 pools, together with the token symbol.  This file is created by reading [uniswap_v3_factory_events.csv](uniswap_v3_factory_events.csv) to get the address of each pool (from the "PoolCreated" events), and then looking up the ERC-20 symbols of the tokens being traded by the pool.  This file is created by [add_symbols.py](../scripts/add_symbols.py).

## Pool data

This repository also historical balance data from some (popular) pools.  These logs are created by the [get_specific_pool_info.py](../scripts/get_specific_pool_info.py).  These files currently have data sampled every 100 blocks, but this can easily be changed by modifying [get_specific_pool_info.py](../scripts/get_specific_pool_info.py).  These files make it easy to calculate the average LP returns for each pool.

* [Uniswap v2 WETH-USDC](v2-0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852-WETH-USDT.csv)
* [Uniswap v2 WETH-USDC](v2-0x21b8065d10f73ee2e260e5b47d3344d3ced7596e-WISE-WETH.csv)
* [Uniswap v2 USDC-USDT](v2-0x3041cbd36888becc7bbcbc0045e3b1f144466f5f-USDC-USDT.csv)
* [Uniswap v2 FNK-USDT](v2-0x61b62c5d56ccd158a38367ef2f539668a06356ab-FNK-USDT.csv)
* [Uniswap v2 FEI-TRIBE](v2-0x9928e4046d7c6513326ccea028cd3e7a91c7590a-FEI-TRIBE.csv)
* [Uniswap v2 DAI-WETH](v2-0xa478c2975ab1ea89e8196811f51a7b7ade33eb11-DAI-WETH.csv)
* [Uniswap v2 DAI-USDC](v2-0xae461ca67b15dc8dc81ce7615e0320da1a9ab8d5-DAI-USDC.csv)
* [Uniswap v2 DAI-USDT](v2-0xb20bd5d04be54f870d5c0d3ca85d82b34b836405-DAI-USDT.csv)
* [Uniswap v2 USDC-WETH](v2-0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc-USDC-WETH.csv)
* [Uniswap v2 WBTC-WETH](v2-0xbb2b8038a1640196fbe3e38816f3e67cba72d940-WBTC-WETH.csv)
* [Uniswap v2 FXS-FRAX](v2-0xe1573b9d29e2183b1af0e743dc2754979a40d237-FXS-FRAX.csv)

These files have the following columns:

* pool_address - The address of the pool (stays constant within a file)
* token0_address - The address of token 0 (stays constant within a file)
* token1_address - The address of token 1 (stays constant within a file)
* token0_symbol - The symbol of token 0 (stays constant within a file)
* token1_symbol - The symbol of token 1 (stays constant within a file)
* block - The current block height (i.e., the current block number)
* ts - The timestamp of the block
* token0_bal - The total balance of token 0 held by the pool at the current block height (obtained by calling balance_of() on the token 0 contract)
* token1_bal - The total balance of token 1 held by the pool at the current block height (obtained by calling balance_of() on the token 1 contract)
* lp_supply - The total supply of LP tokens at the current block height (obtained by calling total_supply() on the pool contract)


# Data Schema for Uniswap v3 Pool Data (available on [Box](https://upenn.box.com/s/ay5e6tc47pvwauo1kc4fboa17k0zc7ik))

This document outlines the data schema for the top liquidity pools on Uniswap v3, as identified from [Uniswap Pool Statistics](https://info.uniswap.org/#/pools). The pools included in this schema are among the most active and significant in terms of liquidity and trading volume. It's important to note that the rankings of these pools are subject to change, but they generally represent the most prominent pools in the Uniswap ecosystem. The scraped data for these pools can be found in this [Box folder](https://upenn.box.com/s/ay5e6tc47pvwauo1kc4fboa17k0zc7ik).

Some of the pools available for download from [Box](https://upenn.box.com/s/ay5e6tc47pvwauo1kc4fboa17k0zc7ik) are:

1. **DAI/USDC Pool**
   - Address: [0x5777d92f208679db4b9778590fa3cab3ac9e2168](https://etherscan.io/address/0x5777d92f208679db4b9778590fa3cab3ac9e2168)
2. **FRAX/USDC Pool**
   - Address: [0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52](https://etherscan.io/address/0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52)
3. **USDC/ETH Pool ([.05% Fee](https://support.uniswap.org/hc/en-us/articles/20904283758349-What-are-fee-tiers))**
   - Address: [0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640](https://etherscan.io/address/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640)
4. **USDC/ETH Pool ([.3% Fee](https://support.uniswap.org/hc/en-us/articles/20904283758349-What-are-fee-tiers))**
   - Note: This is a distinct pool from the first USDC/ETH pool, denote as `USDCETH2` for distinction.
   - Address: [0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8](https://etherscan.io/address/0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8)
5. **WBTC/ETH Pool**
   - Address: [0xcbcdf9626bc03e24f779434178a73a0b4bad62ed](https://etherscan.io/address/0xcbcdf9626bc03e24f779434178a73a0b4bad62ed)

Each of these pools plays a vital role in the Uniswap ecosystem, offering significant liquidity and trading opportunities. The data schema will provide insights into the workings of these pools, including liquidity metrics, transaction details, and more.

## Events

This schema details the data structure for events scraped from Uniswap v3 pool contracts. The events are identical across different pools due to the standardized implementation of Uniswap v3. For illustration purposes, we use the WBTC/ETH pool as an example. The same structure applies to other pools: DAI/USDC, FRAX/USDC, USDC/ETH, and USDC/ETH2.

The events covered in this schema include:

* `Burn` - Describes the burning of LP tokens.  This event is emitted when an LP withdraws funds from the pool.
* `Collect` - Represents the collection of fees accrued from providing liquidity.
* `Flash` - Details flash loan transactions.
* `IncreaseObservationCardinalityNext` - Pertains to adjustments in the observation cardinality.
* `Initialize` - Initial setup of a liquidity pool.
* `Mint` - Describes the creation of LP tokens.  This event is emitted when an LP deposits funds into the pool.
* `Swap` - Represents swap events between tokens in the pool.

Each event's structure will be detailed in the following sections.

## Event Schema

### `Burn` Event
Columns in `Uniswap_WBTCETH_Burn.csv`:
- `event`: Type of the event (Burn).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `owner`: Address of the liquidity position owner.
- `tickLower`: Lower end of the tick range.
- `tickUpper`: Upper end of the tick range.
- `amount`: Amount of liquidity burned.
- `amount0`: Amount of token0 burned.
- `amount1`: Amount of token1 burned.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `Collect` Event
Columns in `Uniswap_WBTCETH_Collect.csv`:
- `event`: Type of the event (Collect).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `owner`: Address of the liquidity position owner.
- `tickLower`: Lower end of the tick range.
- `tickUpper`: Upper end of the tick range.
- `recipient`: Address of the fee recipient.
- `amount0`: Amount of token0 collected.
- `amount1`: Amount of token1 collected.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `Flash` Event
Columns in `Uniswap_WBTCETH_Flash.csv`:
- `event`: Type of the event (Flash).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `sender`: Address of the flash loan sender.
- `recipient`: Address of the flash loan recipient.
- `amount0`: Amount of token0 in the flash loan.
- `amount1`: Amount of token1 in the flash loan.
- `paid0`: Amount of token0 paid back.
- `paid1`: Amount of token1 paid back.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `IncreaseObservationCardinalityNext` Event
Columns in `Uniswap_WBTCETH_IncreaseObservationCardinalityNext.csv`:
- `event`: Type of the event (IncreaseObservationCardinalityNext).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `observationCardinalityNextOld`: Old observation cardinality value.
- `observationCardinalityNextNew`: New observation cardinality value.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `Initialize` Event
Columns in `Uniswap_WBTCETH_Initialize.csv`:
- `event`: Type of the event (Initialize).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `sqrtPriceX96`: The square root of the price in X96 format.
- `tick`: The tick associated with the event.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `Mint` Event
Columns in `Uniswap_WBTCETH_Mint.csv`:
- `event`: Type of the event (Mint).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `owner`: Address of the liquidity position owner.
- `tickLower`: Lower end of the tick range.
- `tickUpper`: Upper end of the tick range.
- `sender`: Address that initiated the minting.
- `amount`: Total amount of liquidity minted.
- `amount0`: Amount of token0 used in minting.
- `amount1`: Amount of token1 used in minting.
- `block_timestamp`: Human-readable timestamp of the block.
- `block_timestamp_unix`: Unix timestamp of the block.

### `Swap` Event
Columns in `Uniswap_WBTCETH_Swap.csv`:
- `event`: Type of the event (Swap).
- `logIndex`: Index of the event log.
- `transactionIndex`: Index of the transaction within the block.
- `transactionHash`: Hash of the transaction.
- `address`: Address of the contract that emitted the event.
- `blockHash`: Hash of the block containing the event.
- `blockNumber`: Number of the block.
- `sender`: Address that initiated the swap.
- `recipient`: Address that received the swap output.
- `amount0`: Amount of token0 used in the swap.
- `amount1`: Amount of token1 used in the swap.
- `sqrtPriceX96`: The square root of the product of the prices of the two tokens, scaled by $2^{96}$. This is a key metric in Uniswap v3's concentrated liquidity mechanism.
- `liquidity`: The liquidity of the pool at the time of the swap.
- `tick`: The current price tick of the pool.
- `block_timestamp`: The human-readable timestamp of the block when the event occurred.
- `block_timestamp_unix`: The Unix timestamp of the block when the event occurred.

