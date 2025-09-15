from fastapi import FastAPI

app = FastAPI()

#lalalalalala
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def testefuncao():
    return{"teste": "deu certo"}


