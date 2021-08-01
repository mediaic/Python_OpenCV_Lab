import os
import numpy as np
import argparse
import cv2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', help='ground truth path')
    parser.add_argument('--out', help='your output file path')

    args = parser.parse_args()
    try:
        if (cv2.imread(os.path.join(args.gt)) - cv2.imread(os.path.join(args.out))).sum() == 0.0: print("PASS!")
        else: print("FAIL!")
    except:
        print("FAIL!")

if __name__ == '__main__':
    main()