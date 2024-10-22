import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

i = "Y"
while i == "Y":
    #test.insert("Connor", "password1", crsr)
    test.select(crsr)
    print("Would you like to perform again? (Y?N)")
    i = input()

test.closeConnection()