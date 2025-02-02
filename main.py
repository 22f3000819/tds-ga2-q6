from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get('/api')
def getmarks(name: List[str] = Query(default=[])):
    lom = []
    with open('q-vercel-python.json', "r") as json_file:
        data = json.load(json_file)
        for n in name:
            print(n)
            for entity in data:
                if n == entity['name']:
                    lom.append(entity['marks'])
                    break
    return {
        "marks": lom
    }


@app.get('/')
def check():
    return {
        "message": 'Request Successful'
    }, 200