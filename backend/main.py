
from fastapi import FastAPI
from backend.db import SessionLocal,Todo
app=FastAPI()

@app.get("/todos")
def get_all():
    db=SessionLocal()
    return db.query(Todo).all()

@app.post("/todos")
def add(title:str):
    db=SessionLocal()
    t=Todo(title=title); db.add(t); db.commit()
    return {"ok":True}
