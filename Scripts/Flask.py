from flask import Flask, send_file, request, jsonify
import Give_Images as GI
from QueryBuilder import QueryBuilder
import mysql.connector
from flask import Flask
from flask_cors import CORS
import SQL_Database as DB
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
def add_sort_menu_1(): builder.add_condition("menu_1","menu = 1")
def add_sort_menu_2(): builder.add_condition("menu_2","menu = 2")
def add_sort_menu_3(): builder.add_condition("menu_3","menu = 3")
def add_sort_menu_4(): builder.add_condition("menu_4","menu = 4")
def add_sort_menu_5(): builder.add_condition("menu_5","menu = 5")
def add_sort_menu_6(): builder.add_condition("menu_6","menu = 6")

def remove_sort_menu_1(): builder.remove_condition("menu_1")
def remove_sort_menu_2(): builder.remove_condition("menu_2")
def remove_sort_menu_3(): builder.remove_condition("menu_3")
def remove_sort_menu_4(): builder.remove_condition("menu_4")
def remove_sort_menu_5(): builder.remove_condition("menu_5")
def remove_sort_menu_6(): builder.remove_condition("menu_6")

def add_sort_KVV_TRUE(): builder.add_condition("kvv_true","kvv = 1")
def add_sort_KVV_FALSE(): builder.add_condition("kvv_false","kvv = 0")

def remove_sort_KVV_TRUE(): builder.remove_condition("kvv_true")
def remove_sort_KVV_FALSE(): builder.remove_condition("kvv_false")

def sort_by_date(): builder.add_order_by("Date ASC")

def add_between_date(Start_date, End_date): builder.add_between_condition('date_range', 'date', Start_date, End_date)
def remove_between_date(): builder.add_between_condition('date_range')


def Fetch_IMG():
    DB.paths_left.clear()
    DB.paths_right.clear()
    DB.Right_Date_List.clear()
    DB.Left_Date_List.clear()
    sort_by_date()
    query = builder.build()
    mycursor.execute(query)
    rows = mycursor.fetchall()

    for row in rows:
        if "right" in row[-1]:
            DB.paths_right.append(row[-1])
            DB.Right_Date_List.append(row[-3])
        if "left" in row[-1]:
            DB.paths_left.append(row[-1])
            DB.Left_Date_List.append(row[-3])



@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/imageRight_FWRD')
def serve_image_Right_FWRD():
    image_path = GI.Give_Image_Right_FWRD()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageLeft_FWRD')
def serve_image_Left_FWRD():
    image_path = GI.Give_Image_Left_FWRD()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageRight_BCK')
def serve_image_Right_BCK():
    image_path = GI.Give_Image_Right_BCK()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

@app.route('/imageLeft_BCK')
def serve_image_Left_BCK():
    image_path = GI.Give_Image_Left_BCK()  # replace with your function name
    return send_file(image_path, mimetype='image/gif')

# Routes to expose date retrieval functions
@app.route('/dateRight_FWRD')
def serve_date_Right_FWRD():
    date = GI.Give_Date_Right_FWRD()
    return jsonify({'date': date}), 200

@app.route('/dateLeft_FWRD')
def serve_date_Left_FWRD():
    date = GI.Give_Date_Left_FWRD()
    return jsonify({'date': date}), 200

@app.route('/dateRight_BCK')
def serve_date_Right_BCK():
    date = GI.Give_Date_Right_BCK()
    return jsonify({'date': date}), 200

@app.route('/dateLeft_BCK')
def serve_date_Left_BCK():
    date = GI.Give_Date_Left_BCK()
    return jsonify({'date': date}), 200


@app.route('/fetchImages')
def fetch_images():
    Fetch_IMG()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images fetched successfully'})  # Optionally return a response

@app.route('/sort_KVV_TRUE')
def sort_KVV_TRUE():
    add_sort_KVV_TRUE()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by KVV TRUE successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_KVV_TRUE')
def REMOVE_sort_KVV_TRUE():
    remove_sort_KVV_TRUE()  # Call your function here,
    sort_by_date()

    return jsonify({'message': 'Images sort bye KVV TRUE removed successfully'})  # Optionally return a response

@app.route('/sort_KVV_FALSE')
def sort_KVV_FALSE():
    add_sort_KVV_FALSE()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by KVV FALSE successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_KVV_FALSE')
def REMOVE_sort_KVV_FALSE():
    remove_sort_KVV_FALSE()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort by KVV FALSE removed successfully'})  # Optionally return a response

@app.route('/sort_menu_1')
def sort_menu_1():
    add_sort_menu_1()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 1 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_1')
def REMOVE_sort_menu_1():
    remove_sort_menu_1()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 1 successfully'})  # Optionally return a response

@app.route('/sort_menu_2')
def sort_menu_2():
    add_sort_menu_2()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 2 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_2')
def REMOVE_sort_menu_2():
    remove_sort_menu_2()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 2 successfully'})  # Optionally return a response

@app.route('/sort_menu_3')
def sort_menu_3():
    add_sort_menu_3()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 3 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_3')
def REMOVE_sort_menu_3():
    remove_sort_menu_3()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 3 successfully'})  # Optionally return a response

@app.route('/sort_menu_4')
def sort_menu_4():
    add_sort_menu_4()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 4 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_4')
def REMOVE_sort_menu_4():
    remove_sort_menu_4()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 4 successfully'})  # Optionally return a response

@app.route('/sort_menu_5')
def sort_menu_5():
    add_sort_menu_5()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 5 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_5')
def REMOVE_sort_menu_5():
    remove_sort_menu_5()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 5 successfully'})  # Optionally return a response

@app.route('/sort_menu_6')
def sort_menu_6():
    add_sort_menu_6()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sorted by menu 6 successfully'})  # Optionally return a response

@app.route('/REMOVE_sort_menu_6')
def REMOVE_sort_menu_6():
    remove_sort_menu_6()  # Call your function here
    sort_by_date()
    return jsonify({'message': 'Images sort removed by menu 6 successfully'})  # Optionally return a response

@app.route('/sort_between')
def sort_between():
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    
    add_between_date(start_date, end_date)  # Call your function here with start_date and end_date
    sort_by_date()
    return jsonify({'message': 'Dates added to query builder'}), 200

@app.route('/REMOVE_sort_between')
def remove_sort_between():
    remove_between_date()
    sort_by_date()
    return jsonify({'message': 'Dates deleted to query builder'}), 200

if __name__ == "__main__":
    app.run(port=5000)