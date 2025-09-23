from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

block = w3.eth.get_block(0, full_transactions=True)

print("🧱 Block #0 Inhalt:")
print(block)