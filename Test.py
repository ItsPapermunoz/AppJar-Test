# Imports

import appJar
import pickle

users = []
passwords = []
accounts = [users, passwords]


def database():
    try:
        accounts = pickle.load(open("Accounts_DB.data", "rb"))
    except FileNotFoundError:
        users = []
        passwords = []
        accounts = [users, passwords]
        pickle.dump(accounts, open("Accounts_DB.data", "wb"))
    finally:
        return accounts


def menu(btn):
    global accounts
    if btn == "Register":
        user = app.stringBox("Register", "Please type your new user")
        password = app.stringBox("Register", "Please type in your password")
        accounts[0].append(user)
        accounts[1].append(password)
        pickle.dump(accounts, open("Accounts_DB.data", "wb"))
    elif btn == "Login":
        i = 0
        user = app.stringBox("Login", "Please type your username")
        password = app.stringBox("Login", "Please type in your password")
        for username in accounts[0]:
            if user == username:
                if password == accounts[1][i]:
                    app.addLabel("Login Succesfull!")
            i += 1

app = appJar.gui("Login!")
app.setSize(1000,700)
app.setLocation(200, 50)
app.addButtons(["Register", "Login"], menu)


# Main

accounts = database()
app.go()
