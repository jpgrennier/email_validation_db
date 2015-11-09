from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('mydb')
# print "hello, I've started the server"
@app.route('/')
def index():
	email = mysql.fetch("SELECT * FROM email")
	return render_template('index.html', email=email)
@app.route('/email', methods=['POST'])
def create():
    query = "INSERT INTO email (email, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(request.form['email'])
    print query
    mysql.run_mysql_query(query)
    return redirect('/')
app.run(debug=True)