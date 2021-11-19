from getFeatures import GetFeatures
import cv2
import os

# these is used to save all images features into a csv file
train_Path = r'C:\files\sem5\Machine Learning\project\datasets\inria\train\\'

# get the names of the images in the train path directory
train_images_names = os.listdir(train_Path)

# open or create if not exists featuresData csv
output = open('featuresData.csv', "w")

for img_name in train_images_names:
    img_path = train_Path+img_name
    image = cv2.imread(img_path)

    # get the features from the getFeatures file for a particular image
    features = GetFeatures(image)

    features = [str(f) for f in features]
    output.write("%s,%s\n" % (img_name, ",".join(features)))
