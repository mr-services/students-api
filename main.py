from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Mohit"}


@app.get("/about")
def about():
    return "About page"
