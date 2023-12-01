# Uniswap v3 Pool Data Schema

This document outlines the data schema for the top liquidity pools on Uniswap v3, as identified from [Uniswap Pool Statistics](https://info.uniswap.org/#/pools). The pools included in this schema are among the most active and significant in terms of liquidity and trading volume. It's important to note that the rankings of these pools are subject to change, but they generally represent the most prominent pools in the Uniswap ecosystem. The scraped data for these pools can be found in this [Box folder](https://upenn.box.com/s/ay5e6tc47pvwauo1kc4fboa17k0zc7ik).

The pools covered in this schema are:

1. **DAI/USDC Pool**
   - Address: [0x5777d92f208679db4b9778590fa3cab3ac9e2168](https://etherscan.io/address/0x5777d92f208679db4b9778590fa3cab3ac9e2168)
2. **FRAX/USDC Pool**
   - Address: [0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52](https://etherscan.io/address/0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52)
3. **USDC/ETH Pool ([.05% Fee](https://support.uniswap.org/hc/en-us/articles/20904283758349-What-are-fee-tiers)**
   - Address: [0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640](https://etherscan.io/address/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640)
4. **USDC/ETH Pool ([.3% Fee](https://support.uniswap.org/hc/en-us/articles/20904283758349-What-are-fee-tiers)**
   - Note: This is a distinct pool from the first USDC/ETH pool, denote as `USDCETH2` for distinction.
   - Address: [0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8](https://etherscan.io/address/0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8)
5. **WBTC/ETH Pool**
   - Address: [0xcbcdf9626bc03e24f779434178a73a0b4bad62ed](https://etherscan.io/address/0xcbcdf9626bc03e24f779434178a73a0b4bad62ed)

Each of these pools plays a vital role in the Uniswap ecosystem, offering significant liquidity and trading opportunities. The data schema will provide insights into the workings of these pools, including liquidity metrics, transaction details, and more.

## Event

This schema details the data structure for events scraped from Uniswap v3 pool contracts. The events are identical across different pools due to the standardized implementation of Uniswap v3. For illustration purposes, we use the WBTC/ETH pool as an example. The same structure applies to other pools: DAI/USDC, FRAX/USDC, USDC/ETH, and USDC/ETH2.

The events covered in this schema include:

* `Burn` - Describes the burning of liquidity tokens.
* `Collect` - Represents the collection of fees accrued from providing liquidity.
* `Flash` - Details flash loan transactions.
* `IncreaseObservationCardinalityNext` - Pertains to adjustments in the observation cardinality.
* `Initialize` - Initial setup of a liquidity pool.
* `Mint` - Describes the creation of liquidity tokens.
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

