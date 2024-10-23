import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

#test.start(crsr)
test.deleteUser(crsr)
test.selectUsers(crsr)

test.closeConnection()