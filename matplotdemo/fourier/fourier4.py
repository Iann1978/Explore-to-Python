print("fourier4")


import cv2
import numpy as np
import scipy.fft as fp
import matplotlib.pyplot as plt
import scipy.misc as misc

srcimg = cv2.imread('Elizabeth_Tower.jpg', cv2.IMREAD_GRAYSCALE)
srcimg = srcimg.astype(float)
srcimg = srcimg/srcimg.max()
plt.set_cmap('gray')
plt.title("srcimg")
plt.imshow(srcimg)
plt.show()

fimg = fp.fft2(srcimg)
am = np.abs(fimg)
pm = np.angle(fimg)
logam = np.log(am)
logam = fp.fftshift(logam)
plt.subplot(121)
plt.title('logam')
plt.imshow(logam)
plt.subplot(122)
plt.title('pm')
plt.imshow(pm)
plt.show()

logamex = cv2.rectangle(logam, (5,5), (logam.shape[1]-6, logam.shape[0]-6), 5)
plt.title('logamex')
plt.imshow(logamex)
plt.show()


logam = fp.ifftshift(logam)
covam = np.exp(logam)
covfimg = covam * np.cos(pm) + covam * np.sin(pm) * 1j
covimg = fp.ifft2(covfimg)
plt.set_cmap('gray')
plt.title("covimg")
plt.imshow(covimg.real)
plt.show()







