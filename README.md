# AeroCast

AeroCast est un package Python qui fournit des informations météorologiques essentielles pour les aéroports du monde entier, y compris les rapports METAR et TAF. Ce module est parfait pour les applications qui nécessitent un accès en temps réel aux conditions météorologiques des aéroports pour les pilotes, les compagnies aériennes, ou les enthousiastes de l'aviation.

## Caractéristiques

- **Récupération des METARs** : Obtenez des rapports météorologiques de surface détaillés pour tout aéroport disposant d'un code ICAO.
- **Interprétation des TAFs** : Prévisions météorologiques sur l'aérodrome pour aider à la planification des vols.
- **Facile à intégrer** : Conçu pour être facilement intégré dans des applications Python existantes.
- **Support multiplateforme** : Compatible avec toutes les plateformes supportées par Python.

## Installation

Vous pouvez installer AeroCast directement via pip depuis PyPI :

```bash
pip install AeroCast
```

## Exemple d'utilisation

Pour obtenir les informations météorologiques de l'aéroport Charles de Gaulle (OACI : CDG), utilisez le code suivant :

```python
from aerocast import WeatherManager

weather_manager = WeatherManager('CDG')

try:
    weather_info = weather_manager.get_weather_info()
    print(weather_info)
except Exception as e:
    print(f"Une erreur est survenue lors de la récupération des données météo : {e}")

```

## Contribuer

Les contributions sont toujours les bienvenues ! Si vous souhaitez contribuer, veuillez forker le dépôt et proposer une pull request.

    aerocast/
    │
    ├── aerocast/                        # Package principal
    │   ├── __init__.py                  # Initialise le package
    │   ├── __main__.py                  # Point d'entrée pour exécution du package
    │   ├── api.py                       # Gestion des appels API
    │   ├── data_manager.py              # Manipulation et gestion des données
    │   ├── tts_manager.py               # Gestion de la conversion texte-voix
    │   ├── weather.py                   # Gestion spécifique des données météo
    │   ├── airport.py                   # Gestion spécifique des données aéroport
    │   └── utils/                       # Sous-package pour les utilitaires
    │       ├── __init__.py              # Initialise le sous-package utils
    │       └── helpers.py               # Fonctions utilitaires
    │
    ├── tests/                           # Tests unitaires et autres tests
    │   ├── __init__.py                  # Initialise le package de tests
    │   ├── test_api.py                  # Tests pour api.py
    │   ├── test_data_manager.py         # Tests pour data_manager.py
    │   ├── test_tts_manager.py          # Tests pour tts_manager.py
    │   ├── test_weather.py              # Tests pour weather.py
    │   └── test_airport.py              # Tests pour airport.py
    │
    ├── docs/                            # Documentation du projet
    │   └── index.md                     # Fichier Markdown pour la documentation de base
    │
    ├── setup.py                         # Script de setup pour le packaging et l'installation
    ├── requirements.txt                 # Dépendances du projet
    ├── README.md                        # Informations générales et guide d'utilisation
    └── LICENSE                          # Fichier de licence

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Projet GitHub : https://github.com/Rbtsv2/AeroCast