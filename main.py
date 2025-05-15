from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Convertisseur FCFA → EUR (taux fixe)")

# --- Taux fixe officiel ---
FCFA_TO_EUR_RATE = 1 / 655.957  # ~0.00152449

# --- Modèle de réponse ---
class ConversionResponse(BaseModel):
    fcfa: float
    eur: float
    rate: float

# --- Endpoint de conversion ---
@app.get("/convert-fcfa", response_model=ConversionResponse)
def convert_fcfa(amount: float = Query(..., gt=0, description="Montant en FCFA")):
    eur = round(amount * FCFA_TO_EUR_RATE, 4)
    return ConversionResponse(
        fcfa=amount,
        eur=eur,
        rate=round(FCFA_TO_EUR_RATE, 6)
    )

# --- Page d’accueil ---
@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API de conversion FCFA → EUR (taux fixe 1 EUR = 655.957 FCFA)"}
