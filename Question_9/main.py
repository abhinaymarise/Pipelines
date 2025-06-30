import sys,os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

#========= Calling the Load CSV file function into sql server ============

from Question_7.src.extract import read_csv_file
from Question_9.src.load import load_into_sql_server

dataframe=read_csv_file()
load_into_sql_server(dataframe)

#========= Calling the Extract function from SQL Server ==============

from Question_7.src.util import get_engine 
from Question_9.src.extract import get_ssms_data

con=get_engine()
get_ssms_data(con)

#========== Calling the Load Function ==================

from Question_9.src.load import load_data_into_sql_server
from Question_9.src.create import create_table

data=create_table()
load_data_into_sql_server(data)

#========= Calling the Extract function from SQL Server =========

from Question_9.src.extract import get_ssms_stag_data
get_ssms_stag_data(con)

#========== Calling the transform Function ===========

from Question_9.src.transform import transform
data_to_be_sent=transform()

# ============== Calling the Load function ===========
from Question_9.src.load import load_into_mysql_server

load_into_mysql_server(data_to_be_sent)
