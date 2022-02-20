from flask import Flask, render_template, request, redirect
app = Flask(__name__)

name = ''


@app.route("/form/")
def form():
    return render_template('form.html', loginData={'name': name})


@app.route("/form/save", methods=['POST'])
def save_form():
    global name
    name = request.form['name']
    password = request.form['password']
    print(f'save_form called, name:{name}, password:{password}')
    return redirect('/form/')
