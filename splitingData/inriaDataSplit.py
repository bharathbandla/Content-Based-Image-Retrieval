# # Creating Train / Val / Test folders (One time use)
import os
import numpy as np
import shutil
import random

# root dataset path for inria
root_dir = r'C:\files\sem5\Machine Learning\project\datasets\inria' # data root path

# full dataset path
all_images_dir = r'C:\files\sem5\Machine Learning\project\datasets\inria\full_inria_dataset\\'


train_dir = root_dir+'\\train\\'
test_dir = root_dir +'\\test\\'

# create train, test directories
os.mkdir(train_dir)
os.mkdir(test_dir)

# take all images names, just only names, all_imgs is a list of image names
all_imgs = os.listdir(all_images_dir)

# take 20% data into test data
samp_take = int(len(all_imgs)*0.2)

# generate random 20% numbers( we got this number in the above step
res = random.sample(range(0, len(all_imgs)), samp_take)

# take 20 % image names into a other variable
test_img_list = [all_imgs[nm] for nm in res]

# take other images that are not part in 20% into training data
train_img_list = [ all_imgs[nm] for nm in range(0, len(all_imgs)) if nm not in res]

print(len(test_img_list))
print('...........')
print(len(train_img_list))

# upto now we have train, test image names, not the image paths
# now make a copy into train and test dir

# Copy-pasting images
# for test set images generation
for nm in test_img_list:
    # source, destination
    shutil.copy(all_images_dir +'/'+ nm, test_dir + '/' + nm)

# for train set image generation
for nm in train_img_list:
    shutil.copy(all_images_dir+'/'+nm, train_dir+'/'+nm)


