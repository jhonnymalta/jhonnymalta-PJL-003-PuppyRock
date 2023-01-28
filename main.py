from flask import Flask,render_template,request, flash,redirect,url_for


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
    username = request.args.get('username')
    email = request.args.get('email')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num = any(c.isdigit() for c in username)

    is_valid_username = lower_letter and upper_letter and num
    if is_valid_username:
        return render_template('thankyou.html',username=username)
    else:
        flash('The username must contain a cappital letter and a number')
        return redirect(url_for('signup'))
    


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True) # Turn off debug= true to producton deploy