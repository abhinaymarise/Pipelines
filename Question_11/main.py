from Question_11.src.create import create_database
from Question_11.src.util import mongo_db_connection,collection
from Question_11.src.extract import extract_mongo_data,extract_and_clean
from Question_11.src.transform import transform_un_to_st
from Question_11.src.load import load_into_ssms
import sys

#Executes all the functions at a time {
    #======== DB Creation =============
    #create_database("Mongo_Unstruct_Data")
#}

# The below code is to execute the functions one at a time

if __name__ == '__main__':
    if len(sys.argv)<2:
        sys.exit(1)
    functions=sys.argv[1]

    if functions=='create_database':
        create_database("Mongo_Unstructured_Data")
    elif functions=='mongo_db_connection':
        mongo_db_connection()
    elif functions=='extract_mongo_data':
        extract_mongo_data()
    elif functions=='extract_and_clean':
        extract_and_clean()
    elif functions=='transform_un_to_st':
       transform_un_to_st(collection)
    elif functions=='load_into_ssms':
        load_into_ssms()
    else:
        print('There is no function like that, Recheck the Function Name')
