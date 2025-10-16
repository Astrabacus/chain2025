
---

## ⚙️ 2. CLI-Skript: Automatische Generierung aus Node-Tracker & Bewegungsdaten

```bash
#!/bin/bash

# CLI: generate_echo_kit.sh
# Beschreibung: Extrahiert Node-Metadaten via Etherscan API und koppelt sie mit lokalem Bewegungslog

# API-Schlüssel & Endpunkte
ETHERSCAN_API_KEY="your_api_key_here"
NODE_IP="192.0.2.1"
MOVEMENT_LOG="movement.jsonl"

# 1. Node-Metadaten abrufen
NODE_DATA=$(curl -s "https://api.etherscan.io/api?module=stats&action=nodecount&apikey=$ETHERSCAN_API_KEY")

# 2. Bewegungsdaten extrahieren (letzter Eintrag)
MOVEMENT_ENTRY=$(tail -n 1 $MOVEMENT_LOG)

# 3. Markdown generieren
echo "# Echo-Kit: Planetarer Driftpunkt" > echo_kit.md
echo "## Node-Metadaten" >> echo_kit.md
echo "$NODE_DATA" | jq '.result' >> echo_kit.md
echo "## Bewegungsritual" >> echo_kit.md
echo "$MOVEMENT_ENTRY" | jq '.' >> echo_kit.md
echo "## Audit-Verknüpfung" >> echo_kit.md
echo "- SHA-256: $(sha256sum echo26_driftpoint.png | cut -d ' ' -f1)" >> echo_kit.md

echo "✅ Echo-Kit erfolgreich generiert: echo_kit.md"
