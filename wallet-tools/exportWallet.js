const { Web3 } = require("web3");
const fs = require("fs");
const yaml = require("js-yaml");

const web3 = new Web3();

async function exportWallet() {
  const privateKey = "0x4f3c2e1d9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d"; // mit "0x"
  const password = "Smilen$1984";

  const account = web3.eth.accounts.privateKeyToAccount(privateKey);
  const keystore = await web3.eth.accounts.encrypt(account.privateKey, password);

  const walletYaml = {
    wallet: {
      address: account.address,
      public_key: account.publicKey || "🔍 nicht direkt verfügbar in Web3 v4",
      private_key: privateKey,
      keystore: keystore,
      role: "genesis_initiator",
      symbolic_phase: "🜃 Earth of Origin"
    }
  };

  const walletMarkdown = `
# 🧾 Wallet Export Audit

- **Adresse**: ${account.address}  
- **Private Key**: ${privateKey}  
- **Keystore**: AES-verschlüsselt  
- **Rolle**: Genesis-Initiator  
- **Symbolische Phase**: 🜃 Earth of Origin
`;

  fs.writeFileSync("wallet.yaml", yaml.dump(walletYaml));
  fs.writeFileSync("wallet.json", JSON.stringify(walletYaml, null, 2));
  fs.writeFileSync("wallet_audit.md", walletMarkdown);

  console.log("✅ wallet.yaml, wallet.json und wallet_audit.md wurden erstellt.");
}

exportWallet();