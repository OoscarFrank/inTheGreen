from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modèle pour stocker les données
class ColorData(BaseModel):
    color: str

# Base de données en mémoire (une seule couleur à la fois)
database: ColorData = None

@app.get("/color", response_model=ColorData)
def get_color_data():
    """Récupère les données de couleur actuellement stockées."""
    if database is None:
        raise HTTPException(status_code=404, detail="No color data found")
    return database

@app.post("/color", response_model=ColorData)
def add_color_data(data: ColorData):
    """Ajoute ou remplace la donnée de couleur dans la base."""
    global database
    database = data
    return data
