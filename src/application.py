from flask import Flask, render_template, jsonify, url_for, request, flash
from werkzeug.utils import redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
import datetime
app = Flask(__name__)

number: int = 4


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/user")
def api():
    # TODO function aus eigebundenen Modulen (Datei) aufrufen
    return {
        "name": "Thien Minh",
        "age" : 16
    }


@app.route("/home/")
def home():
    return render_template('index.html')


@app.route("/<page_name>/")
def test(page_name):
    return render_template('test.html', page_name=page_name)


@app.route("/users/", methods=['GET'])
def user1():
    users = [
        {
          "firstname": "Kevin",
          "surname": "Ngo",
          "birthday": "15.09.2021"
        },
        {
          "firstname": "Franz",
          "surname": "Friedrich",
          "birthday": "28.12.2021"
        },
        {
          "firstname": "Hans",
          "surname": "Walter",
          "birthday": "10.04.2022"
        },
        {
          "firstname": "Peter",
          "surname": "Ulrich",
          "birthday": "08.02.2020"
        },
        {
          "firstname": "Frieda",
          "surname": "Barin",
          "birthday": "01.02.2018"
        }
    ]
    return jsonify(users)


@app.route("/cars/", methods=['Get'])
def cars():
    cars = [
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": "2018"
        },
        {
            "brand": "Porsche",
            "model": "944",
            "year": "1989"
        },
        {
            "brand": "Volkswagen",
            "model": "Polo II",
            "year": "1997"
        },
        {
            "brand": "Audi",
            "model": "e-tron GT",
            "year": "2021"
        }
    ]
    return jsonify(cars)


@app.route("/dogs/", methods=['GET', 'POST'])
def dogs():
    return render_template('dogs.html', number=number)


@app.route("/dogs/number", methods=['POST'])
def dogs_number():
    global number
    number = int(request.form['number'])
    print(f'save_form called, name:{number}')
    return redirect('/dogs/')


@app.route("/main_page/")
def main_page():
    return render_template('main_page.html')


@app.route("/cats/", methods=['GET', 'POST'])
def cats():
    return render_template('cats.html', number=number)


@app.route("/cats/number", methods=['POST'])
def cats_number():
    global number
    number = int(request.form['number'])
    print(f'save_form called, name:{number}')
    return redirect('/cats/')


class User:
    pass


name = ''


@app.route("/form/", methods=['GET'])
def forms():
    return render_template('form.html', name=name)


@app.route("/form/save", methods=['POST'])
def save_form():
    global name
    name = request.form["name"]
    return redirect('/form/')





