import os
from flask import Flask,render_template,request, flash,redirect,url_for
from data.db_session import create_tables

from models.Tutor import Tutor

app = Flask(__name__)





app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():
    from data.crud import insert_tutor
    username = request.args.get('username')
    email = request.args.get('email')
    city = request.args.get('city')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num = any(c.isdigit() for c in username)

    is_valid_username = lower_letter and upper_letter and num
    if is_valid_username:

        new_tutor = Tutor(
            name = username,
            email = email,
            city = city
        )
        tutor_created = insert_tutor(new_tutor)
        print(tutor_created)
        return render_template('thankyou.html',username=username)
    else:
        flash('The username must contain a cappital letter and a number')
        return redirect(url_for('signup'))
    



@app.route('/home')
def home():
    from data.crud import get_all_tutors
    lista = get_all_tutors()
    return render_template('home.html',lista=lista)

@app.errorhandler(404)
def page_not_found(e):    
    return render_template('404.html'), 404


if __name__ == '__main__':
    #create_tables()
    app.run(debug=True) # Turn off debug= true to producton deploy