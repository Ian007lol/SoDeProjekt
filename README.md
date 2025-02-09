# SoftwareDesign - User Interaction Visualizer 

## About the project
This script is able to take a folder as an input. After uploading it, the folder gets a basic filter, so all broken and unnecessary images are sorted out. After that you are able to filter the images after specific categories.

## Authors
Ian Zamora Bella<br>
Lena Kirrmann<br>
Franziska Hartmann<br>

## Getting started
First of all: We pushed the .venv into the git. So in order to get it to work you can either delete the .venv and create your own and add the needed libraries or you can open the 'pyvenv.cfg' and change in line 4 the user to your own user. This way you won't need to download the libraries.

In case you haven't worked with Python and/or OpenCV before, here is a quick guide to install both:
You can install Python from [python.org](https://www.python.org/downloads/). The recommended
version is `3.12.2` or above. Usually, the Python installation includes the dependency management tool pip out of the box. If not, download and
install it from [pip.pypa.io](https://pip.pypa.io/en/stable/installation/). The minimum required version is `19.3` and above.
Lastly, you need to install OpenCV in case you don't have it installed. Just write: 
```shell
pip install opencv-python
```
in the terminal. <br>
The same goes for the libraries: pillow, MySQL, Numpy, and OS. <br>
You also need MySQL Workbench for this to work. <br>

Keep in mind that this was only tested with Microsoft! <br>
The HTML was tested on OperaGX and Firefox. <br>

## How to run the code
First, the database file is available as a Dump in the project folder, which can be imported. However, before doing so you need to create the schema with the corresponding name "filteredimages" locally in MySQL. After that, you can import it.<br>
Keep in mind that the server for the database has to be active or the code wont work.<br>
To connect correctly to the database, you must change the password for the connection in both "SQL_Database" (Line 22) and "Flask" (Line 15) to your own password.

In default, the 'Sorted' folder should already have the filtered images. If that's the case, you can just run the 'Flask' script and open the HTML script via Live Server from the vsc extensions. <br>

If you want to start the basic filter, you have to delete all images inside the 'Sorted' folder. After that you have to run the 'main.py' script. Then you have to run the 'SQL_Database.py'. You need to comment out the line 126 'insert_images_to_DB(folder)' after you have run it once or the database will have some problems. Lastly you need to run the 'Flask.py' script and go to the 'Images.html'. Right click into the script and open it via Live Server.<br>

Have fun!
