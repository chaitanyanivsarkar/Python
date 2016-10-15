import numpy as np
import cv2
form matplotlib import pyplot as plt

img=cv2.imread('fate_zero.jpg',0)
cv2.imshow("Fate Zero",img)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

key=cv2.waitKey(0) & 0xFF
if key == ord('k'):
    cv2.imwrite('Fate Zero.jpeg',img)
    cv2.destroyWindow("Fate Zero")
elif key == 27:
    cv2.destroyWindow("Fate Zero")
