import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

test.start(crsr)

test.options(crsr)

test.closeConnection()