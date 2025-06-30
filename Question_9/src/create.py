import pandas as pd

def create_table():
    data={
        'order_id':['209c024e-6c32-49fa-acd1-2501bd19c1cd','f431b991-f9ab-4bac-a8f5-36e0181f5a8c','84421d2f-784e-4fd2-8055-4838dc313f45',
        'fcbe6295-d0e2-4a53-8d73-2c24947c174f','abhinay-abhi1249-varshini-varsh0567'],
        'customer_id':[2,6,49,463,1000],
        'order_date':['2023-11-30','2023-04-12','2024-08-13','2023-03-22','2024-04-22'],
        'order_amount':[499.99,0,20,150,1000],
        'order_status':['Completed','Cancelled','Completed','Cancelled','Completed'],
        'product_category':['Toys','Electronics','Toys','Books','Shoes']
    }
    df=pd.DataFrame(data)
    return df

