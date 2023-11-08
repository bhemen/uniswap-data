"""
Scan the chain for all events from the Uniswap factory contracts
"""

uniswap_v1_factory_address = "0xc0a47dFe034B400B47bDaD5FecDa2621de6c4d95"
uniswap_v2_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
uniswap_v2_factory_address = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
uniswap_v3_swaprouter_address = "0xE592427A0AEce92De3Edee1F18E0157C05861564"

v1_factory_deploy_block = 6627917 
v2_factory_deploy_block = 10000835 
v3_factory_deploy_block = 12369621

############################3

api_url = 'http://127.0.0.1:8545'
start_block = v2_factory_deploy_block
contract_address = uniswap_v2_factory_address
outfile = "data/uniswap_v2_factory_events.csv"
scanned_events = 'all'

from tools.get_contract_logs import getContractEvents

getContractEvents(api_url,start_block,contract_address,outfile,scanned_events)

