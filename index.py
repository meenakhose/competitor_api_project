from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime
import json

app = FastAPI(title="Competitor Analysis API")

class Competitor(BaseModel):
    id: int
    name: str
    ads_count: int
    reviews: int
    rating: float
    updated_at: datetime

with open("competitors.json", "r") as f:
    data = json.load(f)
    competitors_db = [Competitor(**comp) for comp in data["competitor_related"]]

@app.get("/")
def root():
    return {"message": "Competitor Analysis API is running"}

@app.get("/competitors", response_model=List[Competitor])
def get_competitors():
    return competitors_db

@app.get("/competitor/{comp_id}", response_model=Competitor)
def get_competitor(comp_id: int):
    for comp in competitors_db:
        if comp.id == comp_id:
            return comp
    return {"error": "Competitor not found"}
