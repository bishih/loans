import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="operator_result", user='postgres', password='secretpassword', host='172.17.86.196', port= '31276'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS opertorResult")

#Creating table as per requirement
sql ='''CREATE TABLE opertorResult(
   num1 integer NOT NULL,
   num2 integer NOT NULL,
   operator varchar(1),
   result integer,
   id serial PRIMARY KEY
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()