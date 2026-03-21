import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt

# 파일 선택기 열어서 이미지 파일 선택
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일 열기",\
                    filetypes = (("*.jpg","*jpg"),("*.png","png")))

src = cv2.imread(files[0])
histColor = ('b', 'g', 'r')
for i in range(3):
    hist = cv2.calcHist(images=[src],channels=[i],mask=None,
                        histSize=[256],ranges=[0,256])
    plt.plot(hist,color=histColor[i])
plt.show()