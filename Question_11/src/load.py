#======= Load Unstructed Data Into Mongo_DB=======
import os
import json
from Question_11.src.util import collection

file_path=os.path.join(os.path.dirname(__file__),'..','Doc_unstructured_1.txt')
with open(file_path,'r') as data:
    file=json.load(data)
collection.insert_many(file)

#==== To check what kind of data is present ======
#for doc in collection.find():
    #print(doc)


# ============ Load the transform data into SSMS =======

from Question_11.src.extract import extract_and_clean
from Question_11.src.util import connect_to_db

def load_into_ssms():
    data=extract_and_clean()
    engine=connect_to_db()
    df=data.to_sql("Structured_Data",con=engine,if_exists='replace',index=False)
    print("Sucessfully sent into SQL Server!")
    return df