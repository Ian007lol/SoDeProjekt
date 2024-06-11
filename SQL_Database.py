import mysql.connector
import cv2
import numpy as np
import os
from PIL import Image
import time
import pickle
from QueryBuilder import QueryBuilder
filnam = []
builder = QueryBuilder()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="17MySQL03_",
  database="filteredImages"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE filteredImages")
#mycursor.execute("ALTER TABLE images ADD COLUMN img LONGBLOB")
#mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, menu INT, KVV BOOL, Date DATE)")
#mycursor.execute("SHOW TABLES")

def insert_images_to_DB(folder):
    counter = 1
    for filename in os.listdir(folder):
        if filename.endswith(".bmp"): # add file types as needed
                with Image.open(os.path.join(folder, filename)) as img:
                    img_np = np.array(img)  # convert image to numpy array
                    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)  # convert image to BGR
                    img_bytes = pickle.dumps(img_bgr)
                    sql = "INSERT INTO images (menu, KVV, Date, screen, img) VALUES (%s, %s, %s, %s, %s)"
                    #os.rename(folder+"/"+filename, folder+"/"+str(counter)+" "+filename)
                    #counter = counter + 1
                    if "left" in filename: 
                        if img_bgr[1800][325].tolist() == [52,113,0] :
                            val = (1, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][450].tolist() == [52,113,0] : 
                            val = (2, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][575].tolist() == [52,113,0] :
                            val = (3, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][700].tolist() == [52,113,0] :
                            val = (4, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][825].tolist() == [52,113,0]:
                            val = (5, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][950].tolist() == [52,113,0]:
                            val = (6, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][325].tolist() == [38,12,145]:
                            val = (1, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][450].tolist() == [38,12,145]:
                            val = (2, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][575].tolist() == [38,12,145]:
                            val = (3, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][700].tolist() == [38,12,145] :
                            val = (4, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][825].tolist() == [38,12,145]:
                            val = (5, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][950].tolist() == [38,12,145]:
                            val = (6, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left", img_bytes)
                            mycursor.execute(sql, val)

                    if "right" in filename:
                        if img_bgr[1800][140].tolist() == [52,113,0]:
                            val = (1, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][260].tolist() == [52,113,0]: 
                            val = (2, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][380].tolist() == [52,113,0]:
                            val = (3, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][500].tolist() == [52,113,0]:
                            val = (4, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][620].tolist() == [52,113,0]:
                            val = (5, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][740].tolist() == [52,113,0]:
                            val = (6, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][140].tolist() == [38,12,145]:
                            val = (1, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][260].tolist() == [38,12,145]:
                            val = (2, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][380].tolist() == [38,12,145]:
                            val = (3, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][500].tolist() == [38,12,145]:
                            val = (4, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][620].tolist() == [38,12,145]:
                            val = (5, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                        if img_bgr[1800][740].tolist() == [38,12,145]:
                            val = (6, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right", img_bytes)
                            mycursor.execute(sql, val)
                    

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
     
#load folder name


folder = "Sorted"
start = time.time()
#insert_images_to_DB(folder)
add_sort_menu_4()
add_sort_KVV_FALSE()
sort_by_date()
query = builder.build()
#mydb.commit()




#builder.add_condition("kvv = 1")
#builder.remove_condition("menu = 2")
#query = builder.build()  # This will return "SELECT * FROM images WHERE menu = 2 AND kvv = 1"
mycursor.execute(query)#Variable für Frontend
rows = mycursor.fetchall()
for row in rows:
    # Convert bytes back to numpy array
    rows = pickle.loads(row[5])
    
end = time.time()

print(
    f"""
Content uploaded to DB
({end - start}s)
""",
        )

cv2.imshow("patpat",rows)
cv2.waitKey(0)







