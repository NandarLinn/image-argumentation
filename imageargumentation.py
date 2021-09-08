import cv2
from skimage.exposure import rescale_intensity
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io
import numpy as np
import os
import argparse

ap = argparse.ArgumentParser()

ap.add_argument('-imgpath','--image_dir',help = 'path of test image',default="test_image")
args = ap.parse_args()

Extension=".jpg"

def multiply_image(image,R,G,B):
    image=image*[R,G,B]
    cv2.imwrite(output_path+"/Multiply-"+str(R)+"*"+str(G)+"*"+str(B)+Extension, image)

def gausian_blur(image,blur):
    image = cv2.GaussianBlur(image,(5,5),blur)
    cv2.imwrite(output_path+"/GausianBLur-"+str(blur)+Extension, image)

def averageing_blur(image,shift):
    image=cv2.blur(image,(shift,shift))
    cv2.imwrite(output_path + "/AverageingBLur-" + str(shift) + Extension, image)

def median_blur(image,shift):
    image=cv2.medianBlur(image,shift)
    cv2.imwrite(output_path + "/MedianBLur-" + str(shift) + Extension, image)

def bileteralBlur(image,d,color,space):
    image = cv2.bilateralFilter(image, d,color,space)
    cv2.imwrite(output_path + "/BileteralBlur-"+str(d)+"*"+str(color)+"*"+str(space)+ Extension, image)

def erosion_image(image,shift):
    kernel = np.ones((shift,shift),np.uint8)
    image = cv2.erode(image,kernel,iterations = 1)
    cv2.imwrite(output_path + "/Erosion-"+"*"+str(shift) + Extension, image)

def dilation_image(image,shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.dilate(image,kernel,iterations = 1)
    cv2.imwrite(output_path + "/Dilation-" + "*" + str(shift)+ Extension, image)

def opening_image(image,shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(output_path + "/Opening-" + "*" + str(shift)+ Extension, image)

def closing_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(output_path + "/Closing-" + "*" + str(shift) + Extension, image)

def morphological_gradient_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite(output_path + "/Morphological_Gradient-" + "*" + str(shift) + Extension, image)

def top_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imwrite(output_path + "/Top_Hat-" + "*" + str(shift) + Extension, image)

def black_hat_image(image, shift):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(output_path + "/Black_Hat-" + "*" + str(shift) + Extension, image)

argumented_img_path = "argumented_img_path/"
if not os.path.exists(argumented_img_path):
    os.mkdir(argumented_img_path)

# image_file="Resize-450*400.jpg"
final_string = ""
for img in os.listdir(args.image_dir):
    window_count = 0
    if not img.startswith('.'):
        final_string +="Image title : " +img+"\n"
        image = os.path.join(args.image_dir,img)

        #get image name to construct folder
        folder_name = os.path.splitext(img)[0]
        output_path = argumented_img_path+ folder_name
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        print(image)
        image=cv2.imread(image)


        multiply_image(image,0.5,1,1)
        multiply_image(image,1,0.5,1)
        multiply_image(image,1,1,0.5)
        multiply_image(image,0.5,0.5,0.5)

        multiply_image(image,0.25,1,1)
        multiply_image(image,1,0.25,1)
        multiply_image(image,1,1,0.25)
        multiply_image(image,0.25,0.25,0.25)

        multiply_image(image,1.25,1,1)
        multiply_image(image,1,1.25,1)
        multiply_image(image,1,1,1.25)
        multiply_image(image,1.25,1.25,1.25)

        multiply_image(image,1.5,1,1)
        multiply_image(image,1,1.5,1)
        multiply_image(image,1,1,1.5)
        multiply_image(image,1.5,1.5,1.5)


        gausian_blur(image,0.25)
        gausian_blur(image,0.50)
        gausian_blur(image,1)
        gausian_blur(image,2)
        gausian_blur(image,4)

        averageing_blur(image,5)
        averageing_blur(image,4)
        averageing_blur(image,6)

        median_blur(image,3)
        median_blur(image,5)
        median_blur(image,7)

        bileteralBlur(image,9,75,75)
        bileteralBlur(image,12,100,100)
        bileteralBlur(image,25,100,100)
        bileteralBlur(image,40,75,75)

        erosion_image(image,1)
        erosion_image(image,3)
        erosion_image(image,6)

        dilation_image(image,1)
        dilation_image(image,3)
        dilation_image(image,5)


        opening_image(image,1)
        opening_image(image,3)
        opening_image(image,5)

        closing_image(image,1)
        closing_image(image,3)
        closing_image(image,5)

        morphological_gradient_image(image,5)
        morphological_gradient_image(image,10)
        morphological_gradient_image(image,15)

        top_hat_image(image,200)
        top_hat_image(image,300)
        top_hat_image(image,500)

        black_hat_image(image,200)
        black_hat_image(image,300)
        black_hat_image(image,500)