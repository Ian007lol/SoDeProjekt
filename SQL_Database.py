import mysql.connector
import cv2
import numpy as np
import os
from PIL import Image
import time
filnam = []

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="17MySQL03_",
  database="filteredImages"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE filteredImages")

#mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, menu INT, KVV BOOL, Date DATE)")
#mycursor.execute("SHOW TABLES")

def insert_images_to_DB(folder):
    counter = 1
    for filename in os.listdir(folder):
        if filename.endswith(".bmp"): # add file types as needed
                with Image.open(os.path.join(folder, filename)) as img:
                    img_np = np.array(img)  # convert image to numpy array
                    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)  # convert image to BGR
                    sql = "INSERT INTO images (menu, KVV, Date, screen) VALUES (%s, %s, %s, %s)"
                    os.rename(folder+"/"+filename, folder+"/"+str(counter)+" "+filename)
                    counter = counter + 1
                    if "left" in filename: 
                        if img_bgr[1800][325].tolist() == [52,113,0] :
                            val = (1, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][450].tolist() == [52,113,0] : 
                            val = (2, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][575].tolist() == [52,113,0] :
                            val = (3, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][700].tolist() == [52,113,0] :
                            val = (4, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][825].tolist() == [52,113,0]:
                            val = (5, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][950].tolist() == [52,113,0]:
                            val = (6, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][325].tolist() == [38,12,145]:
                            val = (1, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][450].tolist() == [38,12,145]:
                            val = (2, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][575].tolist() == [38,12,145]:
                            val = (3, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][700].tolist() == [38,12,145] :
                            val = (4, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][825].tolist() == [38,12,145]:
                            val = (5, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][950].tolist() == [38,12,145]:
                            val = (6, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "left")
                            mycursor.execute(sql, val)

                    if "right" in filename:
                        if img_bgr[1800][140].tolist() == [52,113,0]:
                            val = (1, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][260].tolist() == [52,113,0]: 
                            val = (2, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][380].tolist() == [52,113,0]:
                            val = (3, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][500].tolist() == [52,113,0]:
                            val = (4, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][620].tolist() == [52,113,0]:
                            val = (5, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][740].tolist() == [52,113,0]:
                            val = (6, True, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][140].tolist() == [38,12,145]:
                            val = (1, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][260].tolist() == [38,12,145]:
                            val = (2, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][380].tolist() == [38,12,145]:
                            val = (3, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][500].tolist() == [38,12,145]:
                            val = (4, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][620].tolist() == [38,12,145]:
                            val = (5, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                        if img_bgr[1800][740].tolist() == [38,12,145]:
                            val = (6, False, filename[-20:-10]+" "+filename[-9:-7]+":"+filename[-6:-4]+":00", "right")
                            mycursor.execute(sql, val)
                    

def sort_menuç():
    return      

    
                    
#load folder name
folder = "Sorted"
start = time.time()
insert_images_to_DB(folder)
end = time.time()

print(
    f"""
Content uploaded to DB
({end - start}s)
""",
        )

mydb.commit()






