

import mysql.connector

class cake:
  connection = any
  


  def __init__(self):
    self.connection = mysql.connector.connect(
        host="danes-cupcakes.cp6m66ak6r7n.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Waner!321",
        database="DanesCupcakes"
    )
  # cursor
  def openConnection(self):
    return self.connection.cursor()

  def updateMenu(self, item, value):
    sql_command = f"""UPDATE menu """
    pass
    
  def select(self, crsr):
    sql_command = """SELECT * FROM users;"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    
    for x in result:
      print(x)
    

  def insert(self, username:str, password:str, crsr):
    sql_command = f"""INSERT INTO users (username, password) VALUES("{username}", "{password}");"""

    crsr.execute(sql_command)
    self.connection.commit()

  def closeConnection(self):
    # close the connection
    self.connection.close()
    