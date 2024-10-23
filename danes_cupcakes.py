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
  
  

  def start(self, crsr):
    print("Do you have an account? (Y/N): ")
    i = input()
    if i =="Y":
        admin = self.login(crsr)
    elif i == "N":
        self.createUser(crsr)
    else:
        print("Unknown response, please try again.")
        self.start(crsr)

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

    
    




  def updateMenu(self, crsr):
    print("What do you want to change? (prices, flavors)")
    i = input()
    if i == "prices":
      self.selectMenu(crsr)
      print("Which cupcake price do you want to change? (Enter flavor)")
      flavor = input()
      print("Enter new price: ")
      price = input()
      sql_command = f"""UPDATE menu set price = "{price}" where flavor = "{flavor}";"""
      crsr.execute(sql_command)
      self.connection.commit()
    elif i == "flavors":
      self.selectMenu(crsr)
      print("Which cupcake flavor do you want to change? (Enter flavor)")
      flavor = input()
      print("Enter new name: ")
      name = input()
      sql_command = f"""UPDATE menu set flavor = "{name}" where flavor = "{flavor}";"""
      crsr.execute(sql_command)
      self.connection.commit()
    
    
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

  def deleteUser(self, crsr):
    print("Who's account do you want to delete?")
    name = input()
    sql_command = f"""SELECT * from users where username = "{name}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    
    id = result[0][0]
    self.disableForeignKeyCheck(crsr)
    sql_command = f"""DELETE FROM users where id = "{id}";"""
    crsr.execute(sql_command)
    self.enableForeignKeyCheck(crsr)
    self.connection.commit()

  def disableForeignKeyCheck(self, crsr):
    sql_command = """SET FOREIGN_KEY_CHECKS=0;""" # to disable them
    crsr.execute(sql_command)

  def enableForeignKeyCheck(self, crsr):
    sql_command = """SET FOREIGN_KEY_CHECKS=1;""" # to enable them
    crsr.execute(sql_command)

  def closeConnection(self):
    # close the connection
    self.connection.close()
    
