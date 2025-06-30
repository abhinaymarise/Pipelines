import pandas as pd
from Question_7.src.util import mysql_get_engine

#============ Extract from MySql Server =================

def extract_data(connection):
    df=pd.read_sql("Select * from Orders",connection)
    return df
