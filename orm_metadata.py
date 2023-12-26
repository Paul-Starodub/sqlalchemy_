from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import as_declarative, declared_attr


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id = Column(Integer, autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = "users"
    name = Column(String(30))
    full_name = Column(String)


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
    email = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))


print(UserModel.__tablename__)
print(AddressModel.__tablename__)
