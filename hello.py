from fastapi import FastAPI

app = FastAPI()

@app.get('/api')
def main():
    return {
        "message": 'Request Successful'
    }, 200