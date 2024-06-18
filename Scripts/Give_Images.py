import mysql.connector
from QueryBuilder import QueryBuilder
import SQL_Database as DB

index = [0, 0]

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="17MySQL03_",
  database="filteredImages"
)
mycursor = mydb.cursor()

def Give_Image_Right_FWRD():
    index[1] = (index[1] + 1) % len(DB.paths_right)
    path = "Sorted/" + DB.paths_right[index[1]]
    return path

def Give_Image_Left_FWRD():
    index[0] = (index[0] + 1) % len(DB.paths_left)
    path = "Sorted/" + DB.paths_left[index[0]]
    return path

def Give_Image_Right_BCK():
    index[1] = (index[1] - 1) % len(DB.paths_right)
    path = "Sorted/" + DB.paths_right[index[1]]
    return path

def Give_Image_Left_BCK():
    index[0] = (index[0] - 1) % len(DB.paths_left)
    path = "Sorted/" + DB.paths_left[index[0]]
    return path
