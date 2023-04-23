# pylint: disable-all

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')

@app.route('/places')
def places():
  return render_template("places.html")

@app.route('/aboutus')
def aboutus():
  return render_template("aboutus.html")

@app.route('/loginsignup')
def loginsignup():
  return render_template("loginsignup.html")

@app.route('/submit', methods=['GET','POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']


    row = pd.DataFrame([[fname, lname, email]])

    row.to_csv('csv/subusers.csv', mode='a')

    return render_template('base.html')

@app.route('/submit1', methods=['GET','POST'])
def submit1():
  email1 = request.form['email1']
  username = request.form['username']
  password = request.form['password']
  confirm_pass = request.form['confirm_pass']
  row = pd.DataFrame([[email1, username, password]])

  row.to_csv('csv/logins.csv', mode='a')

  return render_template('loginsignup.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


