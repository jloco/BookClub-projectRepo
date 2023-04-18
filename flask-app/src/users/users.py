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