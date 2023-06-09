from flask import Blueprint, request, jsonify, make_response
import json
from src import db


comments = Blueprint('comments', __name__)

@comments.route('/comments/', methods=['GET'])
def get_comments():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT * FROM Comments')

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


@comments.route('/comments/<commentID>/', methods=['GET'])
def get_comment(commentID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT * FROM Comments WHERE comment_id = {}'.format(commentID))

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

@comments.route('/comments/<commentID>/replies/', methods=['GET'])
def get_replies(commentID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT * FROM Comments WHERE replying_to = {}'.format(commentID))

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

@comments.route('/comments/<commentID>/likes/', methods=['GET'])
def get_comment_likes(commentID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT * FROM Comment_Likes WHERE comment_id = {}'.format(commentID))

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

    if json_data ==[]:
        return "Comment has no likes. "
    else:
        return jsonify(json_data)

@comments.route('/comments/<commentID>/dislikes/', methods=['GET'])
def get_comment_dislikes(commentID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT * FROM Comment_Dislikes WHERE comment_id = {}'.format(commentID))

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

    if json_data ==[]:
        return "Comment has no dislikes. "
    else:
        return jsonify(json_data)

@comments.route('/comments/<commentID>/like-dislike-count/', methods=['GET'])
def get_comment_like_dislike_counts(commentID):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # get the number of likes and dislikes for the given comment ID
    sql = """
    SELECT Comments.comment_id, COUNT(Comment_Likes.comment_id) as likes, COUNT(Comment_Dislikes.comment_id) as dislikes
    FROM Comments
    LEFT JOIN Comment_Likes ON Comment_Likes.comment_id=Comments.comment_id
    LEFT JOIN Comment_Dislikes ON Comments.comment_id=Comment_Dislikes.comment_id
    WHERE Comments.comment_id = {}
    GROUP BY comment_id;
    """

    # use cursor to query the database for a list of comments
    cursor.execute(sql.format(commentID))

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


@comments.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comment(comment_id): 

    #insert data into a SQL statement
    sql = """
    DELETE FROM Comments WHERE comment_id = {};
    """.format(comment_id,comment_id)

    # execute SQL statement
    cursor = db.get_db().cursor()
    cursor.execute(sql)
    db.get_db().commit()

    return "success"

@comments.route('/comments/', methods=['PUT'])
def edit_comment(): 

    #get json data from post
    data = request.get_json()

    # load fields from json
    comment_id = data["comment_id"]
    content = data["content"]
    
    #insert data into a SQL statement
    stmnt = f"UPDATE Comments SET content = '{content}' WHERE comment_id = {comment_id}"

    # execute SQL statement
    cursor = db.get_db().cursor()
    cursor.execute(stmnt)
    db.get_db().commit()

    return "success"

@comments.route('/comments/<commentID>/', methods=['POST'])
def reply_to_comment(commentID):

    #get json data from post
    data = request.get_json()

    # load fields from json
    content = data["content"]
    comment_author = data["comment_author"]

    #get parent book from target comment
    cursor = db.get_db().cursor()
    cursor.execute("SELECT parent_book FROM Comments WHERE comment_id = {}".format(commentID))
    data = cursor.fetchall()
    parent_book = data[0][0]

    #insert data into a SQL statement
    stmnt = f"INSERT INTO Comments (content, parent_book, comment_author) VALUES ('{content}', '{parent_book}', '{comment_author}')"

    # execute SQL statement
    cursor.execute(stmnt)
    db.get_db().commit()

    return "success"