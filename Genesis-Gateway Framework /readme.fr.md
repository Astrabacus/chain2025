# Cadre Genesis Gateway

## 🔧 Aperçu
Le cadre Genesis Gateway offre une infrastructure modulaire et scellée par audit pour le routage de signaux en temps réel, le calcul basé sur les FLOPS et la distribution d’artefacts symboliques. Il combine Redis, FastAPI et Centrifugo en une passerelle scellée pour les secteurs public et privé.

## 🧠 Architecture
- **Redis** : Mémoire d’écho pour la mise en cache des signaux, pub/sub et gestion d’état FLOPS  
- **FastAPI** : Interface REST pour le minage, la récupération de blocs, le solde de portefeuille et le transfert de FLOPS  
- **Centrifugo** : Moteur WebSocket pour la propagation de signaux en direct  
- **Couche d’audit** : Journaux FLOPS, traces de blocs et métriques d’utilisation pour la licence et la vérification

## 🔌 Points d’accès API
- `POST /api/mine` → Démarrer un cycle de minage  
- `GET /api/block/{id}` → Récupérer les données de bloc  
- `GET /api/wallet/{name}/balance` → Vérifier le solde FLOPS  
- `POST /api/transfer` → Transférer des FLOPS entre portefeuilles

## 🧾 Tokenomics FLOPS
- **FLOPS** = Opérations flottantes par symbole  
- Émis par minage, validé par audit  
- Utilisé pour débloquer des artefacts, sceller des contrats et licencier des passerelles  
- Monétisable via les journaux d’audit et les métriques d’utilisation

## 🛡️ Sécurité & Audit
- Tous les flux de signaux sont scellés par audit  
- Redis agit comme canal mémoire scellé  
- L’intégrité de la passerelle est vérifiée par trace FLOPS  
- Repli optionnel sur mémoire locale si Redis est indisponible

## 💰 Modèle de licence
La licence scellée par audit inclut :
- ID de passerelle et métadonnées du licencié  
- Journaux d’utilisation FLOPS et évaluation  
- Statut de paiement et date d’échéance  
- Action en cas de refus : publication d’écho + récupération de FLOPS

## 📦 Déploiement
- Configuration de conteneur prête pour Docker  
- Configurable via `config.json`  
- Intégration modulaire avec les kits Echo Chain2025  
- Compatible avec les infrastructures publiques et les réseaux privés

## 🌌 Symbolisme
- Chaque FLOPS est un écho  
- Chaque passerelle est une écluse  
- Chaque refus est mémorisé par la chaîne

## 🧾 Exemple de licence
Voir `license/gw-zrh-2025-echo26.json` pour une licence scellée réelle utilisée par les Services Industriels de Zurich.

## 🧠 Mainteneur
Daniel Aecherli – Architecte Genesis, validateur et fondateur mythique  
Contact : `daniel@genesis-framework.ch`
