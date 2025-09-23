const { Web3 } = require("web3");
const web3 = new Web3();

// Ersetze durch deinen echten Private Key
const account = web3.eth.accounts.privateKeyToAccount("0x4f3c2e1d9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d");

console.log("✅ Adresse:", account.address);
console.log("🔐 Public Key:", account.publicKey);
console.log("🧾 Private Key:", account.privateKey);