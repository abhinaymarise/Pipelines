from Question_11.src.Config.config import ssms_db_config
import pyodbc
from sqlalchemy import create_engine

#========= Connection Establishment ================
def ssms_connection():
    conn=(
        f"Driver={ssms_db_config['driver']};"
        f"Server={ssms_db_config['server']};"
        f"Database={ssms_db_config['database']};"
        f"UID={ssms_db_config['username']};"
        f"PWD={ssms_db_config['password']};"
        "TrustServerCertificate=Yes;"
    )
    return pyodbc.connect(conn,autocommit=True)

def connect_to_db():
    engine=create_engine("mssql+pyodbc://sa:abcd@DESKTOP-4IVU8N4\\MSSQLSERVER1/Mongo_Unstructured_Data?Driver=ODBC+Driver+17+for+SQL+Server")
    return engine

#======== Connection Establishment with Mongo =======

from Question_10.src.Config.config import mongo_url
from pymongo import MongoClient

def mongo_db_connection():
    url=mongo_url
    return MongoClient(url,serverSelectionTimeoutMS=3000)
client=mongo_db_connection()
db=client['Mongo_Unstructured_Data']
collection=db['Unstruct_Collection']
