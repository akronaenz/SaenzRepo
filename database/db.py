import pymysql

endpoint = 'database-1.cjgms0iukpn8.us-east-2.rds.amazonaws.com'
user = 'admin'
passw = 'linalove13'

def connectionSQL():
    try:

        obj_connect = pymysql.connect(
            host=endpoint,
            user=user,
            password=passw,
        )
        print("Succesfull connection to a database")
        return obj_connect
    except Exception as err:
        print("Error:", err)
        obj_connect = None

    
def add_user(id, name, lastname, birtdhay):
    try:
         instruction_sql = "INSERT INTO db_users.users(id, name, lastname, birtdhay) VALUES("+id+", '"+name+"', '"+lastname+"', '"+birtdhay+"')"
         obj_connect = connectionSQL()
         cursor = obj_connect.cursor()
         cursor.execute(instruction_sql)
         obj_connect.commit()
         print("The user was added")
         return True
    except Exception as err:
        print("Error:", err)
        return False
        
def consult_user(id):
    try:
        instruction_sql = "SELECT * FROM db_users.users WHERE id="+id+";"
        obj_connect = connectionSQL()
        cursor = obj_connect.cursor()
        cursor.execute(instruction_sql)
        result_data = cursor.fetchall()
        print ("User Consulted")
        return result_data
    except Exception as err:
        print("Error:", err)
        return False