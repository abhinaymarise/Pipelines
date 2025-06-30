import pandas as pd
from Question_7.src.util import get_engine

# ========= Extract the Existing data from SQL Server ==============

def get_ssms_data(con):
    df=pd.read_sql("Select * from Orders",con)
    return df

# ========= Extract the Exisiting Stag_Data from SQL Server =========

def get_ssms_stag_data(con):
    df=pd.read_sql("Select * from Stag_Order_Data",con)
    return df
