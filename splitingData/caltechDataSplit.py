# # Creating Train / Val / Test folders (One time use)
import os
import numpy as np
import shutil
import random

# root dataset path for caltech
root_dir = r'C:\files\sem5\Machine Learning\project\datasets\caltech' # data root path
classes_in_dir = [] #total labels

# full dataset path
all_classes_dir = r'C:\files\sem5\Machine Learning\project\datasets\caltech\full_caltech_dataset\\'

# append all the class name folders in the main full dataset
all_classes = os.listdir(all_classes_dir)
for cls in all_classes:
    classes_in_dir.append(cls)


train_dir = root_dir+'\\train\\'
test_dir = root_dir +'\\test\\'

# remove comments

# create train, test directories
os.mkdir(train_dir)
os.mkdir(test_dir)

# create sub directories in the test, train
for cls in all_classes:
    print(cls)
    os.mkdir(train_dir+cls)
    os.mkdir(test_dir+cls)


for single_cls_name in all_classes:
    # get single class image names path
    single_class_full_dir = all_classes_dir+single_cls_name
    # get single class image names
    imgs_in_single_class_dir = os.listdir(single_class_full_dir)
    # take 20% from that to test
    samp_take = int(len(imgs_in_single_class_dir)*0.2)
    # generate random numbers 20% size numbers( we got 20% size in the above step) from 0 to len of that single class dir
    res = random.sample(range(0, len(imgs_in_single_class_dir)), samp_take)   # to generate random number list
    # take those random res numbers and take those images names into test and remaining into train
    test_img_list = [imgs_in_single_class_dir[nm] for nm in res]

    # select those images which are not part in test set
    train_img_list = [imgs_in_single_class_dir[nm] for nm in range(0, len(imgs_in_single_class_dir)) if nm not in res]

    # test_img_list, train_img_list are only image names not image path names
    # pass these test_img_list, train_img_list into a loops to make a copy of the images into respective dir

    # Copy-pasting images
    # for test set images generation
    for nm in test_img_list:
        # source, destination
        shutil.copy(single_class_full_dir +'/'+ nm, test_dir + single_cls_name +'/' + nm)

    # for train set images generation
    for nm in train_img_list:
        # source, destination
        shutil.copy(single_class_full_dir + '/' + nm, train_dir + single_cls_name + '/' + nm)


