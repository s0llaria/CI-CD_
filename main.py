from random import random

from fastapi import FastAPI

app = FastAPI()

#lalalalalala
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def testefuncao():

    return {"teste": True, "num_aleatoerio": random.randint(0, 1000)}
main

