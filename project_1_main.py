import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

test.start(crsr)

#admin

#test.selectUsers(crsr)
#test.selectMenu(crsr)
#test.selectOrders(crsr)
#test.deleteUser(crsr)
#test.updateMenu(crsr)
#test.addMenu(crsr)
#test.deleteMenu(crsr)
#test.makeAdmin(crsr)
#test.notAdmin(crsr)
#test.viewProfit(crsr)

#users

#test.makeOrder(crsr)
#test.viewOrders(crsr)
#test.deleteProfile(crsr)
#test.updateUserName(crsr)
#test.updatePassword(crsr)
#test.viewTotal(crsr)

test.closeConnection()