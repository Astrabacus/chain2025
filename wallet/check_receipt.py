from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

tx_hash = "0xa0648c0998f50d90130a1f0c589a11a58c0ee19f255bafc308698d68744089da"
receipt = w3.eth.get_transaction_receipt(tx_hash)

print("🧾 Transaktions-Receipt:")
print(receipt)