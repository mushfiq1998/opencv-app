import cv2

def start_with_image(capturing_image, alpha_channel_value, pressed_key):
    img = cv2.imread(capturing_image, alpha_channel_value)
    print(img)
    cv2.imshow('Image', img)

    k = cv2.waitKey(pressed_key)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('lena2,jpg', img)
        cv2.destroyAllWindows() 

capturing_image = 'lena.jpg'
alpha_channel_value = -1 
pressed_key = 0

# Function call
start_with_image(capturing_image, alpha_channel_value, pressed_key)
