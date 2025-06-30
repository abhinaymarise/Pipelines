import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from Question_7.src.util import mysql_get_engine
from Question_8.src.extract import extract_data
from Question_8.src.transform import transform_orders
from Question_8.src.load import load_orderby_data

#============= Extracting data from MySql ==================

con=mysql_get_engine()
data=extract_data(con)

#============ Calling Transform Function ===================

clean_data=transform_orders(data)

#============ Calling Load Function ===================

load_orderby_data(clean_data)


