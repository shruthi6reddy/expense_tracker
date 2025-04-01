from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
import datetime


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(String, nullable=False)


class Expenses(Base):
    __tablename__ = "expenses_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee_table.id"))
    amount = Column(Integer, nullable= False)
    expense_type = Column(String, nullable=False)
    created_time = Column(DateTime, default=datetime.datetime.now)

# we could keep an expense type table for normalization