import cv2 as cv
import numpy as np

def mark_image(img, top_left, bottom_right):
	cv.rectangle(img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
	# debug(img)
	cv.imwrite('assets/images/result.jpg', img)

def is_template_found(value):
	threshold = 0.5
	if value >= threshold:
		print('Found template')
		return True
	else:
		print('Template not found')
		return False

def debug(result):
	cv.imshow('Result', result)
	cv.waitKey()

root_img = cv.imread('assets/images/easy.jpg', cv.IMREAD_UNCHANGED)
template_img = cv.imread('assets/images/object_01.png', cv.IMREAD_UNCHANGED)
# template_img = cv.imread('assets/images/needle_huge.png', cv.IMREAD_UNCHANGED)

heigh_root, width_root = root_img.shape[:2]
print(f'heigh_root {heigh_root} width_root {width_root}')

heigh_template, width_template = template_img.shape[:2]
print(f'heigh_template {heigh_template} width_template {width_template}')

# template_img_resized = cv.resize(template_img, (width_root, heigh_root))
# result = cv.matchTemplate(root_img, template_img_resized, cv.TM_CCOEFF_NORMED)
result = cv.matchTemplate(root_img, template_img, cv.TM_CCOEFF_NORMED)
print(result)

min_val, max_value, min_loc, max_loc = cv.minMaxLoc(result)
print(f'min_val {min_val} max_value {max_value}')
print(f'min_loc {min_loc} max_loc {max_loc}')

if is_template_found(max_value):
	mark_image(root_img, max_loc, (max_loc[0] + width_template, max_loc[1] + heigh_template))