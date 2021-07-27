from flask import Flask, redirect, render_template, url_for, request
import bot

app = Flask (__name__)
browser = 1
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():
    #return "Hello World!"
    return render_template('home.html')

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        email = request.form.get("exampleInputEmail1")
        licenseNumber = request.form.get("number")
        expiry = request.form.get("expiry")
        thisMonth = request.form.get("thisMonth") == "thisMonth"
        nextMonth = request.form.get("nextMonth") == "nextMonth"
        test = request.form.get("test")
        secret = [email, licenseNumber, expiry, thisMonth, nextMonth, test]

        
        browser = bot.Browser(*secret)
        browser.open()
        browser.login()
        browser.gtest()
        browser.search()

        return render_template('login.html')

    else:
        return render_template('login.html')
