import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt #berupa fungsi yang memberikan perubahan pada gambar
import math 
import pandas as pd
import imutils.paths as path
from tqdm import tqdm


def penentu(imagePaths): #def bisa baris code yang bsa dipanggil berkali2
    # PATH = 'testing/'
    # imagePaths = sorted(list(path.list_images(PATH)))
    # print (imagePaths)


    data = []
    for i in tqdm(imagePaths,desc="load"):
        imgg=cv.imread (i)
        img = cv.cvtColor(imgg, cv.COLOR_BGR2GRAY)#konversi warna frame
        a = cv.resize (img, (128, 128))
        data.append (a) #append nambahin nilai array

    def derajat0 (img):
        max = np.max(img) #mencari nilai tertinggi menemukan terbesar dari iterable
        imgTmp=np.zeros([max+1,max+1])
        for i in range (len(img)):
            for j in range (len(img[i])-1):
                imgTmp[img[i,j],img[i,j+1]] += 1
                
        data= imgTmp+np.transpose(imgTmp)
        tmp=np.sum(data)
                
        for i in range (len (data)):
            for j in range (len (data)):
                data[i,j]/=tmp
        return data

    def derajat45 (img):
        max = np.max(img)
        imgTmp=np.zeros([max+1,max+1])
        for i in range (len (img)-1):
            for j in range (len (img[i])-1):
                imgTmp[img[i+1,j],img[i,j+1]] += 1
                
        data= imgTmp+np.transpose(imgTmp)
        tmp=np.sum(data)
        
        for i in range (len (data)):
            for j in range (len (data)):
                data[i,j]/=tmp
        return data

    def derajat90 (img):
        max = np.max(img)
        imgTmp=np.zeros([max+1,max+1])
        for i in range (len (img)-1):
            for j in range (len (img[i])):
                imgTmp[img[i+1,j],img[i,j]] += 1
                
        data= imgTmp+np.transpose(imgTmp)
        tmp=np.sum(data)
                
        for i in range (len (data)):
            for j in range (len (data)):
                data[i,j]/=tmp
        return data

    def derajat135 (img):
        max = np.max(img)
        imgTmp=np.zeros([max+1,max+1])
        for i in range (len (img)-1):
            for j in range (len (img[i])-1):
                imgTmp[img[i,j],img[i+1,j+1]] += 1
                
        data= imgTmp+np.transpose(imgTmp)
        tmp=np.sum(data)
                
        for i in range (len (data)):
            for j in range (len (data)):
                data[i,j]/=tmp
        return data

    hasil=[]
    for i in tqdm (range (len (data)),desc='glcm'):
        dat=[]
        dat.append(derajat0 (data[i]))
        dat.append(derajat45 (data[i]))
        dat.append(derajat90 (data[i]))
        dat.append(derajat135 (data[i]))
        hasil.append(dat)

    def Contrast (data):
        contras=0
        for i in range (len (data)):
            for j in range (len (data)):
                contras+=data[i,j]*pow(i-j,2)
        return contras
    def Entropy (data):
        entro=0
        for i in range (len (data)):
            for j in range (len (data)):
                if data[i,j] > 0.0:
                    entro += -(data[i,j] * np.log(data[i,j]))
        return entro
    def Homogeneity (data):
        homogen=0
        for i in range (len (data)):
            for j in range (len (data)):
                homogen+=data[i,j]/(1+(pow(i-j,2)))
        return homogen
    def Energy (data):
        ener=0
        for i in range (len (data)):
            for j in range (len (data)):
                ener += data[i,j]**2
        return ener

    data0=[]
    x=['0','45','90','135']

    hasilnya=[]
    for j in tqdm (range(len(hasil)),desc="Ekstraksi GLCM Buah Pepaya"):
        da=[]
        da.append(imagePaths[j])
        for i in hasil[j]:
            dx=Energy (i)
            da.append(dx)

            dh=Homogeneity (i)
            da.append(dh)

            den=Entropy (i)
            da.append(den)

            dco=Contrast (i)
            da.append(dco)
            
        hasilnya.append(da)
    headerssss=['path','Energy0','Homogeneity0','Entropy0','Contrast0'
            ,'Energy45','Homogeneity45','Entropy45','Contrast45'
            ,'Energy90','Homogeneity90','Entropy90','Contrast90'
            ,'Energy135','Homogeneity135','Entropy135','Contrast135']
    df = pd.DataFrame(hasilnya, columns=headerssss)
    df.head()
    pd.set_option('max_columns', None)
    pd.set_option("max_rows", None)
    df.to_csv(r'percobaan.csv', index=False)


