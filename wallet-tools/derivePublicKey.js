// 📄 Datei: derivePublicKey.js
const ethUtil = require("ethereumjs-util");

const privateKeyHex = "4f3c2e1d9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d"; // z. B. "4f3c2e..."
const privateKey = Buffer.from(privateKeyHex, "hex");

const publicKey = ethUtil.privateToPublic(privateKey);
const address = ethUtil.publicToAddress(publicKey);

console.log("🔐 Public Key:", "0x" + publicKey.toString("hex"));
console.log("✅ Adresse:", "0x" + address.toString("hex"));