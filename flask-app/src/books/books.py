from flask import Blueprint, request, jsonify, make_response
import json
from src import db


books = Blueprint('books', __name__)

@books.route('/books/', methods=['GET'])
def get_books():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    sql = """
    SELECT Books.book_id, Books.title, Books.num_pages, Books.num_chapters, COUNT(Bookshelf.user_id) as readers, AVG(Bookshelf.rating) as average_rating
    FROM Books
    JOIN Bookshelf ON Books.book_id = Bookshelf.book_id
    GROUP BY Books.book_id
    """

    # use cursor to query the database for a list of books
    cursor.execute(sql)

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

@books.route('/books/<bookID>/', methods=['GET'])
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

@books.route('/books/<bookID>/comments/', methods=['GET'])
def get_book_comments(bookID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT * FROM Comments WHERE parent_book = {}'.format(bookID))

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

@books.route('/books/<bookID>/likes/', methods=['GET'])
def get_book_likes(bookID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT * FROM Book_Likes WHERE book_id = {}'.format(bookID))

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

@books.route('/books/<bookID>/dislikes/', methods=['GET'])
def get_book_dislikes(bookID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of books
    cursor.execute('SELECT * FROM Book_Dislikes WHERE book_id = {}'.format(bookID))

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

@books.route('/books/<bookID>/like-dislike-count/', methods=['GET'])
def get_book_like_dislike_counts(bookID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # get the number of likes and dislikes for the given book ID
    sql = """
    SELECT Books.book_id, COUNT(Book_Likes.book_id) as likes, COUNT(Book_Dislikes.book_id) as dislikes
    FROM Books
    LEFT JOIN Book_Likes ON Book_Likes.book_id=Books.book_id
    LEFT JOIN Book_Dislikes ON Books.book_id=Book_Dislikes.book_id
    WHERE Books.book_id = {}
    GROUP BY book_id;
    """

    # use cursor to query the database for a list of books
    cursor.execute(sql.format(bookID))

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
