from fastapi import FastAPI
from manager import analysis


app = FastAPI()

@app.get("/")
def get_results():
    js = analysis()
    return js