import sys
import numpy as np
import argparse
from PIL import Image, ImageFilter
 
def main():
    #get values parsed from command-line arguments
    args = getArgs()
    filename = args.filename
    width = int(args.width)
    height = int(args.height)
    radius = int(args.radius)
    xMod = int(args.xmod)
    yMod = int(args.ymod)

    #fill array [w,h,3] with random values between 0 and 255
    arr = np.random.rand(width % 7, height % 7, 3) * 255

    #create an image from those values
    img = Image.fromarray(arr.astype('uint8')).convert('RGBA')
    
    #resize the low-res image to the desired dimensions
    img = img.resize((width, height))

    #apply blur
    img = img.filter(ImageFilter.GaussianBlur(radius)) 

    #save image
    img.save(filename)

def printUsage():
    #prints usage information
    s = "Usage: \"python makewalpaper.py filename width height [radius [modX [modY]]]\""
    print(s)

def getArgs():
    #set up parser for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("width")
    parser.add_argument("height")
    parser.add_argument("radius", default=64, nargs="?")
    parser.add_argument("xmod", default=7, nargs="?")
    parser.add_argument("ymod", default=7, nargs="?")
    return parser.parse_args()


if __name__ == "__main__":
    main()
