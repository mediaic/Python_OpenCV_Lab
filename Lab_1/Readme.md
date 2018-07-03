# Lab_1 
**What you will learn :**
 - Image Operation
 - Image Smoothing
 - Image Denoising
 - Image PCA & Classification 


**Directory Tree**
```
|__Lab1
|  |__ Readme.md
|  |__ Face_dataset/
|  |__ fig.jpg
```

**Requirement**
You can only use the python packages below:

 - numpy
 - cv2 (opencv)
 - matplotlib
 - sklearn

## 1. Image Operation

1.	Load "**fig.jpg**"
2.	Resize the image (**fig.jpg**) with scaling factor = 0.25 and try different interpolation methods.
	
	- cv2.INTER_NEAREST&nbsp;&nbsp;&nbsp;  [fig_1.jpg] 
	- cv2.INTER_LINEAR     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [fig_2.jpg] 
	- cv2.INTER_CUBIC     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [fig_3.jpg]
3. Resize the image (**fig_3.jpg**) with scaling factor = 4 and try different interpolation methods.
	
	- cv2.INTER_NEAREST&nbsp;&nbsp;&nbsp;  [fig_4.jpg] 
	- cv2.INTER_LINEAR     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [fig_5.jpg] 
	- cv2.INTER_CUBIC     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [fig_6.jpg]
4.  Convert the color space to *YCbCr* for the upsampled images and the <u>original image</u>, and compute **PSNR** values for "**Y**" channel to the original image (**fig.jpg**).
**Q**: Which one performs better?

## 2. Image Smoothing
1.	Load "**fig.jpg**" with **gray** scale.
2.	Compute three kinds of smoothing methods and observe the results.
	
	- **Averaging**   [fig_7.jpg]
		- kernel size = 5
		- cv2.blur()
	-   **Gaussian Filtering** [fig_8.jpg], [fig_9.jpg]
		- kernel size = 5
		- 2 kinds of std: (x,y) = (5,5) and (3,3)
		- cv2.GaussianBlur()
	- **Median Filtering**  [fig_10.jpg]
		- kernel size = 5
		- cv2.medianBlur()

## 3. Image Denoising
1.	Load "**fig.jpg**" with **gray** scale.
### Add Noise
2.	 **Gaussian noise** [fig_gau.jpg]
		- mean = 0, std = 5
		- hint: *np.random.normal()*
3.	 **Salt and Pepper noise** [fig_sp.jpg]
		- s vs p : 50% for each,  all_noise_amount = 1%
		- hint: use *np.random.randint()* to generate the salt or pepper coordinates
		- salt =255,  pepper = 0	
### Denoise
4. Apply **Gaussian filter** and **Median filter** on  the image with Gaussian noise. 
	**Q** :Which one  performs better?
	
5. Apply **Gaussian filter** and **Median filter** on  the image with Salt&Pepper noise.
	**Q** :Which one  performs better?

## 4. Image PCA  Analysis
The dataset you need is under `Face_dataset/` directory, which contains 56×46 pixel face images of 40 different subjects (classes), and 10 images available for each subject. Note that, i_j.png means personi_imagej . Now you have to split the dataset into two subsets (i.e., training and test sets). The first subset contains the **first 6 images** of each subject, while the second subset include the remaining images. Thus, a total of 6 × 40 = 240 images are in the training set, while 160 images in the test set.

1. Perform PCA on the **training set**. Save the **mean face** and the first **three** eigenfaces.
	- save to [mean.png], [1.png], [2.png], [3.png]
	- Be careful the values in eigenvectors after PCA !  (*cv2.PCACompute()*)
	- hint: 　255 * (shifted **x**/ max(shifted **x**))
2. Take **7_2.png**, and project it onto the above PCA eigenspace. Reconstruct this image using the first n = 3, 100 eigenfaces. For each n, compute the mean square error (MSE) between the reconstructed face image and "1_1.png". Please save these reconstructed images, and record the corresponding MSE values.
3. Apply the **k-nearest neighbors classifier** to recognize **test set** images. For simplicity, try k={1,3} and n = {3,100}.  Report the recognition rate on the test set with different (k,n) pairs.
	- hint: *sklearn.neighbors.KNeighborsClassifier()*


