from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Expenses(BaseModel):
    expense_type: str
    amount: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add_employee")
def add_new_employee(employee_name):
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, expense: Expenses):
    return {"expense_amount": expense.amount, "item_id": item_id}