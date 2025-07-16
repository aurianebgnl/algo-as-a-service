from fastapi import FastAPI
from pydantic import BaseModel #classe spéciale, pour définir le format des données que l’API accepte (validation automatique).
from typing import List
from sorting import bubble_sort

#création d'une instance de l'application FastAPI
app = FastAPI()

# création d'une classe qui décrit ce qu'on attend dans une requête
class SortRequest(BaseModel):
    sort_order: str  # "asc" ou "desc"
    values: List[int]

# Route HTTP : quand le serveur reçoit une requête POST à l’URL /sort,
# il exécute la fonction juste en dessous
@app.post("/sort")
def sort_numbers(request: SortRequest):
    ascending = request.sort_order.lower() == "asc"
    sorted_values = bubble_sort(request.values, ascending=ascending)
    return {"sorted": sorted_values}
