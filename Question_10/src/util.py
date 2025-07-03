#============== MongoDB Connection =========================

from pymongo import MongoClient
from Question_10.src.Config.config import mongo_url

def connect_to_mongo():
    url=mongo_url
    return MongoClient(url,serverSelectionTimeoutMS=3000)

client=connect_to_mongo()
db=client['Pipelines']
collection=db['Project']

#=============== SQL Server Connection =========================

from sqlalchemy import create_engine
from Question_10.src.Config.config import ssms_db_config,ssms_url

def ssms_connection():
    #db = ssms_db_config
    #conn = f"{db['dialect']}://{db['username']}:{db['password']}@{db['server']}/{db['database']}?driver={db['driver']}"
    conn=create_engine(ssms_url)
    return conn

engine=ssms_connection()
with engine.connect():
    print("database created!")

