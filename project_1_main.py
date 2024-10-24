import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

test.start(crsr)
repeat = True
if test.admin == True:
    print("Hello, you have admin privileges for Dane's Cupcakes. What would you like to do?")

    #admin
    while repeat:
        print("1: Print out list of users\n2: Print out the menu\n3: Print out the list of orders\n4: Update the menu")
        print("5: Add items to the menu\n6: Delete items from the menu\n7: Give another user admin privileges")
        print("8: Take away admin priviliges\n9: Look at the current profit\n10: Delete a users account")
        i = input()
        match int(i):
            case 1: 
                test.selectUsers(crsr)
            case 2:
                test.selectMenu(crsr)
            case 3:
                test.selectOrders(crsr)
            case 4:
                test.updateMenu(crsr)
            case 5:
                test.addMenu(crsr)
            case 6:
                test.deleteMenu(crsr)
            case 7:
                test.makeAdmin(crsr)
            case 8:
                test.notAdmin(crsr)
            case 9: 
                test.viewProfit(crsr)
            case 10:
                test.deleteUser(crsr)
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
                test.makeOrder(crsr)
            case 2:
                test.viewOrders(crsr)
            case 3:
                test.updateUserName(crsr)
            case 4:
                test.updatePassword(crsr)
            case 5:
                test.viewTotal(crsr)
            case 6:
                test.deleteProfile(crsr)
        print("Would you like to do anything else? (y/n)")
        i = input()
        if i == "n":
            repeat = False

test.closeConnection()