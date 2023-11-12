import cv2

class Calculate:

    def __init__(self, target_x, target_y, placing_image, on_which_placed, 
                         target_x2, target_y2):
        self.target_x = target_x
        self.target_y = target_y
        self.placing_image = placing_image
        self.on_which_placed = on_which_placed
        self.target_x2 = target_x2
        self.target_y2 = target_y2

    def put_image_on_bgimage(self):
        football_img = cv2.imread(self.placing_image)

        football_height, football_width, _ = football_img.shape
        print('football_img.shape: ', football_img.shape)
        print('football_height: ', football_height)
        print('football_width: ', football_width)

        background_img = cv2.imread(self.on_which_placed)

        self.top_left_x = self.target_x
        self.top_left_y = self.target_y
        self.bottom_right_x = self.target_x + football_width
        self.bottom_right_y = self.target_y + football_height

        self.target_region = background_img[self.top_left_y:self.bottom_right_y, 
                                    self.top_left_x:self.bottom_right_x]
        target_region_height, target_region_width, _ = self.target_region.shape
        print('target_region.shape: ', self.target_region.shape)
        print('target_region_height: ', target_region_height)
        print('target_region_width: ', target_region_width)
        football_img_resized = cv2.resize(football_img, (target_region_width, 
                                                        target_region_height))

        background_img[self.top_left_y:self.bottom_right_y, 
                    self.top_left_x:self.bottom_right_x] = football_img_resized

        self.top_left_x2 = self.target_x2
        self.top_left_y2 = self.target_y2
        self.bottom_right_x2 = self.target_x2 + football_width
        self.bottom_right_y2 = self.target_y2 + football_height

        self.target_region2 = background_img[self.top_left_y2:self.bottom_right_y2, 
                                        self.top_left_x2:self.bottom_right_x2]
        target_region2_height, target_region2_width, _ = self.target_region2.shape
        print('target_region2.shape: ', self.target_region2.shape)
        print('target_region2_height: ', target_region2_height)
        print('target_region2_width: ', target_region2_width)
        football_img_resized2 = cv2.resize(football_img, 
                        (target_region2_width, target_region2_height))
        background_img[self.top_left_y2:self.bottom_right_y2, 
                    self.top_left_x2:self.bottom_right_x2] = football_img_resized2

        cv2.imshow('Result', background_img)

target_x = 700
target_y = 370
placing_image = 'Redball.PNG'
on_which_placed = 'stadium4.jpeg'

target_x2 = 100
target_y2 = 370

# Create object
obj = Calculate(target_x, target_y, placing_image, on_which_placed, 
                         target_x2, target_y2)
# Function call
obj.put_image_on_bgimage()

cv2.waitKey(0)
cv2.destroyAllWindows()