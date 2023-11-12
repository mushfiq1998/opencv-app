import cv2

class Image:
    def __init__(self, capturing_image, alpha_channel_value, pressed_key):
        self.capturing_image = capturing_image
        self.alpha_channel_value = alpha_channel_value
        self.pressed_key = pressed_key
    
    def start_with_image(self):
        img = cv2.imread(self.capturing_image, self.alpha_channel_value)
        print(img)
        cv2.imshow('Image', img)

        k = cv2.waitKey(self.pressed_key)
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('lena_copy.jpg', img)
            cv2.destroyAllWindows() 

capturing_image = 'lena.jpg'
alpha_channel_value = -1 
pressed_key = 0

# Create object
picture = Image(capturing_image, alpha_channel_value, pressed_key)
# Function call
picture.start_with_image()
