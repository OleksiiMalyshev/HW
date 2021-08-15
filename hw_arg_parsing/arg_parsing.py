import argparse
import json


class UserOrEmailInvalid(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Enter username ")
parser.add_argument("--email", help="Enter email ")

args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict["username"] = args.username

if args.email:
    user_dict["email"] = args.email

with open("data.json", 'r') as file:
    user_data = json.loads(file.readline())

try:
    for user in user_data:
        if user["username"] == user_dict["username"]:
            raise UserOrEmailInvalid
        elif user["email"] == user_dict["email"]:
            raise UserOrEmailInvalid

    user_data.append(user_dict)

except UserOrEmailInvalid:
    print("Username or email already exist! To change him.")


with open("data.json", 'w') as file:
    file.write(json.dumps(user_data))