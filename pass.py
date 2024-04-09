print("Welcome to Pyrofox, Enter your username and password.")
entered_User = input("Username: ")
enteredPass = input("Password: ")
inSystem_User = "Test_1234"
inSystem_pass = 251045
username = entered_User == inSystem_User
password = int(enteredPass) == inSystem_pass
print(username)
if username is True:
    print("Valid Username, but the password?")
else:
    print("No user found with that username, I guess you wrote it wrong or just tried to hack someone in here.")
print(password)
if password is True:
    print("Ok, go in, I just don't know how to make a JavaScript (or even HTML/CSS or PHP) UI.")
else:
    print("Are you trying to hack someone on this device to get their personal info? You have been reported to the FBI.")
