from Question_7.src.Config.config import ms_connection_url,mysql_db_config
from sqlalchemy import create_engine
import pandas as pd

#=============== SQL Server Connection =====================
def get_engine():
   # conn=f"{db['dialect']}'://{db['username']}:{db['password']}@{db['server']}/{db['Database']}?{db['Driver']}"
    con=create_engine(ms_connection_url)
    return con

#get_engine()
#try:
#    with get_engine().connect():
#        print("Connected")
#except Exception as e:
#    print("not connected",e)

#================ MYSQL Server Connection ==============
def mysql_get_engine():
    db=mysql_db_config
    conn=f"mysql+mysqlconnector://{db['username']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    con=create_engine(conn)
    return con

#try:
#    engine=mysql_get_engine()
#    with engine.connect():
#        print("Connected To Mysql")
#except Exception as e:
#    print("Bro, Too close work more on it")


