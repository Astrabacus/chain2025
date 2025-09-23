const { Web3 } = require("web3");
const fs = require("fs");

const web3 = new Web3();

// Async-Funktion für Keystore-Erzeugung
async function generateKeystore() {
  const privateKey = "0x4f3c2e1d9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d"; // z. B. "0x4f3c2e..."
  const password = "Smilen$1984";

  console.log("🔍 Private Key:", privateKey);

  const account = web3.eth.accounts.privateKeyToAccount(privateKey);
  const keystore = await web3.eth.accounts.encrypt(account.privateKey, password);

  console.log("📦 Keystore Inhalt:", keystore);

  fs.writeFileSync("keystore.json", JSON.stringify(keystore, null, 2));
  console.log("✅ Keystore gespeichert als keystore.json");
}

// Funktion ausführen
generateKeystore();
