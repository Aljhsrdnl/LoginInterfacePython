#the user has an option to sign up or log in
#login system

from tkinter import *

root = Tk()
root.title("Simple Log in System")

stat = StringVar()
title = Label(root, text = "Simple Log in System").grid(row = 0, column = 0, padx = 50, pady = 20, columnspan=2)
def clearEntry():
    userName.delete(0, END)
    password.delete(0, END)
    
def checkIfPasswordMatch():
    if input_password == regPassword:
        stat.set( "You have logged in!")
        print("You are in the system! welcome!")
        clearEntry()
    else:
        stat.set("The password is incorrect.")
        print("The password is incorrect.")


def analyzeData():
    f = open("login.txt", "r")

    for line in f:
        if input_username in line:
            global data
            data = line.split("$")
            global regUsername
            global regPassword
            regUsername = data[0]
            regPassword = data[1]
            print(regPassword, input_password)
            if input_username == regUsername:
                checkIfPasswordMatch()
                return
            else:
                stat.set( "Username not found!")
                print("Username cannot be found")
                clearEntry()
        else:
            stat.set("Username not found!")
            clearEntry()

    f.close()
    

    
def getData ():
    global input_username
    global input_password
    input_username = userName.get()
    input_password = password.get()
    analyzeData()
    
    
user = Label(root, text = "Username")
passWord = Label (root, text = "Password")
userName = Entry(root, width = 50)
password = Entry(root, width = 50, show = "*")
submitBtn = Button(root, width = 10, text = "Log in", command = getData)

statusUpdate = Label(root, textvariable = stat ).grid(row = 3, column = 0, columnspan = 2, pady = 20)
stat.set("Log in using your username.")
user.grid(row = 1, column = 0, padx = 10)
passWord.grid(row = 2, column = 0, padx = 10)
userName.grid(row = 1, column = 1, padx = 10)
password.grid(row = 2, column = 1, padx = 10)
submitBtn.grid(row = 4, column = 0, columnspan = 2)



root.mainloop()

