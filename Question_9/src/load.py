import pandas as pd
from Question_7.src.util import get_engine
from Question_9.src.create import create_table

# =========== Loading the data into SQL Server ===================

def load_into_sql_server(dataframe):
    engine=get_engine()
    try:
        df=dataframe.to_sql("Orders",con=engine,if_exists='replace',index=False)
        # print("Data sent into Sql Server")
    except Exception as e:
        e
        # print("Work Hard Bro, it will connect")

# =========== Load the Stag_Data into SQL Server ==================

data=create_table()
def load_data_into_sql_server(data):
    engine=get_engine()
    try:
        df=data.to_sql("Stag_Order_Data",con=engine,if_exists='replace',index=False)
        #print("Stag Data sent into SQL Server")
    except Exception as e:
        #print("Work more on Stag Data") 
        e

#=========== Load it into the MySql Server =================

from Question_7.src.util import mysql_get_engine

def load_into_mysql_server(data):
    engine=mysql_get_engine()
    try:
        df=data.to_sql("SCD2_Orders_Table",con=engine,if_exists='replace',index=False)
        print("Sent safely into mysql")
    except Exception as e:
        print("Work more you will make it",e)
    