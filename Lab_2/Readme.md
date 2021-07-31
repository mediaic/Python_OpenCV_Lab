# Lab_2 

This is part of HW3 in NTU Computer Vision: from Recognition to Geometry (CV) course.

**What you will learn :**
- Homography


**Directory Tree**
```
|__Lab2
|  |__ main.py
|  |__ screan.jpg
```

**Requirement**

You can only use the python packages below:
 - python standard library
 - numpy
 - cv2 (opencv) excluding `cv2.findhomography`

## Unwarp the screen

Given the image **screen.jpg** with twisted QRcode, the goal of this lab is to untwist it with homography transformation. The goal can be accomplished with the following steps:

### 1. Complete the function *solve_homography()*

Given two N-by-2 matrices, (u, v), representing N corresponding points for v = T(u), this function should return the 3-by-3 homography matrix.

### 2. Backward Warping

We want to output an **300\*300** image with untwisted QRcode on it. 

- With the corners of the region of QRcode in **screen.jpg** and the corners of the output image, we can construct the homography matrix. 
- To prevent hole on the output image, instead of transforming all the pixels on the region of QRcode in **screen.jpg**, we should search for the pixel value for every pixel on the output image based on the homography matrix. 

**Q**: what is the content of the QRcode?
