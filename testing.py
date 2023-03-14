from datetime import datetime
import sqlalchemy
from models import Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

heroku_secrets = {'host': 'ec2-52-1-104-110.compute-1.amazonaws.com',
                  'database': 'd1649qlkq0m529',
                  'user': 'uru6ce975o54d',
                  'password': 'p038b4a22e1aea86c2c34a21aa0117b1e15a38d923a450bba039a548db26fdb8b'}
engine = create_engine(f'postgresql://{heroku_secrets["user"]}:{heroku_secrets["password"]}@{heroku_secrets["host"]}/{heroku_secrets["database"]}')

session = Session(bind=engine)
table = sqlalchemy.Table('full_options_tqqq', Base.metadata, autoload_with=engine)
query = table.select()
data = session.execute(query).fetchall()
session.close()
