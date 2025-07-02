from Question_10.src.extract import extract_data_from_mongodb
from Question_10.src.util import collection

def transform():
    df=collection.find({},{'project_manager':1,'_id':0})
    return df

