from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
app = Flask(__name__)
mysql = MySQLConnector('mydb')
# print "hello, I've started the server"
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
	email = mysql.fetch("SELECT * FROM email")
	return render_template('index.html', email=email)
@app.route('/email', methods=['POST'])
def create():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
 		flash("Invalid Email Address!")
	else:
		query = "INSERT INTO email (email, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(request.form['email'])
		print query
		mysql.run_mysql_query(query)
	return redirect('/')
app.run(debug=True)