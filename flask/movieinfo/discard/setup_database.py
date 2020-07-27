import pandas as pd
from sqlalchemy import create_engine


def setup_db():
    engine = create_engine('sqlite:///movieinfo.sqlite', echo=False)

    movies_forsql = pd.read_csv('./csv/movies_sql.csv', index_col=0)
    movies_forsql.to_sql('movies', con=engine, if_exists='replace',index_label='id')


    people_forsql = pd.read_csv('./csv/people_forsql.csv')
    people_forsql.to_sql('people', con=engine, if_exists='replace',index_label='id')

    
    cast_forsql = pd.read_csv('./csv/cast.csv')
    cast_forsql.to_sql('cast', con=engine, if_exists='replace',index_label='id')
    print("successful setup")

setup_db()