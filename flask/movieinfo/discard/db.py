import sqlalchemy as db

engine = db.create_engine('sqlite:///movieinfo.sqlite')
connection = engine.connect()
metadata = db.MetaData()

movies = db.Table('movies', metadata, autoload=True, autoload_with=engine)
people = db.Table('people', metadata, autoload=True, autoload_with=engine)

print(movies.columns.keys())
print(people.columns.keys())

query = db.select([people]).where(people.columns.gender==1)
result = connection.execute(query).fetchall()
print(result[:10])