#print(type(login_details))

#Receives username first,
username = input('Enter your username:\n')

#Checks if username in dcitionary
if username in login_details:
    print('Hi %s!' %username)
    #prompts for password
    password = input( 'Input your password: ')
    #checks if password is valid and prints success message
    if password == login_details[username]:
        print('Welcome, %s !' %username)

    #prints error message for invalid password
    else:
        print('Sorry %s, Incorrect password' %username)
        
#prints error message for invalid user
else:
    print('Commot for here joor!, You never register and you wan sign in')
