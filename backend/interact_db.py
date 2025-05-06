from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, mapped_column, relationship, Session
import datetime

DATABASE_URL = "sqlite:///expenses_database.db"  # Change to PostgreSQL later
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Employee(Base):
    __tablename__  = "employee_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(String, nullable=False)
    employee_email = Column(String, nullable=False)

class Expenses(Base):
    __tablename__  = "expenses_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee_table.id"))
    amount = Column(Integer, nullable= False)
    expense_type = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

