# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(
#    database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# cursor.execute("select * from products")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print("Connection established to: ",data)

      # 5.QUIZ
#Once you see products,now redo the code and have a function called get_data that:
#takes in table_name as aguements
#fetches all records
#return list of records

import psycopg2

def table_name(p):
   conn = psycopg2.connect(
   database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
   cursor = conn.cursor()
   t = "select * from"+" " + p
   cursor.execute(t)
   data = cursor.fetchall()
   return data

products=table_name("products")

# print(products)



sales = table_name("sales")
print(sales)


  
    

      

