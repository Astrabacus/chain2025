import hashlib

def generate_audit_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            sha256.update(block)
    return sha256.hexdigest()

if __name__ == "__main__":
    path = "withdrawal_log.yaml"
    hash_value = generate_audit_hash(path)
    print("🔐 Audit-Hash:", hash_value)