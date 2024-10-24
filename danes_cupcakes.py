import mysql.connector

class cake:
  connection = any
  user = str
  id = int
  admin = bool



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
        self.login(crsr)
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
      self.user = name
      self.admin = True
      return True
    sql_command = f"""SELECT * from users where username = "{name}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    
    if result == None:
      print("Wrong info, try again.")
      self.login(crsr)
    elif result[2] == pw:
      print("Logged in")
      self.user = name
      self.id = result[0]
      if result[3] == 1:
        self.admin = True
      else:
        self.admin = False
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
        sql_command = f"""Insert into users (username, password, admin) values ("{name}", "{pw}", "{False}");"""
        crsr.execute(sql_command)
        self.connection.commit()
        self.user = name
        self.admin = False

        sql_command = f"""SELECT * FROM users where username = "{name}";"""
        crsr.execute(sql_command)
        result = crsr.fetchone()
        self.id = result[0]

        passed = True

  def options(self, crsr):
    repeat = True
    if self.admin == True:
        print("Hello, you have admin privileges for Dane's Cupcakes. What would you like to do?")

        #admin
        while repeat:
            print("1: Print out list of users\n2: Print out the menu\n3: Print out the list of orders\n4: Update the menu")
            print("5: Add items to the menu\n6: Delete items from the menu\n7: Give another user admin privileges")
            print("8: Take away admin priviliges\n9: Look at the current profit\n10: Delete a users account")
            i = input()
            match int(i):
                case 1: 
                    self.selectUsers(crsr)
                case 2:
                    self.selectMenu(crsr)
                case 3:
                    self.selectOrders(crsr)
                case 4:
                    self.updateMenu(crsr)
                case 5:
                    self.addMenu(crsr)
                case 6:
                    self.deleteMenu(crsr)
                case 7:
                    self.makeAdmin(crsr)
                case 8:
                    self.notAdmin(crsr)
                case 9: 
                    self.viewProfit(crsr)
                case 10:
                    self.deleteUser(crsr)
            print("Would you like to do anything else? (y/n)")
            i = input()
            if i == "n":
                repeat = False
                
    else:
        #User
        print("Welcome to Dane's Cupcakes! What would you like to do?")
        while repeat:
            print("1: Add a cupcake to your order?\n2: View your cart?\n3: Update your Username?\n4: Update your password?")
            print("5: Look at your total for your current cart\n6: Delete your account")
            i = input()
            match int(i):
                case 1:
                    self.makeOrder(crsr)
                case 2:
                    self.viewOrders(crsr)
                case 3:
                    self.updateUserName(crsr)
                case 4:
                    self.updatePassword(crsr)
                case 5:
                    self.viewTotal(crsr)
                case 6:
                    self.deleteProfile(crsr)
            print("Would you like to do anything else? (y/n)")
            i = input()
            if i == "n":
                repeat = False


  def deleteProfile(self, crsr):
    print("Are you sure you want to delete your profile? (Y/N)")
    i = input()
    if i == "Y":
      sql_command = f"""SELECT * from users where username = "{self.user}";"""
      crsr.execute(sql_command)
      result = crsr.fetchall()
      
      id = result[0][0]
      self.disableForeignKeyCheck(crsr)
      sql_command = f"""DELETE FROM users where id = "{id}";"""
      crsr.execute(sql_command)
      self.enableForeignKeyCheck(crsr)
      self.connection.commit()
    elif i == "N":
      print("Ok, returning to options.")

  def deleteUser(self, crsr):
    self.selectUsers(crsr)
    print("Whose profile do you want to remove? (Enter user id)")
    i = input()
    
    sql_command = f""" SELECT * from users where id = "{i}"; """
    crsr.execute(sql_command)
    result = crsr.fetchall()
    if result == []:
      print("Invalid user id, please enter again.")
      self.deleteUser(crsr)
    else:
      self.disableForeignKeyCheck(crsr)
      sql_command = f""" DELETE FROM users where id = "{i}"; """
      crsr.execute(sql_command)
      self.enableForeignKeyCheck(crsr)
      self.connection.commit()
    
  def makeAdmin(self, crsr):
    self.selectUsers(crsr)
    print("Which user do you want to give admin privileges? (Enter their user ID)")
    i = input()

    sql_command = f"""SELECT * FROM users where id = "{i}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()

    if result != []:
      if result[0][3] == False:
        sql_command = f"""UPDATE users set admin = true where id = "{i}";"""
        crsr.execute(sql_command)
        self.connection.commit()
      else:
        print("User already has admin privileges.")
    else:
      print("There is no user with that ID, try again.")
      self.makeAdmin(crsr)

  def notAdmin(self,crsr):
    self.selectUsers(crsr)
    print("Which user do you want to take away admin privileges? (Enter their user ID)")
    i = input()

    sql_command = f"""SELECT * FROM users where id = "{i}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()

    if result != []:
      if result[0][3] == True:
        sql_command = f"""UPDATE users set admin = false where id = "{i}";"""
        crsr.execute(sql_command)
        self.connection.commit()
      else:
        print("User already does not have admin privileges.")
    else:
      print("There is no user with that ID, try again.")
      self.notAdmin(crsr)

  def makeOrder(self, crsr):
    self.selectMenu(crsr)
    print("What would you like to order?")
    i = input()
    sql_command = f"""SELECT * from menu where flavor = "{i}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    if result == None:
      print("Non valid answer, try again.")
      self.makeOrder(crsr)
    price = result[0][1]
    sql_command = f"""SELECT id from users where username = "{self.user}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    sql_command = f"""Insert into orders (orderPrice, item, userId) VALUES ("{price}", "{i}","{result[0][0]}");"""
    crsr.execute(sql_command)
    self.connection.commit()
    
    
  def updateUserName(self, crsr):
    print("To make sure this is truly you, enter your password: ")
    i = input()
    sql_command = f"""SELECT * FROM users where password = "{i}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    if result == None:
      print("Wrong password.")
    elif result[2] == i:
      print("What would you like your new username to be?")
      i = input()
      sql_command = f"""UPDATE users set username = "{i}" where username = "{self.user}";"""
      crsr.execute(sql_command)
      self.connection.commit()
      self.user = i

  def updatePassword(self, crsr):
    print("To make sure this is truly you, enter your current password: ")
    i = input()
    sql_command = f"""SELECT * FROM users where password = "{i}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    if result == None:
      print("Wrong password.")
    elif result[2] == i:
      print("What would you like your new password to be?")
      i = input()
      sql_command = f"""UPDATE users set password = "{i}" where username = "{self.user}";"""
      crsr.execute(sql_command)
      self.connection.commit()


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
    else:
      print("Unknown option, try again.")
      self.updateMenu(crsr)
    print("Want to change anything else? (Y/N)")
    i = input()
    if i == "Y":
      self.updateMenu(crsr)
    
  def addMenu(self, crsr):
    self.selectMenu(crsr)
    print("Enter flavor that you want to add: ")
    flavor = input()
    sql_command = f"""SELECT * from menu WHERE flavor = "{flavor}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    if result == []:
      print("Enter price of item: ")
      price = input()
      sql_command = f"""INSERT INTO menu (flavor, price) VALUES ("{flavor}", "{price}");"""
      crsr.execute(sql_command)
      self.connection.commit()
    else:
      print("Flavor already exists, please try again")
      self.addMenu(crsr)

  def deleteMenu(self, crsr):
    self.selectMenu(crsr)
    print("Enter flavor that you want to delete: ")
    flavor = input()
    sql_command = f"""SELECT * from menu WHERE flavor = "{flavor}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    if result != []:
      sql_command = f"""DELETE FROM menu WHERE flavor = "{flavor}";"""
      crsr.execute(sql_command)
      self.connection.commit()
    else:
      print("Flavor doesn't exists, please try again")
      self.deleteMenu(crsr)

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
    for x in result:
      print(x)

  def selectOrders(self, crsr):
    sql_command = """SELECT * FROM orders;"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    for x in result:
      print(x)
    
  def viewOrders(self, crsr):
    sql_command = f"""SELECT id from users WHERE username = "{self.user}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()

    #print(result[0])
    sql_command = f"""SELECT * from orders WHERE userId = "{result[0]}";"""
    crsr.execute(sql_command)
    result = crsr.fetchall()
    print("Orders:")
    for x in result:
      print(x)

  """ def insert(self, username:str, password:str, crsr):
    sql_command = fINSERT INTO users (username, password) VALUES("{username}", "{password}");

    crsr.execute(sql_command)
    self.connection.commit() """

  def viewTotal(self,crsr):
    sql_command = f"""SELECT SUM(orderPrice) from orders where userId = "{self.id}";"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    print(f"${result[0]}")
  

  def viewProfit(self,crsr):
    sql_command = """SELECT SUM(orderPrice) from orders;"""
    crsr.execute(sql_command)
    result = crsr.fetchone()
    print(f"${result[0]}")

  def disableForeignKeyCheck(self, crsr):
    sql_command = """SET FOREIGN_KEY_CHECKS=0;""" # to disable them
    crsr.execute(sql_command)

  def enableForeignKeyCheck(self, crsr):
    sql_command = """SET FOREIGN_KEY_CHECKS=1;""" # to enable them
    crsr.execute(sql_command)

  def closeConnection(self):
    # close the connection
    self.connection.close()
    
