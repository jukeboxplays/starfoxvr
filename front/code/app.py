from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import json
import requests
from forms import LoginForm, RegisterForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    r = ""
    form = LoginForm()
    if form.validate_on_submit():
        r = get_json('login',
                      json.dumps({'username': form.username.data,
                                  'password': form.password.data
                      }))        
    
    return render_template('login.html', form=form, title=r)


@app.route('/register', methods=['GET', 'POST'])
def register():
    r = ""
    form = RegisterForm()
    if form.validate_on_submit():
        r = post_json('register',
                      json.dumps({'username': form.username.data,
                                  'email': form.email.data,
                            'password': form.password.data}))
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form, title=r)

@app.route("/api")
def api():
    r = get_banco()
    return render_template("home.html", title=r)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/download")
def download():
    return render_template("download.html")

@app.route("/us")
def us():
    return render_template("us.html")

def get_json(path, json):
    r = requests.get('http://back:5000/' + path,
                      headers={'Content-Type': 'application/json'},
                      data=json)
    try:
        response = json.loads(r.text)
    except:
        response = r
    return response

def post_json(path, json):
    r = requests.post('http://back:5000/api/v1/' + path,
                      headers={'Content-Type': 'application/json'},
                      data=json)
    try:
        response = json.loads(r.text)
    except:
        response = r
    return response

                                 
def get_banco():
    r = requests.post('http://back:5000/',
                      headers={'Content-Type': 'application/json'},
                      data=json.dumps({'text': 'lalala'}))
    try:
        response = json.loads(r.text)
    except:
        response = r
    return response
    
