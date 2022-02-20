from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    return valid
