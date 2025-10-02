# block.py
import hashlib as hasher
import datetime as date

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