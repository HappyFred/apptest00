from flask import Flask, render_template, request, redirect, url_for
import db       # Functions and variables for connecting to MySQL using MySQLclient
import connect  # Imports your db connection details from connect.py
import mysql.connector  # MySQL Connector/Python

app = Flask(__name__)

# Initialize database connection
db.init_db(
    app, connect.dbuser, connect.dbpass, connect.dbhost, connect.dbname, connect.dbport
)


@app.route("/")
def home():
    """Render (display) the Home page using home.html.  
       No data required for this page."""     
    return render_template("home.html")

@app.route("/person-list")
def person_list():
    """Display a list of people in the people table.""" 
    cursor = db.get_cursor()
    # Create SQL query
    qstr = "SELECT * FROM people"
    # Send to database
    cursor.execute(qstr)
    # Save data into variable
    person_list = cursor.fetchall()

    return render_template("person_list.html",
                           person_list=person_list)

