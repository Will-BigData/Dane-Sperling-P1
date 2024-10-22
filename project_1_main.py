import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()


#loggedIn = test.login(crsr)


test.createLogin(crsr)

#test.selectUsers(crsr)

test.closeConnection()