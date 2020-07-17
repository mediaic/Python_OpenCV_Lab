import numpy as np
import numpy.linalg as LA
import cv2


# u, v are N-by-2 matrices, representing N corresponding points for v = T(u)
# this function should return a 3-by-3 homography matrix
def solve_homography(u, v):
	# TODO
	return H

def main():

    # Input Initialization 
	corners = np.array([[190, 106], [256, 142], [193, 244], [258, 285]]) # Points [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
	img_path = './screen.jpg'

    # Output initialization (create an output array to save the result)
	new_h, new_w = 300, 300

    # TODO Solving homography matrix for backward warping (hints: instead of solve v = Hu, solve u = (H^-1)v)

    # TODO Backward Warping 
	

	
if __name__ == '__main__':
	main()
