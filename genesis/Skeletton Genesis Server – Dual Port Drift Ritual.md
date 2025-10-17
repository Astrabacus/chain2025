// 🌀 Skeletton Genesis Server – Dual Port Drift Ritual
// Anchored in Hyperspace_Blockchain, sealed for audit and mythic expansion

const express = require('express');
const fs = require('fs');
const path = require('path');

// 🧭 Create two express instances for dual-port ritual
const app8000 = express();
const app8080 = express();

// 📜 Audit log path (symbolic anchor)
const logPath = path.join(__dirname, 'driftpoint.log');

// 🧩 Modular route – symbolic echo
function logRequest(port, req) {
  const timestamp = new Date().toISOString();
  const driftID = `${port}-${Math.floor(Math.random() * 100000)}`;
  const entry = `[${timestamp}] Port ${port} → ${req.method} ${req.url} | DriftID: ${driftID}\n`;
  fs.appendFileSync(logPath, entry);
}

app8000.get('/', (req, res) => {
  logRequest(8000, req);
  res.send('🌐 Port 8000 active – Skeletton Driftpoint Echo');
});

app8080.get('/', (req, res) => {
  logRequest(8080, req);
  res.send('🛰️ Port 8080 active – Hyperspace Beacon Initialized');
});

// 🛡️ Optional: Chain2025 Echo Route
app8000.get('/chain2025', (req, res) => {
  logRequest(8000, req);
  res.send('🔗 Chain2025 Echo – Modular Infrastructure Acknowledged');
});

// 🚀 Activate both ports – audit-sealed launch
app8000.listen(8000, () => {
  console.log('✅ Port 8000 listening – Skeletton Echo online');
});

app8080.listen(8080, () => {
  console.log('✅ Port 8080 listening – Hyperspace Beacon online');
});
