from web3 import Web3
import json
import getpass

# Pfad zur Keystore-Datei
keystore_path = "wallet/keystore/UTC--2025-09-21T10-59-47.252269982Z--9ec23e5215a8d28e96bc792055251850eea01ec0"

# Passwort sicher eingeben
password = getpass.getpass("🔐 Passwort für Genesis-Keystore: ")

# Keystore laden
with open(keystore_path, 'r') as f:
    keystore = json.load(f)

# Private Key entschlüsseln
try:
    private_key = Web3().eth.account.decrypt(keystore, password)
    print("✅ Entschlüsselung erfolgreich")
    print("🔑 Dein Genesis Private Key:", private_key.hex())
except ValueError:
    print("❌ Falsches Passwort oder ungültiger Keystore")