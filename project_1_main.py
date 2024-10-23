import danes_cupcakes as cl


test = cl.cake()

crsr = test.openConnection()

print("Do you have an account? (Y/N): ")
i = input()
if i =="Y":
    admin = test.login(crsr)
    


#test.createUser(crsr)

#test.selectUsers(crsr)

test.closeConnection()