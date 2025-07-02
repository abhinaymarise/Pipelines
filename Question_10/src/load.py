import json
import os
from Question_10.src.util import collection

#============= Load JSON Data into MongoDB ======================== 

file_path=os.path.join(os.path.dirname(__file__),'..','project.txt')

with open(file_path,'r') as data:
    file=json.load(data)

collection.insert_many(file)

for doc in collection.find():
    print(doc)

#============== Load MongoDB Data into SQL Server =================

from Question_10.src.util import ssms_connection

def load_into_ssms(ssms_data_frame):
    engine=ssms_connection()
    try:
        df=ssms_data_frame.to_sql("Mongo_Semi_Data",con=engine,if_exists='replace',index=False)
        print("sent")
    except Exception as e:
        print("work more",e)
    return df

#============= Load the transform data into SQL Server =====================

from Question_10.src.transform import transform
from Question_10.src.util import ssms_connection
import pandas as pd

def load_transform_data_into_sqlserver(data):
    engine=ssms_connection()
    d=list(data)
    df=pd.DataFrame(d)
    df1=df.to_sql("Transform_Mongo_Data",con=engine,if_exists='replace',index=False)
    print("Sent into SQL Server!")
    return df1


    
