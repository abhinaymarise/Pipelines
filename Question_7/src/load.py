from Question_7.src.extract import df1
from Question_7.src.util import mysql_get_engine, get_engine
from Question_7.src.transform import transform_agg

#-----------Loaded into MySql-----------

def load_data():
    engine=mysql_get_engine()
    try:
        data_frame=df1.to_sql("Orders",con=engine,if_exists='replace',index=False)
        print("Sent into MySql")
    except Exception as e:
        print("Work Hard,Come on you wil do it ")

if __name__=="__main__":
    load_data()


#-----------Load into Sql Server=========

def load_data_into_sql_server(agg_df):
    engine=get_engine()
    try:
        df=agg_df.to_sql("Aggregated_Amount",con=engine,if_exists='replace',index=False)
        print("Successfully sent into ssms!")
    except Exception as e:
        print("Exception occurs",e)