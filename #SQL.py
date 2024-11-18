#SQL
from sqlalchemy import create_engine, Table, MetaData

engine = create_engine('sqlite:///books.db')


metadata = MetaData()

book_table = Table('book', metadata, autoload_with=engine)

with engine.connect() as connection:

    result = connection.execute(book_table.select().order_by(book_table.c.title))

    for row in result:
        print(row['title'])
