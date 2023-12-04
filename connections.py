from sqlalchemy import create_engine, text


# lazy initialization
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'hello world'"))
    # print(result)  # print cursor
    # print(result.all())  # print list
    # print(result.scalar())  # print text
    print(result.scalars().all())  # print list
