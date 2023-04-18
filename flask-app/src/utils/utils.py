from flask import Blueprint, request, jsonify, make_response
import json
from src import db


utils = Blueprint('utils', __name__)

@utils.route('/countries/', methods=['GET'])
def get_countries():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT country_code as value, country_name as label FROM Countries')

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

@utils.route('/languages/', methods=['GET'])
def get_languages():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of comments
    cursor.execute('SELECT language_code as value, language_name as label FROM Languages')

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

