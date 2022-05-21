"""
auto-marking
"""

import cv2 as cv
import pyautogui
import time
import numpy as np


def gama_transfer(img, power1):
    if len(img.shape) == 3:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = 255*np.power(img/255, power1)
    img = np.around(img)
    img[img > 255] = 255
    out_img = img.astype(np.uint8)
    return out_img


def edge_position(img_path):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    img = gama_transfer(img, 1.5)
    array = np.array(img)
    height, width = array.shape
    for i in range(height):
        for j in range(width):
            if array[i][j] <= 53:
                array[i][j] = 0
            else:
                array[i][j] = 255
    result = array.astype(np.uint8)
    result = cv.GaussianBlur(result, (27, 27), 0)
    result = cv.Canny(result, 50, 150)
    return result


if __name__ == '__main__':
    width_pro, height_pro = 2880/1440, 1800/900
    print(pyautogui.size())
    pyautogui.click(1410, 214, button='left')
    time.sleep(3)
    height_left_x, height_left_y = pyautogui.position()
    print('OK')
    time.sleep(3)
    low_right_x, low_right_y = pyautogui.position()
    width, height = low_right_x - height_left_x, low_right_y - height_left_y
    pyautogui.screenshot(region=(int(height_left_x*width_pro), int(height_left_y*height_pro), int(width*width_pro),
                                 int(height*height_pro))).save("/Users/jackrich/Desktop/auto/screenshot.png")
    edge_img = edge_position("/Users/jackrich/Desktop/auto/screenshot.png")
    print(edge_img.shape)
    edge_img = np.array(edge_img)
    edge_img_height, edge_img_width = edge_img.shape
    up_coo, down_coo = [], []
    for i in range(0, edge_img_width, 50):
        tem_coo = []
        for j in range(edge_img_height):
            if edge_img[j][i] == 255:
                tem_coo.append((i, j))
        if len(tem_coo) != 0:
            up_coo.append(tem_coo[0])
            down_coo.append(tem_coo.pop())
    down_coo.reverse()
    total_coo = up_coo + down_coo
    print(total_coo)
    first_point = [int(total_coo[0][0]/width_pro)+height_left_x, int(total_coo[0][1]/height_pro)+height_left_y]
    for item in total_coo:
        x, y = item
        x, y = int(x/width_pro)+height_left_x, int(y/height_pro)+height_left_y
        pyautogui.click(x, y, button='left')
    pyautogui.click(first_point[0], first_point[1], button='left')
    # edge_img = edge_img.astype(np.uint8)
    # cv.imshow('r', edge_img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


