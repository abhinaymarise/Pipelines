import pandas as pd
from Question_7.src.extract import export_from_sql 

#========= Order by =============

def transform_orderby(dataframe):
    orderby_df=dataframe.sort_values(["order_date"])
    return orderby_df

#========  Where =============

def transform_where(dataframe):
    df=dataframe[dataframe["order_status"]=="Pending"]
    return df

#======== Aggregation ===========

def transform_agg(dataframe):
    agg_df=(dataframe.groupby("customer_id",as_index=False)
    .agg(total_amount=("order_amount","sum"),total_count=("order_id","count")))
    return agg_df