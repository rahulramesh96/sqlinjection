import mysql.connector

def search_users(username):
  db = mysql.connector.connect(
    host="localhost",
    user="myusername",
    password="mypassword",
    database="mydatabase"
  )
  cursor = db.cursor()
  query = "SELECT * FROM users WHERE username = '" + username + "'"
  cursor.execute(query)
  results = cursor.fetchall()
  db.close()
  return results
