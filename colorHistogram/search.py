from getFeatures import GetFeatures
from searcher import Searcher
import cv2


# train_Path = r'C:\files\sem5\Machine Learning\project\datasets\inria\train\\'
# test_img_path = r'C:\files\sem5\Machine Learning\project\datasets\inria\test\104001.jpg'

train_Path = r'C:\files\sem5\Machine Learning\project\datasets\inria\full_inria_dataset\\'
# test_img_path = r'C:\files\sem5\Machine Learning\project\datasets\inria\full_inria_dataset\106600.jpg'

test_img_path = r'C:\files\sem5\Machine Learning\project\datasets\caltech\full_caltech_dataset\anchor\image_0042.jpg'

# load the query image and describe it
query = cv2.imread(test_img_path)
features = GetFeatures(query)


# perform the search on this features we got from the image
results = Searcher(features)

# display the query imageq
# this is used for resizing the window because images are too big to show
im = cv2.resize(query, (250, 250))
cv2.imshow("Query", im)


# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    result = cv2.imread(train_Path + resultID)
    im = cv2.resize(result, (250, 250))
    cv2.imshow("Result", im)
    cv2.waitKey(0)