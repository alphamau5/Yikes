# using usernames.json
import json

with open("usernames.json") as accounts:
    users_json = json.load(accounts)


def login(u):
    # already have an account
    u_n = input("username: ")
    pw = input("password: ")
    if u["users"][u_n][0]["password"] == pw:
        print(u["users"][u_n][1]["general"], u["users"][u_n][2])
    else:
        print("incorrect, try again or quit (ctrl+c)")
        login(u)


def intro():
    print("1: sign in\n2: sign up")
    enter = int(input("enter one or 2: "))
    if enter == 1:
        login(users_json)
    if enter == 2:
        signup(users_json)


def signup(u):
    # signing up a new user
    first_n = input("first name: ")
    last_n = input("last name: ")
    usrnm = input("enter username: ")
    passwd = input("enter password: ")
    country = input("country: ")
    city = input("city: ")
    print("enter top 3 bucket list items: ")
    bucket_list = []

    for i in range(0, 3):
        bucket_list.append(input())

    new_user = [
        {
            "password": passwd},
        {
            "general": {
                "first_n": first_n,
                "last_n": last_n,
                "location": {
                    "country": country,
                    "location": city}}},
        {
            "bucket_list": bucket_list}]

    u["users"][usrnm] = new_user
    with open('usernames.json', 'w') as updated_accounts:
        json.dump(u, updated_accounts, indent=2)

    # takes you back to log in screen
    intro()


intro()
