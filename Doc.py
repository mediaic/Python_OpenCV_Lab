import cv2
import numpy as np 

## Load image
img = cv2.imread('Lenna.jpg') ## BGR 
## Grayscale
img = cv2.imread('Lenna.jpg',0)

## Show image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Save image
cv2.imwrite('test.jpg',img)

## Show image with matplotlib
import matplotlib.pyplot as plt 
plt.imshow(img[:,:,::-1]) ## To RGB
plt.show()

plt.imshow(img,cmap='gray')
plt.show()

#-----------------Lab1-----------------------
## Resize
cv2.resize()
## Color space 
cv2.cvtColor()
## smoothing
cv2.blur(),cv2.GaussianBlur(),cv2.mediaBlur()
## PCA Compute
mean,eigenvectors = cv2.PCACompute(matrix,mean=None)

## min, max
np.min(), np.max()
## dot
np.dot()
## flatten
np.flatten()

## KNN
from sklearn.neighbors import KNeighborsClassifier
# 宣告
KNN = KNeighborsClassifier(args)
# Feed Training Data
KNN.fit(X_train,Y_train)
# Predict Class
KNN.predict(X_test)
# 直接告訴你acc 
KNN.score(X_test,Y_test)

#-----------------Lab2-----------------------
## Opencv
# ColorMap
cv2.applyColorMap()
# Padding
cv2.copyMakeBorder() #use cv2.BORDER_REFLECT
# SURF
cv2.xfeatures2d.SURF_create()
cv2.drawKeyPoints()

## Numpy scipy
# Save & load
np.save(),np.load()
# concatenate
np.concatenate()
# mean 
np.mean()
# reciprocal
np.reciprocal()
# load .mat file 
import scipy.io as sio 
sio.loadmat()
# Euclidean distance
from scipy.spatial import distance
distance.euclidean()

## Sklearn 
# Kmeans
from sklearn.cluster import KMeans
Kmeans = KMeans(args)
Kmeans.fit_predict(X)

## Matplotlib
import matplotlib.pyplot as plt
plt.figure()
plt.bar(x,y)
plt.title()
plt.xlabel()
plt.ylabel()
plt.savefig()


