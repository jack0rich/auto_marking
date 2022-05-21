"""
调试参数
"""

import cv2 as cv
import pyautogui
import numpy as np

# 检查屏幕分辨率
print('屏幕分辨率：', pyautogui.size())

# 检查截屏分辨率
pyautogui.screenshot().save("随便输一个地址保存截屏，以png图片名结尾")
img = cv.imread('刚刚输的那个地址', cv.IMREAD_GRAYSCALE)
print('截屏分辨率：', img.shape)


