from fastapi import Depends
from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session

# Database Connection
sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# postgres_url = "postgresql://user:password@localhost:5432/db"
postgres_url = "postgresql://postgres:postgres@localhost:5432/postgres"

# connect_args = {"check_same_thread": False}
engine = create_engine(postgres_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
