from flask import Flask, render_template, request, redirect, json, jsonify

app = Flask(__name__)

USER_FILE_NAME = 'src/users.json'


def load_user():
    file = open(USER_FILE_NAME)  # lese aus users.json
    content = json.load(file)
    file.close()
    print(content)
    return content  # gibt gelesene liste zurück


user_list = load_user()


user = {
    "name": "",
    "surname": "",
    "address": "",
    "zipcode": None,
    "city": "",
    "email": "",
}

form_data = {
    'user': user,
    'message': '',
    'name_error': '',
    'surname_error': '',
    'address_error': '',
    'zipcode_error': '',
    'city_error': "",
    'e-mail_error': "",
}


@app.route("/register/", methods=['GET', 'POST'])
def register():
    print(f'methode: {request.method}')
    if request.method == 'POST':
        read_form()
        is_form_valid = validation()
        if is_form_valid:
            return render_template('register_confirm.html', user=form_data['user'])

    return render_template('register.html', form_data=form_data)


@app.route("/register/delete/")
def delete_user():
    reset_user()
    return redirect("/register/")


def reset_user():
    user["name"] = ''
    user["surname"] = ''
    user["address"] = ''
    user["zipcode"] = ''
    user["city"] = ''
    user["email"] = ''


def reset_error():
    form_data['zipcode_error'] = None
    form_data['name_error'] = None
    form_data['surname_error'] = None
    form_data['address_error'] = None
    form_data['city_error'] = None
    form_data['email_error'] = None


def read_form():
    reset_error()
    global user
    user['name'] = request.form['name']
    user['surname'] = request.form['surname']
    user['address'] = request.form['address']
    user['city'] = request.form['city']
    user['email'] = request.form['email']
    try:
        user['zipcode'] = int(request.form['zipcode'])
    except ValueError:
        print('ValueError')
        user['zipcode'] = request.form['zipcode']
        form_data['zipcode_error'] = 'You can only write numbers for your zipcode!'
    print(f'type(user["zipcode"]) : {type(user["zipcode"])}')


def validation():
    valid = True;
    if len(user['name']) < 3 or len(user['name']) > 25:
        form_data['name_error'] = 'Name needs to have more than 3 und less than 25 characters!'
        valid = False;
        print('name_error')
    if len(user['surname']) < 3 or len(user['surname']) > 25:
        form_data['surname_error'] = 'Surname needs to have more than 3 und less than 25 characters!'
        valid = False;
    if len(user['address']) < 3:
        form_data['address_error'] = 'Address needs to have more than 3 characters!'
        valid = False;
    if len(user['city']) < 3:
        form_data['city_error'] = 'City needs to have more than 3 characters!'
        valid = False;
    if len(user['email']) < 1:
        form_data['email_error'] = 'Invalid email!'
        valid = False;

    if is_user_ready_exist():
        form_data['name_error'] = 'Name already exists!'
        valid = False;
    return valid


def is_user_ready_exist():
    user_from_list = find_user()
    return user_from_list is not None


def find_user():
    # for u in user_list gehe alle benutzer in der liste durch
    print(f"user: {user}")
    print(f"user_list: {len(user_list)}")
    for item in user_list:
        print(f"item: {item}")
    filtered_user = [item for item in user_list if 'name' in item and item['name'] == user['name']]
    if filtered_user is not None and len(filtered_user) > 0:
        return filtered_user[0]
    return None


@app.route('/register/confirm/')
def data_confirmation():
    global user
    user_list.append(user)  # füge der neu registrierte user in die liste
    write_user_list_to_file()
    return render_template('confirmed.html', user=user)


def write_user_list_to_file():
    with open(USER_FILE_NAME, 'w') as json_file:
        json.dump(user_list, json_file)  # schreibe die benutzerliste in die datei


@app.route('/user-list/')
def list_of_user():

    return render_template('user_list.html', user_list=load_user())
