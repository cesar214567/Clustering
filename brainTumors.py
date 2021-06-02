from DBSCAN import DBSCAN
#from KMeans import KMeans
#from MeanShift import MeanShift
from PIL import Image
from scipy import misc
import numpy as np

def read_db():
    i = 1
    file = open("files.txt","r")
    for line in file:
        #     if (i == 1):
        #         i += 1
        #         continue
        print(line)
        points = []
        im = Image.open(line[:-1], 'r').convert("L")
        print(im)
        pix_val=list(im.getdata())
        #pix_val = im.convert("RGB")
        #pix_val=list([] im.getdata())
        pix_val = np.array(im,  dtype="object")
        h,w = len(pix_val),len(pix_val[0])
        print(len(pix_val[0]))
        print(h,w)
        for y in range(h):
            for x in range(w):
                points.append((x*2.5, y*2.5, pix_val[y][x]/2))
        print("----------------DBSCAN---------------")
        DBSCAN(points, i)
        # print("----------------KMeans---------------")
        # KMeans(points,w,h)
        #print("--------------Mean Shift-------------")
        #MeanShift(points,i)
        points.clear()
        

read_db()

        