# encoding: utf-8
import cv2
import numpy as np
import roi_merge as roi_
import util_funs as util
from get_rects import *
# import pytesseract


def main(img):
    region = get_rects(img)
    roi_solve = roi_.roi_solve(region)
    roi_solve.rm_inside()
    roi_solve.rm_overlop()
    region = roi_solve.merge_roi()
    # region = util.sort_region(region)
    # region = util.get_targetRoi(region)

    for i in range(len(region)):
        rect2 = region[i]
        w1, w2 = rect2[0], rect2[0] + rect2[2]
        h1, h2 = rect2[1], rect2[1] + rect2[3]
        box = [[w1, h2], [w1, h1], [w2, h1], [w2, h2]]
        cv2.drawContours(img, np.array([box]), 0, (0, 255, 0), 1)
        '''
        if i == 0:
            cv2.imwrite(r"d:\代码" + str(i) + ".jpg", img[h1:h2, w1:w2])
        else:
             cv2.imwrite(r"d:\号码" + str(i) + ".jpg", img[h1:h2, w1:w2])
        '''
        # cv2.imshow(pytesseract.image_to_string((img), lang='chi_sim'), img)
        # cv2.imshow('img', img[h1:h2, w1:w2])
        cv2.imshow('img', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread(r"d:\fp1.png")

    main(img)

