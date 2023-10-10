from fastapi import FastAPI, Body
from pydantic import EmailStr
import uvicorn

app = FastAPI()


@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
        "Item3",
    ]


@app.get("/items/latest/")
def get_latest_item():
    return {
        "item": {"id": "0", "name": "latest"},
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.post("/users/")
def create_user(email: EmailStr = Body()):
    return {
        "message": "success",
        "email": email,
    }


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item": {"id": item_id},
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
