from Question_11.src.util import mongo_db_connection,collection
from Question_11.src.transform import transform_un_to_st
import pandas as pd

def extract_mongo_data():
    data=collection.find({},{'_id':0})
    #cursor=list(data)
    #df=pd.DataFrame(cursor)
    for doc in data:
        print(doc)

def extract_and_clean():
    data=collection.find()
    cleaned_data=[]
    for doc in data:
        clean_doc=transform_un_to_st(doc)
        cleaned_data.append(clean_doc)
    df=pd.DataFrame(cleaned_data)
    return df