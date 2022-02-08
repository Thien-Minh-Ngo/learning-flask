from flask import Flask, render_template, jsonify
import datetime
app = Flask(__name__)



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
def user():
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


@app.route("/layout/")
def page_with_flex():
    return render_template('japy.html')


@app.route("/dogs/")
def dogs():
    dogs = ["rdp1", "rdp2", "rdp3", "rdp4", "rdp5", "rdp6"]
    return render_template('dogs.html', dogs=dogs)


@app.route("/main_page/")
def main_page():
    return render_template('main_page.html')


@app.route("/cats/")
def cats():
    cats = ["rcp1", "rcp2", "rcp3", "rcp4", "rcp5", "rcp6"]
    return render_template('cats.html', cats=cats)

