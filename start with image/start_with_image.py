import cv2

# Read image
'''img = cv2.imread('Image name', flag value -1 indicates that it loads 
# image with alpha channel'''
img = cv2.imread('lena.jpg', -1)
print(img)

# cv2.imshow('Windows name wherein it will be shown', image name)
cv2.imshow('Image', img)

'''in documentatoin it has been written that the below line of code can be 
alternative for the 64 bit machine. but my pc is working nice without it.
cv2.waitKey(0) & oxFF
'''
'''when this method takes 0 as argument, it will nom be disappeared 
until you close it'''
# when you press any key, its value is stored in k
k = cv2.waitKey(0)
# 27 means you pressed the escape key, then it destroy all windows
if k == 27:
    # It destroys all windows which you have created
    cv2.destroyAllWindows()
# eilf you press s key (s button from keyboard), it saves the image
elif k == ord('s'):
    # Write or save image 
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows() 

'''
here, ord() is a builtin function that takes key name (as argument) 
which you want to press.
'''