import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

test.start(crsr)
#test.makeOrder(crsr)
#test.deleteUser(crsr)
#test.selectUsers(crsr)
#test.updateMenu(crsr)
#test.selectOrders(crsr)
#test.deleteProfile(crsr)
#test.updateUserName(crsr)
test.updatePassword(crsr)

test.closeConnection()