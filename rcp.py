from web3 import Web3

rpc_url = "https://mainnet.infura.io/v3/3339f7ca7edbd2ffaa7eb34f1c099c7c75b794d374323da4f582b818b096d519"
web3 = Web3(Web3.HTTPProvider(rpc_url))

print("✅ Verbindung aktiv:", web3.is_connected())