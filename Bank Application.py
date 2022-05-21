import random
import time
import sqlite3

conn =  sqlite3.connect('BankAccounts.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE Accounts (Name TEXT, Gender TEXT, Age INTEGER, Nationality TEXT, AccNum INTEGER UNIQUE, AccBal FLOAT )')
except:
    None
    
def createAccount():
    accNumber = random.randint(1000000, 2000000)
    """Creates an Account """
    name = input('Please enter your name: ')
    gender = input('Please enter your gender: ')
    age = input('Please enter your Age: ')
    nationality = input('Please enter your Country of Origin: ')
    accBalance = 0
    cur.execute('INSERT INTO Accounts (Name, Gender, Age, Nationality, AccNum, AccBal) VALUES(?,?,?,?,?,?)',
                (name, gender, age, nationality, accNumber,accBalance))
    conn.commit()
    print("You're Account has been created!")
    

def checkAccountDetails():
    choice = input("Enter your name and we'll provide your details: ")
    cur.execute('SELECT Name, Gender, Age, Nationality, AccNum, AccBal FROM Accounts WHERE Name = "%s"' %choice)
    for row in cur:    
        print('Your Account name is ',row[0])
        print('Gender: ',row[1])
        print('Age: ',row[2])
        print('Nationality: ',row[3])
        print('Your Account number is ',row[4])
        print('Your Account balance is ',row[5])

def depositMoney():
    choice = input("Enter your The Account name you wish to deposit into: ")
    deposit = eval(input('Please Enter the Amount you wish to deposit: '))
    cur.execute('UPDATE Accounts SET AccBal = AccBal + %d WHERE Name = "%s"' %(deposit, choice))
    conn.commit()
    time.sleep(1)
    cur.execute('SELECT  AccBal FROM Accounts WHERE Name = "%s"' %choice)
    for row in cur:    
        print('Your Account balance is now ',row[0])
    

def withdrawMoney():
    choice = input("Enter your The Account name you wish to withdraw from: ")
    wthdraw = eval(input('Please Enter the Amount you wish to withdraw: '))
    cur.execute('SELECT  AccBal FROM Accounts WHERE Name = "%s"' %choice)
    for i in cur:
        bal = i[0]
    if bal < wthdraw:
        print("Insufficient funds")
    else:
        cur.execute('UPDATE Accounts SET AccBal = AccBal - %d WHERE Name = "%s"' %(wthdraw, choice))
        conn.commit()
        time.sleep(1)
        cur.execute('SELECT  AccBal FROM Accounts WHERE Name = "%s"' %choice)
        for row in cur:    
            print('Your Account balance is now ',row[0])

print("Hi There! \n Welcome to Noel's Bank!")
print("What would you like to do today?")

while True:
    option = input("""Enter:
            1 to Create an Account
            2 to Check Account Details
            3 to Deposit Money
            4 to Withdraw Money
            5 to Quit \n: """)
    if option == '1':
        createAccount()
        print('Would you like to do something else')
    elif option == '2':
        checkAccountDetails()
        print('Would you like to do something else')
    elif option == '3':
        depositMoney()
        print('Would you like to do something else')
    elif option == '4':
        withdrawMoney()
        print('Would you like to do something else')
    elif option == '5':
        print("Have a Lovely day!!")
        
        break
    else :
        print('Invalid Input')
        print('Would you like to do something else')
            
