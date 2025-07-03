from Question_11.src.util import ssms_connection


#============ Database Creation =====================

def create_database(db_name):
    conn_call=ssms_connection() 
    cursor=conn_call.cursor()

    try:
        cursor.execute("Select name from sys.databases where name = ?",db_name)
        result = cursor.fetchone()

        if result:
            print(f"Database {db_name} exists")
        else:
            cursor.execute(f'Create Database {db_name}')
            conn_call.commit()
            print(f'Database {db_name} has been created successfully')
    except Exception as e:
        print("Error Creating database",e)
    finally:
        cursor.commit()
        conn_call.commit()

