#=========== Calling the extract function ===================

from Question_10.src.extract import extract_data_from_mongodb
received_data=extract_data_from_mongodb()

#=========== Establish the SSMS Connection ======================

from Question_10.src.util import ssms_connection
ssms_connection()

#============== Load the MongoDB data into SSMS ================== 

from Question_10.src.load import load_into_ssms
load_into_ssms(received_data)

#============= Calling the transform function ===============

from Question_10.src.transform import transform
data=transform()

#============= Calling the load function ================

from Question_10.src.load import load_transform_data_into_sqlserver
load_transform_data_into_sqlserver(data)