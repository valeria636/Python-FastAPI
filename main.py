from fastapi import FastAPI, HTTPException
import json
import os

# Nom del fitxer JSON
FITXER_JSON = "alumnes.json"

# Carregar alumnes del fitxer JSON
def carregar_alumnes():
    if not os.path.exists(FITXER_JSON):
        return []
    with open(FITXER_JSON, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Desar alumnes al fitxer JSON
def desar_alumnes(alumnes):
    with open(FITXER_JSON, "w", encoding="utf-8") as file:
        json.dump(alumnes, file, indent=4, ensure_ascii=False)

# Obtenir el següent ID disponible
def obtenir_seguent_id(alumnes):
    return max((alumne["id"] for alumne in alumnes), default=0) + 1

# Inicialitzar FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Institut TIC de Barcelona"}

@app.get("/alumnes/")
def get_total_alumnes():
    alumnes = carregar_alumnes()
    return {"total_alumnes": len(alumnes)}

@app.get("/id/{alumne_id}")
def get_alumne(alumne_id: int):
    alumnes = carregar_alumnes()
    alumne = next((a for a in alumnes if a["id"] == alumne_id), None)
    if not alumne:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

@app.delete("/del/{alumne_id}")
def delete_alumne(alumne_id: int):
    alumnes = carregar_alumnes()
    alumnes_nou = [a for a in alumnes if a["id"] != alumne_id]
    if len(alumnes) == len(alumnes_nou):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    desar_alumnes(alumnes_nou)
    return {"message": "Alumne eliminat"}

@app.post("/alumne/")
def add_alumne(alumne: dict):
    alumnes = carregar_alumnes()
    alumne["id"] = obtenir_seguent_id(alumnes)
    alumnes.append(alumne)
    desar_alumnes(alumnes)
    return {"message": "Alumne afegit", "alumne": alumne}
