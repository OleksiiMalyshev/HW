import json


class UserOrEmailInvalid(Exception):
    pass


def dict_add(us, em):
    user_dict = {'username': us, 'email': em}
    return user_dict


user_list = []

while True:
    try:
        user_data = input("Введите username и email (ex to exit) - ").split()
        if user_data[0] == 'ex':
            break
        for i in user_list:
            if i['username'] == user_data[0] or i['email'] == user_data[1]:
                raise UserOrEmailInvalid

        user_list.append(dict_add(user_data[0], user_data[1]))
    except UserOrEmailInvalid:
        print("User or Email already exists")

users = json.dumps(user_list)

with open('data.json', 'r') as file:
    file.readline()

with open('data.json', 'w') as file:
    file.write(users)

print(users)
