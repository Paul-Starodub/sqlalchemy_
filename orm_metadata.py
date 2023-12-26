from sqlalchemy import create_engine, String, ForeignKey, BigInteger
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = "users"
    user_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()  # new syntax (mapped_column)
    full_name: Mapped[str] = mapped_column()


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
    email = mapped_column(String, nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))
