from flask import Blueprint, request, jsonify, make_response
import json
from src import db


users = Blueprint('users', __name__)

@users.route('/users/', methods=['GET'])
def get_users():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT * FROM Users')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

    #return jsonify(json_data)


@users.route('/users/<userID>/', methods=['GET'])
def get_user(userID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT * FROM Users WHERE user_id = {}'.format(userID))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@users.route('/users/<userID>/bookshelf/', methods=['GET'])
def get_user_bookshelf(userID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT * FROM Bookshelf WHERE user_id = {}'.format(userID))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@users.route('/users/<userID>/currently_reading/', methods=['GET'])
def get_user_reading(userID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT * FROM Currently_Reading WHERE user_id = {}'.format(userID))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@users.route('/users/<userID>/comments/', methods=['GET'])
def get_user_comments(userID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of users
    cursor.execute('SELECT * FROM Comments WHERE comment_author = {}'.format(userID))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@users.route('/users/<userID>/works/', methods=['GET'])
def get_user_works(userID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    sql = """
    SELECT Books.book_id, Books.title, Books.num_pages, Books.num_chapters
    FROM Books
    JOIN Written_By ON Books.book_id = Written_By.book_id
    JOIN Users ON Written_By.user_id = Users.user_id
    WHERE Users.user_id = {}
    """
    # use cursor to query the database for a list of users
    cursor.execute(sql.format(userID))

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@users.route('/users/', methods=['POST'])
def add_user():
    #get json data from post
    data = request.get_json()

    # load fields from json
    username = data["username"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    bio = data["bio"]
    country_code = data["country_code"]
    company = data["company"]
    
    #insert data into a SQL statement
    stmnt = f"INSERT INTO Users (username,first_name,last_name,bio,country_code,company) VALUES ('{username}', '{first_name}', '{last_name}', '{bio}', '{country_code}', '{company}')"

    # execute SQL statement
    cursor = db.get_db().cursor()
    cursor.execute(stmnt)
    db.get_db().commit()

    return "success"

@users.route('/users/<userID>/username/', methods=['PUT'])
def change_username(userID):
    #get json data from post
    data = request.get_json()

    # load fields from json
    new_username = data["username"]
    
    #insert data into a SQL statement
    stmnt = f"UPDATE Users SET username = {new_username} WHERE user_id = {userID}"

    # execute SQL statement
    cursor = db.get_db().cursor()
    cursor.execute(stmnt)
    db.get_db().commit()

    return "success"

@users.route('/users/<userID>/', methods=['DELETE'])
def delete_user(userID):
    
    #insert data into a SQL statement
    stmnt = f"DELETE FROM Users WHERE user_id = {userID}"

    # execute SQL statement
    cursor = db.get_db().cursor()
    cursor.execute(stmnt)
    db.get_db().commit()

    return "success"
