# Simple Password Manager by Michael Hebert
# A simple password manager that creates passwords of several difficulties, saves them to a file, and provides a way to look them up with an authentication system
# Version 2.0 will inlcude a GUI, however this version runs in the terminal

from random import randint

chars = "abcddefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$1234567890"
charList = list(chars)


def authenticationSet(change):  # allows user to set authentication password if there is none, or if they want to change it
    au = open("Authentication.txt", "r")
    auStr = au.read()  # creates a string with the contents of the auth document
    if len(auStr) == 0:  # checks if there is a password there already
        authenticatorPass = input("Please input an authenticator password. Remember this! It is important! ")
        au = open("Authentication.txt", "w")
        au.write(authenticatorPass)
    elif change == True:
        makeSure = input("To change authenticator password, please input past password to verify: ")  # security check
        if makeSure == auStr:
            authenticatorPass = input("Please input an authenticator password. Remember this! It is important! ")
            au = open("Authentication.txt", "w")
            au.write(authenticatorPass)
        else:
            print("Wrong password, try again...")  # if failed it boots the user back to choices
    au.close


def authenticator(userAuth):  # to authenticate password lookup
    a = open("Authentication.txt", "r")
    authentication = a.read()
    if userAuth == authentication:
        return True
    else:
        return False

def lookup(dictionary):  # looks up sites in the contentDict dictionary
    passLookup = str(input("Which site's password do you wish to lookup? Type 'back' to go back "))
    while True:
        if passLookup in dictionary:
            print(f"The {passLookup} password is {dictionary[passLookup]}")
        if passLookup == "back":
            break
        else:
            passLookup = str(input("Please type in a valid website, or type 'back' to go back "))

def passGenerator(difficulty):  # generates the passwords, difficulties have different lengths
    password = ""
    if difficulty == "easy":
        for i in range (0,8):
            randomChar = randint(0, len(charList)-1)
            password += charList[randomChar]
    elif difficulty == "medium":
        for i in range (0,12):
            randomChar = randint(0, len(charList)-1)
            password += charList[randomChar]
    elif difficulty == "hard":
        for i in range (0,16):
            randomChar = randint(0, len(charList)-1)
            password += charList[randomChar]
    else:
        difficulty = str(input("Please input either 'easy', 'medium', 'hard', or 'back' to go back. "))

    return password


passDict = {}

f = open("Passwords.txt", "r")  # reads the passwords document
content = f.read()
f.close()
contentList = content.split()
contentDict = {}
for i in range(0, len(contentList) - 1):  # creates a dictionary with the site as a key and password as the value
    if i == 0 or i % 2 == 0:  # since the site is always even, this will find the site name and put it as the key in the dictionary
        contentDict[contentList[i]] = contentList[i + 1]

# initial print statements, includes instructions and disclaimer
print("HELLO AND WELCOME TO MICHAEL'S PASSWORD MANAGER")
print("TO BEGIN, FOLLOW THE INSTRUCTIONS BELOW\n")
print("IMPORTANT NOTE: THIS PASSWORD MANAGER IS HIGHLY INSECURE AS TXT FILES ARE READILY READABLE, PLEASE DO NOT USE THIS FOR SERIOUS PURPOSES\n")

while True:
    change = False
    authenticationSet(change)  # executes if there is no auth password in the text document
    userInput = str(input("What would you like to do? 'Lookup', 'Create' a Password, 'Change' Auth Password, or 'Quit'? ")).lower()
    # the following statements point the program to which function to call
    if userInput == "lookup":
        authPassword = str(input("What is the authenticator password? "))
        auth = authenticator(authPassword)
        if auth:
            lookup(contentDict)
        else:
            print("FAKE USER DETECTED! QUITTING PROGRAM")
            break
    elif userInput == "create":
        while True:
            site = str(input("What site is this password for? Type 'back' to go back. "))
            if site != "back":
                difficulty = str(input("Please input either 'easy', 'medium', 'hard', or 'back' to go back. "))
            if site == "back" or difficulty == "back":
                if len(passDict) == 0:
                    print("No passwords generated.")
                    break
                else:
                    break
            else:
                f = open("Passwords.txt", "a+")
                password = passGenerator(difficulty)
                passDict[site] = password
                print(f"Password Generated! {site} password is: {password}")  # if the site is already in use, it's password will be replaced
                f.write(f"{site} {password}\n")
                f.close()
    elif userInput == "quit":
        print("Goodbye!")
        break
    elif userInput == "change" or userInput == "change password":  # allows the user to change their authenticator password
        change = True
        authenticationSet(change)
    else:
        userInput = str(input("Please input either 'lookup', 'create' or 'create password', 'change', or 'quit'"))  # failsafe response


