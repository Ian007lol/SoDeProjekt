import cv2
import numpy as np
import os
from PIL import Image
import time

def add_two_numbers():

    return

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".bmp"): # add file types as needed
            with Image.open(os.path.join(folder, filename)) as img:
                img_np = np.array(img)  # convert image to numpy array
                img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)  # convert image to BGR

                if img_bgr[0][0].tolist() != [154,203,102] and img_bgr[0][0].tolist() != [150,190,110]:
                    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)  # convert image to BGR
                    images.append(img_bgr)
    return images

def sample_size(folder):
    counter = 0
    for files in os.listdir(folder):
        if files.endswith(".bmp"):
            counter = counter + 1
    return counter        
    

#load folder name
folder = "smmiMai_Test"
sampleSize = sample_size(folder)
#Start timer to know the computing time of our method
start = time.time()

#load the all the images in the folder
images = load_images_from_folder(folder)

#stop the timer
end = time.time()

print(
    f"""
Computing the basic filter for the images with a sample size of {sampleSize}
{sampleSize-len(images)} images were filtered out, leaving {len(images)} usable images
({end - start}s)
""",
        )

#pixel_info = images[0]
# Now display the image
#cv2.imshow("test", images[0])
#cv2.waitKey(0)

