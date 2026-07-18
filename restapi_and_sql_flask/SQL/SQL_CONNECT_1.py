# terminal
# pip install mysql-connector-python

import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="ml_project"
    )
conn=get_conn()
print("connected : "conn.is_connected())
conn.close()

# Create database and table

conn=mysql.connector.connect(host="localhost",user='root',password="pass")
c=conn.cursor()

c.execute("CREATE DATABASE IF NOT EXIST ml_project")
c.execute("USE ml_project")

c.execute("""
          CREATE TABLE IF NOT EXISTS predictions(
          id           INT AUTO_INCREMENT PRIMARY KEY,
          input_data    TEXT,
          prediction    VARCHAR(100),
          CONFIDENCE    FLOST  
          created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
          )""")