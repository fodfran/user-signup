from flask import Flask, request, redirect, render_template, url_for
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index_form():
    return render_template('index.html', title = "SHINee World Signup")

@app.route("/", methods = ['POST'])
def validate_form():
    username = request.form['username']
    username_error = ''
    password = request.form['password']
    password_error = ''
    verify = request.form['verify']
    verify_error = ''
    email = request.form['email']
    email_error = ''


    #if not username or len(username) < 3 or len(username) > 20 or " " in username:
    if not re.match(r"^\w{3,20}$", username):
        username_error = "That's not a valid username"
        username = ''  
    #if not password or len(password) < 3 or len(password) > 20 or " " in password:
    if not re.match(r"^\w{3,20}$", password):
        password_error = "That's not a valid password"
    if not verify or verify != password:
        verify_error = "Passwords don't match"
    if email: 
        #if '@' not in email or '.' not in email or len(email) < 3 or len(email) > 20 or " " in email:
        if not (re.match(r"^.{3,20}$", email) and re.match(r"^\w+@\w+\.\w+$", email)):    
            email_error = "That's not a valid email"
            email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error = email_error, username=username, email=email, title = "SHINee World Signup")


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username, title = "Welcome")

app.run()