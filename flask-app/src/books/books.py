from flask import Blueprint, request, jsonify, make_response
import json
from src import db


books = Blueprint('books', __name__)

@books.route('/books', methods=['GET'])
def get_books():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT book_id, title, num_pages, num_chapters, language_code FROM Books')

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

@books.route('/books/<bookID>', methods=['GET'])
def get_book(bookID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT book_id, title, num_pages, num_chapters, language_code, content FROM Books WHERE book_id = {}'.format(bookID))

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
