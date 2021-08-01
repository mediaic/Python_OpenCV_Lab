import numpy as np
import numpy.linalg as LA
import cv2


# u, v are N-by-2 matrices, representing N corresponding points for v = T(u)
# this function should return a 3-by-3 homography matrix
def solve_homography(u, v):
    """
    This function should return a 3-by-3 homography matrix,
    u, v are N-by-2 matrices, representing N corresponding points for v = T(u)
    :param u: N-by-2 source pixel location matrices
    :param v: N-by-2 destination pixel location matrices
    :return:
    """
    # TODO: 1.forming A

    # TODO: 2.solve H with A

    return H

def warping(src, dst, H, ymin, ymax, xmin, xmax):
    """
    Perform forward/backward warpping without for loops. i.e.
    for all pixels in src(xmin~xmax, ymin~ymax),  warp to destination
          (xmin=0,ymin=0)  source                       destination
                         |--------|              |------------------------|
                         |        |              |                        |
                         |        |     warp     |                        |
    forward warp         |        |  --------->  |                        |
                         |        |              |                        |
                         |--------|              |------------------------|
                                 (xmax=w,ymax=h)

    for all pixels in dst(xmin~xmax, ymin~ymax),  sample from source
                            source                       destination
                         |--------|              |------------------------|
                         |        |              | (xmin,ymin)            |
                         |        |     warp     |           |--|         |
    backward warp        |        |  <---------  |           |__|         |
                         |        |              |             (xmax,ymax)|
                         |--------|              |------------------------|

    :param src: source image
    :param dst: destination output image
    :param H:
    :param ymin: lower vertical bound of the destination(source, if forward warp) pixel coordinate
    :param ymax: upper vertical bound of the destination(source, if forward warp) pixel coordinate
    :param xmin: lower horizontal bound of the destination(source, if forward warp) pixel coordinate
    :param xmax: upper horizontal bound of the destination(source, if forward warp) pixel coordinate
    :param direction: indicates backward warping or forward warping
    :return: destination output image
    """

    # TODO: 1.meshgrid the (x,y) coordinate pairs

    # TODO: 2.reshape the destination pixels as N x 3 homogeneous coordinate

    # TODO: 3.apply H_inv to the destination pixels and retrieve (u,v) pixels, then reshape to (ymax-ymin),(xmax-xmin)

    # TODO: 4.calculate the mask of the transformed coordinate (should not exceed the boundaries of source image)

    # TODO: 5.sample the source image with the masked and reshaped transformed coordinates

    # TODO: 6. assign to destination image with proper masking


    return dst

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
