import cv2

class Calculate:

    def __init__(self, target_x, target_y, placing_image, 
                 on_which_placed, target_x2, target_y2):
        self.target_x = target_x 
        self.target_y = target_y
        self.placing_image = placing_image
        self.on_which_placed = on_which_placed
        self.target_x2 = target_x2 
        self.target_y2 = target_y2

    def put_image_on_bgimage(self):
        self.football_img = cv2.imread(self.placing_image )

        self.football_height, self.football_width, _ = self.football_img.shape
        print('football_img.shape: ', self.football_img.shape)
        print('football_height: ', self.football_height)
        print('football_width: ', self.football_width)

        self.background_img = cv2.imread(self.on_which_placed)

        self.top_left_x = self.target_x
        self.top_left_y = self.target_y
        self.bottom_right_x = self.target_x + self.football_width
        self.bottom_right_y = self.target_y + self.football_height

        self.target_region = self.background_img[
            self.top_left_y:self.bottom_right_y, 
            self.top_left_x:self.bottom_right_x]
        self.target_region_height, self.target_region_width, _ = self.target_region.shape
        print('target_region.shape: ', self.target_region.shape)
        print('target_region_height: ', self.target_region_height)
        print('target_region_width: ', self.target_region_width)
        self.football_img_resized = cv2.resize(self.football_img, 
                (self.target_region_width, self.target_region_height))

        self.background_img[self.top_left_y:self.bottom_right_y, 
            self.top_left_x:self.bottom_right_x] = self.football_img_resized

        self.redball = self.background_img[self.top_left_y:self.bottom_right_y, 
                                self.top_left_x:self.bottom_right_x]

        #### Define another target coordinates to place another football

        self.top_left_x2 = self.target_x2
        self.top_left_y2 = self.target_y2
        self.bottom_right_x2 = self.target_x2 + self.football_width
        self.bottom_right_y2 = self.target_y2 + self.football_height

        self.target_region2 = self.background_img[self.top_left_y2:self.bottom_right_y2, 
                                        self.top_left_x2:self.bottom_right_x2]
        self.target_region2_height, self.target_region2_width, _ = self.target_region2.shape
        print('target_region2.shape: ', self.target_region2.shape)
        print('target_region2_height: ', self.target_region2_height)
        print('target_region2_width: ', self.target_region2_width)
        self.redball_resized2 = cv2.resize(self.redball, 
            (self.target_region2_width, self.target_region2_height))
        self.background_img[self.top_left_y2:self.bottom_right_y2, 
            self.top_left_x2:self.bottom_right_x2] = self.redball_resized2

        cv2.imshow('Result', self.background_img)

target_x = 700
target_y = 570
placing_image = 'blueball.PNG'
on_which_placed = 'stadium3.jpg'

target_x2 = 100
target_y2 = 570
# Crate object
obj = Calculate(target_x, target_y, placing_image, 
                 on_which_placed, target_x2, target_y2)
# Function call
obj.put_image_on_bgimage()

cv2.waitKey(0)
cv2.destroyAllWindows()