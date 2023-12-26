from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import as_declarative


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id = Column(Integer, autoincrement=True, primary_key=True)


class UserModel(AbstractModel):
    __tablename__ = "users"


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
