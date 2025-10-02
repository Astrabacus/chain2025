import json
import os
import hashlib as hasher

BLOCK_PATH = r"C:\Users\DanielAecherli\CoreCraftSystems\infra\chain\chainid2025\ares\blocks"

def hash_block(block):
    sha = hasher.sha256()
    sha.update(str(block["index"]).encode('utf-8') +
               str(block["timestamp"]).encode('utf-8') +
               str(block["data"]).encode('utf-8') +
               str(block["previous_hash"]).encode('utf-8') +
               str(block["commit_hash"]).encode('utf-8') +
               str(block["manifest_hash"]).encode('utf-8') +
               str(block["license_type"]).encode('utf-8') +
               str(block["validator_sig"]).encode('utf-8'))
    return sha.hexdigest()

def verify_chain():
    files = sorted([f for f in os.listdir(BLOCK_PATH) if f.startswith("block_")])
    previous_hash = "0"
    for file in files:
        with open(os.path.join(BLOCK_PATH, file), "r") as f:
            block = json.load(f)
        calculated_hash = hash_block(block)
        if block["hash"] != calculated_hash:
            print(f"❌ Hash mismatch in {file}")
        elif block["previous_hash"] != previous_hash:
            print(f"⚠️ Chain break in {file} – previous hash mismatch")
        else:
            print(f"✅ {file} verified")
        previous_hash = block["hash"]

if __name__ == "__main__":
    verify_chain()