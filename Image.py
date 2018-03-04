from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

pil_im = Image.open('images.jpg')
pil_road = pil_im.load()
(width, height) = pil_im.size

cell_temp = []
row_temp = [[],[]]
Total_image = [[],[]]

for i in range(0, 5):
    for j in range(0, 5):
        (r, g, b) = pil_road[i,j]
        X = 0.49 * r + 0.31 * g + 0.20 * b
        Y = 0.17697 * r + 0.81240 * g + 0.01063 * b
        Z = 0.00 * r + 0.01 * g + 0.99 * b
        (X, Y, Z) = (X/0.17697, Y/0.17697, Z/0.17697)
        (x, y) = (X/(X+Y+Z), Y/(X+Y+Z))
        cell_temp = np.array([x,y])
        cell_temp = cell_temp.T
        row_temp = np.c_[row_temp,cell_temp]
    print('-----------------')
    print(row_temp,'&',i)
    Total_image = np.vstack([Total_image,row_temp])
    row_temp = [[],[]]

print(Total_image)