import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

test.start(crsr)
#test.makeOrder(crsr)

#test.selectUsers(crsr)
#test.selectMenu(crsr)

#test.updateMenu(crsr)
#test.selectOrders(crsr)
#test.deleteProfile(crsr)
#test.updateUserName(crsr)
#test.updatePassword(crsr)
#test.deleteUser(crsr)
#test.viewOrders(crsr)
#test.addMenu(crsr)
#test.deleteMenu(crsr)
#test.makeAdmin(crsr)
#test.notAdmin(crsr)

test.closeConnection()