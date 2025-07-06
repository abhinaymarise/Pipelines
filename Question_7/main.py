from Question_7.src.util import mysql_get_engine
from Question_7.src.extract import export_from_sql
from Question_7.src.transform import transform_orderby,transform_where,transform_agg
from Question_7.src.load import load_data_into_sql_server

#============= Extracting from MySql ==================

con=mysql_get_engine()
df=export_from_sql(con)

#============= Calling tranform file ==================

transform_orderby(df)
transform_where(df)
cleaned_data=transform_agg(df)

#============ Loading into SSMS ========================
load_data_into_sql_server(cleaned_data)