import pymysql

endpoint = 'database-1.cjgms0iukpn8.us-east-2.rds.amazonaws.com'
user = 'admin'
passw = 'linalove13'

def connectionSQL():
    try:

        pymysql.connect(
            host=endpoint,
            user=user,
            password=passw,
        )
        print("Succesfull connection to a database")
    except Exception as err:
        print("Error:", err)
    
connectionSQL()