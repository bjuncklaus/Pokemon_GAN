from PIL import Image
from resizeimage import resizeimage
import os

dir = './data/'
dir_output = './resizedData/'

files = [f for f in os.listdir(dir)] # check extension if necessary

if not (os.path.exists(dir_output)):
	os.mkdir(dir_output)

for f in files:
	print(f)
	fd_img = open(dir + f, 'r+b')
	img = Image.open(fd_img)
	img = resizeimage.resize_thumbnail(img, [128, 128]) # this keeps the ratio
	# img = resizeimage.resize_crop(img, [32, 32]) # this crops the image creating a box with the given dimensions
	# img = resizeimage.resize_contain(img, [32, 32]) # resize the image so that it can fit in the specified area, keeping the ratio and without crop
	img.save(dir_output + f, img.format)
	fd_img.close()
