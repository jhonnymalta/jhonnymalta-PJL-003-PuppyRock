import os
from flask import Flask,render_template,request, flash,redirect,url_for,abort


from flask_login import login_required,login_user,LoginManager
from data.db_session import create_tables

from models.User import User

from services.PassHashing import hashing_pass

login_manager = LoginManager()

app = Flask(__name__)





app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():

    from data.crud import insert_tutor
    username = request.args.get('username')
    email = request.args.get('email')
    city = request.args.get('city')
    password: str = request.args.get('password')
    print(password)
    password_to_save:str = hashing_pass(password)
    print(password_to_save)

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num = any(c.isdigit() for c in username)

    is_valid_username = lower_letter and upper_letter and num
    if is_valid_username:

        new_tutor = User(
            username = username,
            email = email,
            city = city,
            password = password_to_save
        )
        tutor_created = insert_tutor(new_tutor)
        print(tutor_created)
        return render_template('thankyou.html',username=username)
    else:
        flash('The username must contain a cappital letter and a number')
        return redirect(url_for('signup'))
    



@app.route('/tutor')
@login_required
def tutor():
    from data.crud import get_all_tutors
    lista = get_all_tutors()
    return render_template('tutor.html',lista=lista)
   
    
@app.route('/profile/<id>')
def profile(id):
    from data.crud import get_tutor_by_id
    tutor: User = get_tutor_by_id(id)
    return render_template('profile.html',tutor=tutor)


@app.errorhandler(404)
def page_not_found(e):    
    return render_template('404.html'), 404


@app.route('/login',methods=['GET','POST'])
def login():  
    
    username = request.args.get('username')
    password = request.args.get('password') 

    from data.crud import authentication_user
    user = authentication_user(username,password) 
    print(user)
    if user is not None:
        login_user(user)
        flash('Logged in successfully.')

        next = request.args.get('next')
        # if not is_safe_url(next):
        #     return redirect(url_for('login'))

        return redirect(next or url_for('tutor'))
    return render_template('login.html')


    
    


@login_manager.user_loader
def load_user(user_id):
    from data.crud import get_tutor_by_id
    return get_tutor_by_id(user_id)

login_manager.init_app(app)
login_manager.login_view = 'login'
if __name__ == '__main__':
    #create_tables()
    
    app.run(debug=True) # Turn off debug= true to producton deploy