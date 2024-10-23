import mysql.connector

class cake:
  connection = any
  


  def __init__(self):
    self.connection = mysql.connector.connect(
        host="danes-cupcakes.cp6m66ak6r7n.us-east-1.rds.amazonaws.com",
        user="admin",
        password="MasterPassword!1",
        database="DanesCupcakes"
    )
  
  def openConnection(self):
    return self.connection.cursor()

  def login(self, crsr):


    print("Enter Username: ")
    name = input()
    print("Enter Password: ")
    pw = input()

    if(name == "admin" and pw == "MasterPassword!1"):
      print("Logged in")
      return True
    sql_command = f"""SELECT password from users where username = "{name}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    print(result)
    if result == None:
      print("Wrong info, try again.")
      self.login(crsr)
    elif result[0] == pw:
      print("Logged in")
      return False
    else:
      print("Wrong info, try again.")
      self.login(crsr)
    

    
  def createUser(self, crsr):
    print("To create a profile, enter a Username: ")

    passed = False
    while not passed:
      name = input()

      sql_command = f"""SELECT * from users where username = "{name}";"""
      crsr.execute(sql_command)
      result = crsr.fetchall()


      if result != []:
        print("Username already exists, please enter a different one: ")
      else:
        print("Enter Password: ")
        pw = input()
        sql_command = f"""Insert into users (username, password) values ("{name}", "{pw}");"""
        crsr.execute(sql_command)
        self.connection.commit()
        passed = True

    
    




  def updateMenu(self, item, value):
    sql_command = f"""UPDATE menu """
    pass
    
  def selectUsers(self, crsr):
    sql_command = """SELECT * FROM users;"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
  
    for x in result:
      print(x)

  def selectMenu(self, crsr):
    sql_command = """SELECT * FROM menu;"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    print(type(result))
    for x in result:
      print(x)

  def selectOrders(self, crsr):
    sql_command = """SELECT * FROM orders;"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    print(type(result))
    for x in result:
      print(x)
    

  def insert(self, username:str, password:str, crsr):
    sql_command = f"""INSERT INTO users (username, password) VALUES("{username}", "{password}");"""

    crsr.execute(sql_command)
    self.connection.commit()

  def closeConnection(self):
    # close the connection
    self.connection.close()
    