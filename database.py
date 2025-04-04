from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

# username = env['USER']
# password = env['PASSWORD']
# db_name = env['NAME']
# host = env['HOST']
# port = env['PORT']

# DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
DATABASE_URL = "mysql+pymysql://root:rootroot@localhost:3306/aicert"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

