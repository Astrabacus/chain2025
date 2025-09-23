from eth_account import Account
import json

# Neue Wallet generieren
wallet = Account.create()

# Ausgabe
print("🆕 Neue Ethereum-Adresse:", wallet.address)
print("🔑 Private Key:", wallet.key.hex())

# Optional: JSON-Export für narrative CLI
wallet_data = {
    "address": wallet.address,
    "private_key": wallet.key.hex()
}

with open("new_wallet.json", "w") as f:
    json.dump(wallet_data, f, indent=2)

print("📁 Wallet-Daten gespeichert in: new_wallet.json")