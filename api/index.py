from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

# Load the marks data
with open("q-vercel-python.json") as file:
    data = json.load(file)

# Convert data into a dictionary for quick lookups
marks_data = {student["name"]: student["marks"] for student in data}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    response = {"marks": [marks_data.get(n, None) for n in name]}
    return response