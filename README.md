# Instrumentation 

Réalisez l'instrumentation d'un applicatif [Python](python).

Ce projet permet d'installer en local une stack complete comprenant:
- opentelemetry collector
- loki ( pour les logs)
- tempo (pour les traces)
- prometheus (pour les metrics)
- Grafana (en backend pour consulter les données)

## Demarrer l'environnement

```bash
docker compose up -d
```

Connecter vous a grafana http://localhost:3000

Une application flask est disponniblepour effectuer des tests http://localhost:8080

## Zero-code

Utilisez l'instrumentation zero-code pour récolter les informations de l'application [Python](python).

## Instrumentation manuelle

Ajoutez de l'instrumentation manuelle pour récolter plus de données sur l'application [Python](python).
