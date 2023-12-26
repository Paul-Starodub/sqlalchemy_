from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id = mapped_column(Integer, autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = "users"
    name = mapped_column(String(30))
    full_name = mapped_column(String)


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
    email = mapped_column(String, nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))


print(UserModel.__tablename__)
print(AddressModel.__tablename__)
