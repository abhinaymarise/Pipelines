import pandas as pd
from Question_7.src.util import mysql_get_engine

#------Extracted from CSV--------------

def read_csv_file():
    df=pd.read_csv(r"C:\Users\Abhinay\Documents\ETL\Pipelines\Question_7\order_data 1.csv")
    return df

df1=read_csv_file()
#print(df1)

#===== Extracted from MYSQL ==============

def export_from_sql(connection):
    df=pd.read_sql("Select * from orders",connection)
    return df


