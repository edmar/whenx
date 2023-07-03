import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# load environment variables from .env file
load_dotenv()

# get the value of the DATABASE_URL environment variable
database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()
