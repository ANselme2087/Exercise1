# Convertisseur FCFA → EUR (taux fixe)

## Description
Ce projet est une API développée avec FastAPI qui permet de convertir un montant en FCFA (Franc CFA) en EUR (Euro) en utilisant un taux de conversion fixe. Le taux utilisé est le taux officiel : **1 EUR = 655.957 FCFA**.

## Fonctionnalités
- **Endpoint `/convert-fcfa`** : Permet de convertir un montant donné en FCFA en EUR.
  - **Paramètre** : `amount` (float, obligatoire, doit être supérieur à 0) - Montant en FCFA à convertir.
  - **Réponse** :
    ```json
    {
        "fcfa": <montant en FCFA>,
        "eur": <montant converti en EUR>,
        "rate": <taux de conversion>
    }
    ```
- **Endpoint `/`** : Page d'accueil de l'API avec un message de bienvenue.

## Installation
1. Clonez ce dépôt ou copiez les fichiers dans un répertoire local.
2. Assurez-vous d'avoir Python 3.10 ou une version ultérieure installée.
3. Créez un environnement virtuel et activez-le :
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Installez les dépendances nécessaires :
   ```powershell
   pip install -r requirements.txt
   ```

## Lancement de l'API
1. Assurez-vous que l'environnement virtuel est activé.
2. Lancez le serveur FastAPI avec la commande suivante :
   ```powershell
   uvicorn main:app --reload
   ```
3. Accédez à l'API via votre navigateur ou un outil comme Postman :
   - Documentation interactive : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Page d'accueil : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Exemple d'utilisation
### Requête
```http
GET /convert-fcfa?amount=1000 HTTP/1.1
Host: 127.0.0.1:8000
```

### Réponse
```json
{
    "fcfa": 1000,
    "eur": 1.5245,
    "rate": 0.001524
}
```

## Dépendances
- **FastAPI** : Framework pour construire l'API.
- **Pydantic** : Validation des données et création de modèles.
- **Uvicorn** : Serveur ASGI pour exécuter l'API.

## Auteur
Ce projet a été réalisé par Anselme KABRAN.
