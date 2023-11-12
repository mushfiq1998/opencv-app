import cv2

# Read image
# img = cv2.imread('Image name', flag value 0 indicates gray scale image)
# img = cv2.imread('lena.jpg', 0)
# img = cv2.imread('Image name', flag value 1 indicates colored image)
# img = cv2.imread('lena.jpg', 1)
# img = cv2.imread('Image name', flag value -1 indicates that it loads image with alpha channel)
img = cv2.imread('Sakib.jpg', -1)
# img = cv2.imread('lena.jpg', -1)
print(img)

# Show image. the image is shown for mili second, then it disappeared
# cv2.imshow('Windows name wherein it will be shown', image name)
cv2.imshow('Image', img)

# 5000 mili seconds = 5 seconds. that means the window will be visible
# for 5 seconds, then it will be disappeared. 
# cv2.waitKey(5000)
'''when this method takes 0 as argument, it will not be disappeared 
until you close it'''
cv2.waitKey(0)

# It destroys all windows which you have created
# when we close the window, this method is called
cv2.destroyAllWindows()

# Write or save image 
cv2.imwrite('lena_copy.png', img) 
