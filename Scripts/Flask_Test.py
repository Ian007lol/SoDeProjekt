from flask import Flask, send_file, request, jsonify

import Give_Images  # replace with your python file name
from QueryBuilder import QueryBuilder
import mysql.connector
from flask import Flask
from flask_cors import CORS
import SQL_Database as DB
import Filter
app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17MySQL03_",
    database="filteredImages"
)
builder = QueryBuilder()

mycursor = mydb.cursor()
def add_sort_menu_1(): builder.add_condition("menu = 1")
def add_sort_menu_2(): builder.add_condition("menu = 2")
def add_sort_menu_3(): builder.add_condition("menu = 3")
def add_sort_menu_4(): builder.add_condition("menu = 4")
def add_sort_menu_5(): builder.add_condition("menu = 5")
def add_sort_menu_6(): builder.add_condition("menu = 6")

def remove_sort_menu_1(): builder.remove_condition("menu = 1")
def remove_sort_menu_2(): builder.remove_condition("menu = 2")
def remove_sort_menu_3(): builder.remove_condition("menu = 3")
def remove_sort_menu_4(): builder.remove_condition("menu = 4")
def remove_sort_menu_5(): builder.remove_condition("menu = 5")
def remove_sort_menu_6(): builder.remove_condition("menu = 6")

def add_sort_KVV_TRUE(): builder.add_condition("kvv = 1")
def add_sort_KVV_FALSE(): builder.add_condition("kvv = 0")

def remove_sort_KVV_TRUE(): builder.remove_condition("kvv = 1")
def remove_sort_KVV_FALSE(): builder.remove_condition("kvv = 0")

def sort_by_date(): builder.add_order_by("Date")
def Fetch_IMG():
    DB.paths_left.clear()
    DB.paths_right.clear()
    query = builder.build()
    mycursor.execute("Select * from images where id = 1")
    rows = mycursor.fetchall()

    for row in rows:
        if "right" in row[-1]:
            DB.paths_right.append(row[-1])
        if "left" in row[-1]:
            DB.paths_left.append(row[-1])

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/imageRight_FWRD')
def serve_image_Right_FWRD():
    image_path = Give_Images.Give_Image_Right_FWRD()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageLeft_FWRD')
def serve_image_Left_FWRD():
    image_path = Give_Images.Give_Image_Left_FWRD()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageRight_BCK')
def serve_image_Right_BCK():
    image_path = Give_Images.Give_Image_Right_BCK()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageLeft_BCK')
def serve_image_Left_BCK():
    image_path = Give_Images.Give_Image_Left_BCK()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/fetchImages')
def fetch_images():
    Fetch_IMG()  # Call your function here
    return jsonify({'message': 'Images fetched successfully'})  # Optionally return a response


if __name__ == "__main__":
    app.run(port=5000)