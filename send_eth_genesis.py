from web3 import Web3
import os

# Infura RPC URL
rpc_url = "https://mainnet.infura.io/v3/12482a84eb8d473d90458c30c6be91de"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Verbindung prüfen
if not web3.is_connected():
    raise Exception("❌ Verbindung zu Infura fehlgeschlagen")

# Private Key aus Umgebungsvariable holen
private_key = os.environ.get("PRIVATE_KEY")
account = web3.eth.account.from_key(private_key)
sender = account.address

# Sicherstellen, dass es die Genesis-Adresse ist
assert sender.lower() == "0x9c2e5215a8d28e96bC792055251850eEa01eC0", "❌ Falscher Private Key für Genesis-Adresse"

# Zieladresse und Betrag
recipient = "0x01644a9a8A4337bE54FBE87365BeA9De07F3C590"  # z. B. deine Agentenadresse
amount = 0.001  # ETH

# Nonce abrufen
nonce = web3.eth.get_transaction_count(sender, "pending")

# Transaktion definieren
tx = {
    'nonce': nonce,
    'to': recipient,
    'value': web3.to_wei(amount, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei('40', 'gwei')  # stabiler Gaspreis
}

# Transaktion signieren
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Transaktion senden
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
print("✅ Transaktion gesendet von Genesis-Adresse:", sender)
print("🔗 Hash:", web3.to_hex(tx_hash))