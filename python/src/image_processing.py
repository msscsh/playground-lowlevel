import os
import cv2 as cv
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def draw_all_locations(root_img, template_img):
	result = cv.matchTemplate(root_img, template_img, cv.TM_CCOEFF_NORMED)
	debug(result)

	threshold = 0.8
	locations = np.where(result >= threshold)
	locations = list(zip(*locations[::-1]))

	if locations:
		needle_w = template_img.shape[1]
		needle_h = template_img.shape[0]
		line_color = (0, 255, 0)
		line_type = cv.LINE_4

		for loc in locations:
			top_left = loc
			bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
			cv.rectangle(root_img, top_left, bottom_right, line_color, line_type)

def draw_location(root_img, template_img):
	result = cv.matchTemplate(root_img, template_img, cv.TM_CCOEFF_NORMED)
	debug(result)
	min_val, max_value, min_loc, max_loc = cv.minMaxLoc(result)
	top_left = max_loc
	bottom_right = (max_loc[0] + image_sizes(template_img)[1], max_loc[1] + image_sizes(template_img)[0])
	cv.rectangle(root_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

def image_sizes(img):
	heigh_root, width_root = img.shape[:2]
	print(f'heigh_root {heigh_root} width_root {width_root}')
	return heigh_root, width_root

def image_resize(img, width, heigh):
	img_resized = cv.resize(img, (width, heigh))
	return img_resized

def debug(result):
	print(result)
	cv.imshow('Result', result)
	cv.waitKey()

root_img = cv.imread('../assets/images/hard.jpg', cv.IMREAD_UNCHANGED)
template_img = cv.imread('../assets/images/object_01.png', cv.IMREAD_UNCHANGED)

draw_all_locations(root_img, template_img)
# draw_location(root_img, template_img)

cv.imshow('Matches', root_img)
cv.waitKey()