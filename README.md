# Content Based Image Retrieval
This is basic content Based Image Retrieval project

## first setp preprocessing 
<ul>
  <li>split the dataset into train and test sets </li>
  <li> here i used 80 : 20 as the ratio of train and test split </li>
 </ul>

## CBIR with color histogram
<ul>
  <li> convert each image in HSV formate </li>
  <li> divide image into 5 segments : top-left, top-right, bottom-right, bottom-left, center as ecllipse </li>
  <li> histogram bins : here 8, 12, 3 bin sizes </li>
  <li> for 1 segment of the image 8*12*3 features </li>
  <li> for 5 segments 5*8*12*3 == 1,440 -- > this is the feature vector size for the single image</li>
 </ul>
 
 ![image](https://user-images.githubusercontent.com/82259446/142576985-b75b601f-a3b7-45ad-b7b4-768af5ac7748.png)

### Training:
<ul>
<li> Divide the image into 5 segments </li>
<li> Finding feature vector by using bins</li>
<li> Storing the feature vectors in a bag</li>
</ul>

<br/>


### Testing :
<ul>
<li> For test Image finding feature vector by using bins</li>
<li> Measure the simmilarity of the image with the features present in our bag</li>
</ul>
 
![colorhist](https://user-images.githubusercontent.com/82259446/136047789-798d3917-1ed0-4cf5-8e25-1db1c89f8440.gif)

## The Second section of the project that is ***color histogram CBIR*** is the idea taken from <a href="https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/">pyimagesearch </a>
### Thanks to pyimagesearch, for making color histogram CBIR blog as open source
