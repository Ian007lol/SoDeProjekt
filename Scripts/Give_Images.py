import mysql.connector
from QueryBuilder import QueryBuilder
import SQL_Database as DB

index = [1, 1]
index_2 = [1, 1]

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="17MySQL03_",
  database="filteredImages"
)
mycursor = mydb.cursor()
builder = QueryBuilder()

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

def Give_Date_Right_FWRD():
    index_2[1] = (index_2[1] + 1) % len(DB.Right_Date_List)
    date = DB.Right_Date_List[index_2[1]]
    return date

def Give_Date_Left_FWRD():
    index_2[0] = (index_2[0] + 1) % len(DB.Left_Date_List)
    date = DB.Left_Date_List[index_2[0]]
    return date

def Give_Date_Right_BCK():
    index_2[1] = (index_2[1] - 1) % len(DB.Right_Date_List)
    date = DB.Right_Date_List[index_2[1]]
    return date

def Give_Date_Left_BCK():
    index_2[0] = (index_2[0] - 1) % len(DB.Left_Date_List)
    date = DB.Left_Date_List[index_2[0]]
    return date