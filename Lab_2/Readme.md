# Lab_2 

This is the simplified version of DLCV course HW2.

**What you will learn :**
- Color Segmentation
- Texture Segmentation
- Feature Descriptor
- Recognition with Bag of Visual Words


**Directory Tree**
```
|__Lab1
|  |__ Readme.md
|  |__ filterBank.mat
|  |__ mountain.jpg
|  |__ zebra.jpg
```

**Requirement**

You can only use the python packages below:

 - numpy
 - cv2 (opencv)
 - matplotlib
 - sklearn
 - scipy  ( only  for reading .mat file)

## 1. Color & Texture Segmentation

<img src="./image/zebra.jpg" alt="zebra" width="180px"/> <img src="./image/combine_RGB_zebra.jpg" alt="zebra" width="180px"/> <img src="./image/mountain.jpg" alt="mountain" width="160px"/><img src="./image/combine_RGB_mountain.jpg" alt="mountain" width="160px"/>
### Image data and filter banks
-	**filterBank.mat** :  The given .mat file contains a set of 38 filters. This filter bank is stored as a 49x49x38 matrix.
-	**Images** :  *zebra.jpg* and *mountain.jpg*
### Problems
1. **Color Segmentation** :   

