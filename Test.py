import cv2
import numpy as np
import os
from PIL import Image
import time
import cProfile

def add_two_numbers():

    return

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".bmp"): # add file types as needed
            with Image.open(os.path.join(folder, filename)) as img:
                img_np = np.array(img)  # convert image to numpy array
                img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)  # convert image to BGR

                if img_bgr[0][0].tolist() != [154,203,102] and img_bgr[0][0].tolist() != [150,190,110]:
                    if img_bgr.shape == (1920,1080,3):
                        if  (img_bgr[1800][450].tolist() == [52,113,0] 
                            or img_bgr[1800][325].tolist() == [52,113,0] 
                            or img_bgr[1800][575].tolist() == [52,113,0] 
                            or img_bgr[1800][700].tolist() == [52,113,0] 
                            or img_bgr[1800][825].tolist() == [52,113,0] 
                            or img_bgr[1800][950].tolist() == [52,113,0]
                            or img_bgr[1800][450].tolist() == [38,12,145] 
                            or img_bgr[1800][325].tolist() == [38,12,145] 
                            or img_bgr[1800][575].tolist() == [38,12,145] 
                            or img_bgr[1800][700].tolist() == [38,12,145] 
                            or img_bgr[1800][825].tolist() == [38,12,145]  
                            or img_bgr[1800][950].tolist() == [38,12,145]):
                                yield img_bgr
                    else:
                        yield img_bgr


def sample_size(folder):
    counter = 0
    for files in os.listdir(folder):
        if files.endswith(".bmp"):
            counter = counter + 1
    return counter        
    

#load folder name
folder = "smmiMai_Test"
img_test = cv2.imread("smmiMai_Test\screen-left-2022-05-29-17-10.bmp")
sampleSize = sample_size(folder)
counter = 0
image = []
#Start timer to know the computing time of our method
start = time.time()

#load the all the images in the folder
images = load_images_from_folder(folder)
for img in images:
    counter = counter +1
    image.append(img)

#stop the timer
end = time.time()
print(
    f"""
Computing the basic filter for the images with a sample size of {sampleSize}
{sampleSize-counter} images were filtered out, leaving {counter} usable images
({end - start}s)
""",
        )

#pixel_info = images[0]
# Now display the image
cv2.imshow("test", cv2.resize(image[2], (500, 1000)))
cv2.waitKey(0)