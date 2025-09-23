const fs = require("fs");

const audit = `
# 🧾 Genesis Wallet Audit

- **Adresse**: 0xDEINE_ADRESSE  
- **Private Key**: 0xDEIN_PRIVATE_KEY  
- **Public Key**: 0xDEIN_PUBLIC_KEY  
- **Genesis Block**: 0  
- **Rolle**: Genesis-Initiator  
- **Symbolische Phase**: 🜃 Earth of Origin

> Dieser Schlüssel wurde manuell validiert und entspricht dem Ursprung der ChainID 2025.
`;

fs.writeFileSync("wallet_audit.md", audit);
console.log("📜 wallet_audit.md wurde erstellt.");