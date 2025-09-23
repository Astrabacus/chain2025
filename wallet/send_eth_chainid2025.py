from web3 import Web3

# Verbindung zum lokalen Geth-Node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Absenderadresse (aus Genesis)
sender = "0x4Fa7B3aD32164c91eD76D37611088567E14538c3"

# Empfängeradresse (z. B. MetaMask)
receiver = "0x01644a9a8A4337bE54FBE87365BeA9De07F3C590"

# Privater Schlüssel des Absenders (64 hex-Zeichen mit 0x-Präfix)
private_key = "0x4f3c2e1d9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d"

# Transaktion definieren
tx = {
    'from': sender,
    'to': receiver,
    'value': w3.to_wei(1, 'ether'),  # exakt 1 ETH
    'gas': 21000,
    'gasPrice': w3.to_wei(1, 'gwei'),
    'nonce': w3.eth.get_transaction_count(sender),
    'chainId': 2025
}

# Signieren und senden
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("🜂 Transaktion gesendet:", tx_hash.hex())