from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from backend.interact_db import get_session, Employee, Expenses
from sqlalchemy.orm import Session


app = FastAPI()

class ExpensesCreate(BaseModel):
    expense_type: str
    amount: float
    employee_id: int

class EmployeeData(BaseModel):
    employee_name: str
    employee_email: str

class EmployeeResponse(BaseModel):
    id: int

@app.post("/add_employee/", response_model=EmployeeResponse)
def add_new_employee(employee: EmployeeData, session: Session = Depends(get_session)):
    employee_db = Employee(**employee.model_dump())   
    # employee is an instance of EmployeeData, which is a Pydantic model. employee.model_dump() allows easier mapping conversion from a Pydantic model to a SQLAlchemy model (Exployee)
    session.add(employee_db)
    session.commit()
    session.refresh(employee_db)
    return employee_db
   
@app.get("/employee_expenses/{employee_id}")
def get_employee_expenses(employee_id: int, session: Session = Depends(get_session)):
    employee_expenses = session.query(Expenses).filter(Expenses.employee_id== employee_id).all()
    return employee_expenses

@app.get("/all_expenses/")
def get_all_expenses(session: Session = Depends(get_session)):
    expenses= session.query(Expenses).all()
    return expenses 

@app.post("/add_expense/")
def add_expense(expense: ExpensesCreate, session: Session = Depends(get_session)):
    expense_db = Expenses(**expense.model_dump())
    session.add(expense_db)
    session.commit()
    session.refresh(expense_db)
    return expense

@app.get("/all_employees/")
def get_all_expenses(session: Session = Depends(get_session)):
    employee_data= session.query(Employee).all()
    return employee_data 