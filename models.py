from typing import Optional
from sqlmodel import SQLModel, Field

# Model definition
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    brand: Optional[str] = Field(default="N/A")
    price: float = Field(max_digits=9, decimal_places=2)


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field()
    department: str = Field()
    salary: float = Field(max_digits=9, decimal_places=2)