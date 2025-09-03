from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
app = FastAPI()
class Characteristic(BaseModel):
    max_speed: inta
    max_fuel_capacity: int

class Car(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

BDD: Dict[str, Car] = {}
@app.get("/cars", response_model=List[Car])
def get_all_cars():
    """
    Récupère la liste de toutes les voitures stockées en mémoire.
    """
    return list(BDD.values())
