from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

address = "0x4Fa7B3aD32164c91eD76D37611088567E14538c3"
balance = w3.eth.get_balance(address)

print("🪙 Guthaben:", w3.from_wei(balance, 'ether'), "ETH")