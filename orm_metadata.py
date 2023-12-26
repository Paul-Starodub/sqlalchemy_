from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import registry, declarative_base


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
mapper_registry = registry()  # looks like metadata
# Base = mapper_registry.generate_base()  # old style
Base = declarative_base()


class AbstractModel(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)


class UserModel(AbstractModel):
    pass


class AddressModel(AbstractModel):
    pass
