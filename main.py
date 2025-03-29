from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List
import pandas as pd
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get('/api/ga2q6')
def getmarks(name: List[str] = Query(default=[])):
    data = {
        "name": name
    }
    response = requests.post('http://localhost:8000/api/p2ga2q6', json=data)
    return response.json()

@app.get("/api/ga2q10")
def get_students(class_: list[str] = Query(None, alias="class")):
    """
    Fetch student data from the CSV. If 'class' query parameters are provided,
    filter students by those classes.
    """
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    # Convert to dictionary list
    students = filtered_df.to_dict(orient="records")
    return {"students": students}

@app.get('/')
def check():
    return {
        "message": 'Request Successful'
    }, 200