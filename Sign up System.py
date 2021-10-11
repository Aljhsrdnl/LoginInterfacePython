from tkinter import *
import string
root = Tk()
root.title("Sign Up System")




def registerAccount():
    file = open("login.txt", "a")
    file.write("\n" + userName + "$" + password + "$" + firstName + "$" + lastName)
    file.close()
    signUpStatus.set("You are logged in.")

def passwordStrength():
    val = True
    if len(password) < 8:
        print("Password must be atleast 8 characters.")
        val = False

    if not any(char.isdigit() for char in password):
        print("Password must have at least one number.")
        val = False

    if not any(char.isupper() for char in password):
        print("Password must have atleast one uppercase letter.")
        val = False

    if not any(char.islower() for char in password):
        print("Password must have atlease one lowercase letter.")
        val = False

    if val == True:
        signUpStatus.set("Password is valid!")
        registerAccount()
    else:
        signUpStatus.set("Password is invalid!")


            
def passwordMatch():
    if password_confirmation == password:
        passwordStrength()
    else:
        signUpStatus.set("Your passwords don't match. Please retype them.")
        retypePasswordInput.delete(0, END)
        
def checkForNameDuplicate():
    file = open("login.txt", "r")
    global reg_firstName
    global reg_lastName
    global reg_userName
    global reg_password
    
    for line in file:
        if userName in line:
            data = line.split("$") #get the data line
            username_is_in_file = True
            break
        elif userName not in line:
            username_is_in_file = False
    print(username_is_in_file)
            
    if username_is_in_file == True:
        reg_firstName = data[2]
        reg_lastName = data[3].replace("\n", "")
        reg_userName = data[0]
        reg_password = data[1]       
        if (userName == reg_userName):
            signUpStatus.set("The username " + userName + " is already taken.")
            usernameInput.delete(0, END)
            print("The username is already taken")
        else:
            passwordMatch()
            print("the username is available!!!!!!!")
    else:
        passwordMatch()
        print("the username is available.")
        
    file.close()
    
def getData():
    global firstName
    global lastName
    global userName
    global password
    global password_confirmation
    firstName = firstNameInput.get()
    lastName = lastNameInput.get()
    userName = usernameInput.get()
    password = passwordInput.get()
    password_confirmation = retypePasswordInput.get()
    
    #print(firstName, lastName, userName, password, password_confirmation)
    
    checkForNameDuplicate()
    
signUpStatus = StringVar()
passwordAdvisory = StringVar()
header = Label(root, text = "Sign up").grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)

firstNameLbl = Label(root, text = "First Name").grid(row = 1, column = 0)
lastNameLbl = Label(root, text = "Last Name").grid(row  = 2, column = 0)
usernameLbl = Label(root, text = "Username").grid(row = 3, column = 0)
passwordLbl = Label(root, text = "Password").grid(row = 4, column = 0)
retypePasswordLbl = Label(root, text = "Confirm your password").grid(row = 7, column = 0)
submitBtn = Button(root, text = "Submit", command = getData).grid(row = 8, column = 0, columnspan = 2 , pady = 20)
passwordRule = Label(root, textvariable = passwordAdvisory ).grid(row = 5, column = 0, columnspan = 2, rowspan = 2)
passwordAdvisory.set("Password must be atleast 8 characters with uppercase and lowercase letters and digits.")
statusSee = Label(root, textvariable = signUpStatus).grid(row = 9, column = 0, columnspan = 2)
signUpStatus.set("Fill up the form above to sign up.")

#input fields
firstNameInput = Entry(root, width = 50)
lastNameInput = Entry(root, width = 50)
usernameInput = Entry(root, width = 50)
passwordInput = Entry(root, width = 50, show = "*")
retypePasswordInput = Entry(root, width = 50, show = "*")


#Lay out
firstNameInput.grid(row  = 1, column = 1)
lastNameInput.grid(row  = 2, column = 1)
usernameInput.grid(row  = 3, column = 1)
passwordInput.grid(row  = 4, column = 1)
retypePasswordInput.grid(row  = 7, column = 1)
root.mainloop()
