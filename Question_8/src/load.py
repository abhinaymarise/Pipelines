import pandas as pd
from Question_8.src.transform import transform_orders
from Question_7.src.util import get_engine


def load_orderby_data(orderby_df):
    engine=get_engine()
    try:
        df=orderby_df.to_sql("OrderBy_Data",con=engine,if_exists='replace',index=False)
        print("Sent into SSMS")
    except Exception as e:
        print("Not yet sent")


