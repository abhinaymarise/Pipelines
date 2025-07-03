from Question_10.src.util import collection
import pandas as pd

def extract_data_from_mongodb():
    data=collection.find({},{"_id":0})
    cursor=list(data)
    data_frame=pd.DataFrame(cursor)
    #==== In order to convert the list data into string such that it has to be inserted into SQL Server==============
    for cols in data_frame.columns:
        data_frame[cols]=data_frame[cols].apply(lambda x:','.join(x) if isinstance(x,list) else x)
    return data_frame

