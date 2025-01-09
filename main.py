from fastapi import FastAPI
from sqlmodel import select
from db import create_db_and_tables, SessionDep
from models import Product, Employee

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()



@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with SQLModel"}


@app.get("/products/")
def get_products(session: SessionDep):
    products = session.exec(select(Product)).all()
    return products

@app.post("/products/")
def create_product(product: Product, session: SessionDep) -> Product:
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.get("/products/{product_id}")
def get_product(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    return product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, session: SessionDep):
    statement = select(Product).where(Product.id == product_id)
    results = session.exec(statement)
    session.commit()
    session.refresh(results)
    return {"message": f"Product {product_id} deleted successfully."}











