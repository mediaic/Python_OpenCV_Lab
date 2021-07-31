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
## filtering
cv2.filter2D()
## PCA Compute
mean,eigenvectors = cv2.PCACompute(matrix,mean=None)

## min, max
np.min(), np.max()
## dot
np.dot()
## flatten
np.flatten()
## stack list of array
np.stack(np_list)

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

## Useful function

def mse(raw,recon):
    return ((raw-recon) **2).mean()
#-----------------Lab2-----------------------
## Numpy scipy
# concatenate
np.concatenate()
# mean 
np.mean()
## matrix multiplication
np.matmul()
## create meshgrid
np.meshgrid()



