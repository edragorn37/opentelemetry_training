# Instrumentation 

Réalisez l'instrumentation d'un applicatif [Python](python).

Ce projet permet d'installer en local une stack complete comprenant:
- opentelemetry collector
- loki ( pour les logs)
- tempo (pour les traces)
- prometheus (pour les metrics)
- Grafana (en backend pour consulter les données)

Le dossier tempo provient du git grafana tempo et, est importé dans le projet afin de faciliter l'installation

## Demarrer l'environnement

```bash
docker compose up -d
```

Connecter vous a grafana http://localhost:3000

## Zero-code

Utilisez l'instrumentation zero-code pour récolter les informations de l'application [Python](python).

## Instrumentation manuelle

Ajoutez de l'instrumentation manuelle pour récolter plus de données sur l'application [Python](python).
