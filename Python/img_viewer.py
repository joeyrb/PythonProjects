#!/usr/bin/python
from os import listdir
from PIL import Image as PImage
from PIL import _imaging

def loadImgs(path):
	# Return list of images
	imgList = listdir(path)
	loadedImgs = []
	for img in imgList:
		img = PImage.open(path + img)
		loadedImgs.append(img.draft("RGB" ,(300,300)))

	return loadedImgs

def main():
	# path = "/media/joey/USB\ DISK/Default\ Files/"
	path = "2/"

	imgs = loadImgs(path)

	for img in imgs:
		img.show()


if __name__ == '__main__':
	main()