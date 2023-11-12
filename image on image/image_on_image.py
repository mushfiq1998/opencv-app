'''calculate coordinate on image and place an image on a background image,
then place that image on the another region of background image. '''

import cv2

# Load the football image
#football_img = cv2.imread('Redball.PNG')
football_img = cv2.imread('blueball.PNG')

# Get the dimensions of the football image
football_height, football_width, _ = football_img.shape
print('football_img.shape: ', football_img.shape)
print('football_height: ', football_height)
print('football_width: ', football_width)

# Load the background image where you want to place the football
background_img = cv2.imread('stadium3.jpg')

# Define the target coordinates where you want to place the football
target_x = 700
target_y = 570

# Calculate the coordinates for the football's new position
top_left_x = target_x
top_left_y = target_y
bottom_right_x = target_x + football_width
bottom_right_y = target_y + football_height

# Adjust the dimensions of the target region to match the football image
target_region = background_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
target_region_height, target_region_width, _ = target_region.shape
print('target_region.shape: ', target_region.shape)
print('target_region_height: ', target_region_height)
print('target_region_width: ', target_region_width)
football_img_resized = cv2.resize(football_img, (target_region_width, target_region_height))

# Place the resized football image onto the background image
background_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = football_img_resized

# Copy the coordinate (wherein the previous ball is placed) to redball
redball = background_img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

#### Define another target coordinates to place another football
target_x2 = 100
target_y2 = 570

# Calculate the coordinates for the football's new position
top_left_x2 = target_x2
top_left_y2 = target_y2
bottom_right_x2 = target_x2 + football_width
bottom_right_y2 = target_y2 + football_height

# Adjust the dimensions of the target region to match the football image
target_region2 = background_img[top_left_y2:bottom_right_y2, top_left_x2:bottom_right_x2]
target_region2_height, target_region2_width, _ = target_region2.shape
print('target_region2.shape: ', target_region2.shape)
print('target_region2_height: ', target_region2_height)
print('target_region2_width: ', target_region2_width)
redball_resized2 = cv2.resize(redball, (target_region2_width, target_region2_height))
background_img[top_left_y2:bottom_right_y2, top_left_x2:bottom_right_x2] = redball_resized2

# Display the resulting image
cv2.imshow('Result', background_img)
cv2.waitKey(0)
cv2.destroyAllWindows()