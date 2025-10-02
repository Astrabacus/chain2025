import hashlib as hasher
import datetime as date
import json
import os
import subprocess

# Pfade definieren
BASE_PATH = r"C:\Users\DanielAecherli\CoreCraftSystems\infra\chain\chainid2025\ares"
BLOCK_PATH = os.path.join(BASE_PATH, "blocks")
MANIFEST_PATH = os.path.join(BASE_PATH, "manifest", "manifest.md")
LICENSE_TYPE = "MIT"
VALIDATOR_SIG = "0xABCDEF1234567890"  # Beispielhafte Signatur

# Hilfsfunktionen
def hash_file(path):
    with open(path, "rb") as f:
        return hasher.sha256(f.read()).hexdigest()

def get_git_commit():
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=BASE_PATH).decode().strip()
        return commit
    except Exception:
        return "unknown"

def save_block(block):
    os.makedirs(BLOCK_PATH, exist_ok=True)
    with open(os.path.join(BLOCK_PATH, f"block_{block.index:03}.json"), "w") as f:
        json.dump(block.__dict__, f, indent=4, default=str)

# Blockklasse
class Block:
    def __init__(self, index, timestamp, data, previous_hash, commit_hash, manifest_hash, license_type, validator_sig):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.commit_hash = commit_hash
        self.manifest_hash = manifest_hash
        self.license_type = license_type
        self.validator_sig = validator_sig
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.commit_hash).encode('utf-8') +
                   str(self.manifest_hash).encode('utf-8') +
                   str(self.license_type).encode('utf-8') +
                   str(self.validator_sig).encode('utf-8'))
        return sha.hexdigest()

# Genesis-Block erzeugen
def create_genesis_block():
    return Block(
        0,
        date.datetime.now(),
        "Genesis Block",
        "0",
        get_git_commit(),
        hash_file(MANIFEST_PATH),
        LICENSE_TYPE,
        VALIDATOR_SIG
    )

# Folgeblöcke erzeugen
def next_block(last_block):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = f"Block {index} – auditierter Eintrag"
    previous_hash = last_block.hash
    return Block(
        index,
        timestamp,
        data,
        previous_hash,
        get_git_commit(),
        hash_file(MANIFEST_PATH),
        LICENSE_TYPE,
        VALIDATOR_SIG
    )

# Chain erzeugen und speichern
def generate_chain(num_blocks=20):
    blockchain = [create_genesis_block()]
    save_block(blockchain[0])
    previous_block = blockchain[0]

    for _ in range(num_blocks):
        block = next_block(previous_block)
        blockchain.append(block)
        save_block(block)
        previous_block = block
        print(f"Block #{block.index} gespeichert – Hash: {block.hash}")

# Ausführung
if __name__ == "__main__":
    generate_chain()