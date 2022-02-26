from flask import json
import json
user_list = [
    {
        "name": "Thien An",
        "surname": "Ngo"
    },
    {
        "name": "Thien Minh",
        "surname": "Ngo"
    }
]

user = {
    "name": "Thien Minh",
    "surname": "Ngo"
}


def load_user():  # lese aus users.json
    f = open('users.json')  # lese aus users.json
    content = json.load(f)
    for i in content["data"]:
        print(i)
    f.close()


def find_user():
    # for u in user_list gehe alle benutzer in der liste durch
    filtered_user = [item for item in user_list if item['name'] == user['name']]
    if filtered_user is not None and len(filtered_user) > 0:
        return filtered_user[0]
    return None


def is_user_ready_exist():
    user_from_list = find_user()
    exist = user_from_list is not None  # is euq==
    return exist


list_user = find_user();
print(f'list_user: {list_user}')

exist = is_user_ready_exist()
print(f'exist: {exist}')
load_user()

