import pandas as pd
from Question_9.src.extract import get_ssms_data,get_ssms_stag_data
from Question_7.src.util import get_engine
from datetime import timedelta

safe_end_date='Null'
con=get_engine()

def transform():
    new_rows=[]
    d1=get_ssms_data(con)
    d2=get_ssms_stag_data(con)

    d1['order_date']=pd.to_datetime(d1["order_date"],errors="coerce")
    d2['order_date']=pd.to_datetime(d2["order_date"],errors="coerce")

    if 'order_end_date' not in d1.columns:
        d1['order_end_date']=pd.NaT
    if 'Active_Flag' not in d1.columns:
        d1['Active_Flag']='Yes'

    for index, rows in d2.iterrows():
        orderid=rows['order_id']
        customerid=rows['customer_id']
        orderdate=rows['order_date']
        orderamount=rows['order_amount']
        orderstatus=rows['order_status']
        productcategory=rows['product_category']

        mark=d1[(d1['customer_id']==customerid) & (d1['Active_Flag']=='Yes')]

        if not mark.empty:
            current_order_status=mark.iloc[0]['order_status']
            if current_order_status!=orderstatus:
                d1.loc[mark.index,'order_end_date']=orderdate-timedelta(days=1)
                d1.loc[mark.index,'Active_Flag']='No'

                new_data={
                    'order_id':orderid,
                    'customer_id': customerid,
                    'order_date':orderdate,
                    'order_end_date':safe_end_date,
                    'order_amount':orderamount,
                    'order_status':orderstatus,
                    'product_category':productcategory,
                    'Active_Flag':'Yes'
                }
                new_rows.append(new_data)
        
        else:
            new_data={
                    'order_id':orderid,
                    'customer_id': customerid,
                    'order_date':orderdate,
                    'order_end_date':safe_end_date,
                    'order_amount':orderamount,
                    'order_status':orderstatus,
                    'product_category':productcategory,
                    'Active_Flag':'Yes'
                }
            new_rows.append(new_data)

    if new_rows:
        d1=pd.concat([d1,pd.DataFrame(new_rows)],ignore_index=True)        
        
    return d1