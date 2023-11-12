import cv2

def put_image_on_bgimage(target_x, target_y, placing_image, on_which_placed, 
                         target_x2, target_y2):
    football_img = cv2.imread(placing_image)

    football_height, football_width, _ = football_img.shape
    print('football_img.shape: ', football_img.shape)
    print('football_height: ', football_height)
    print('football_width: ', football_width)

    background_img = cv2.imread(on_which_placed)

    target_x = target_x
    target_y = target_y

    top_left_x = target_x
    top_left_y = target_y
    bottom_right_x = target_x + football_width
    bottom_right_y = target_y + football_height

    target_region = background_img[top_left_y:bottom_right_y, 
                                   top_left_x:bottom_right_x]
    target_region_height, target_region_width, _ = target_region.shape
    print('target_region.shape: ', target_region.shape)
    print('target_region_height: ', target_region_height)
    print('target_region_width: ', target_region_width)
    football_img_resized = cv2.resize(football_img, (target_region_width, 
                                        target_region_height))

    background_img[top_left_y:bottom_right_y, 
                   top_left_x:bottom_right_x] = football_img_resized

    target_x2 = target_x2
    target_y2 = target_y2

    top_left_x2 = target_x2
    top_left_y2 = target_y2
    bottom_right_x2 = target_x2 + football_width
    bottom_right_y2 = target_y2 + football_height

    target_region2 = background_img[top_left_y2:bottom_right_y2, 
                                    top_left_x2:bottom_right_x2]
    target_region2_height, target_region2_width, _ = target_region2.shape
    print('target_region2.shape: ', target_region2.shape)
    print('target_region2_height: ', target_region2_height)
    print('target_region2_width: ', target_region2_width)
    football_img_resized2 = cv2.resize(football_img, 
                        (target_region2_width, target_region2_height))
    background_img[top_left_y2:bottom_right_y2, 
                   top_left_x2:bottom_right_x2] = football_img_resized2

    cv2.imshow('Result', background_img)

target_x = 700
target_y = 370
placing_image = 'Redball.PNG'
on_which_placed = 'stadium4.jpeg'

target_x2 = 100
target_y2 = 370
# Function call
put_image_on_bgimage(target_x, target_y, placing_image, 
                     on_which_placed, target_x2, target_y2)

cv2.waitKey(0)
cv2.destroyAllWindows()