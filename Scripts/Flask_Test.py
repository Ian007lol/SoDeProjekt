from flask import Flask, send_file
import Give_Images  # replace with your python file name
from QueryBuilder import QueryBuilder
from flask import Flask
from flask_cors import CORS


builder = QueryBuilder()

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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

@app.route('/add_sort_menu_1', methods=['POST'])
def add_sort_menu_1():
    builder.add_condition("menu = 1")
    return 'OK', 200


if __name__ == "__main__":
    app.run(port=5000)