#!/bin/python3.5
"""
A simple desktop wallpaper generator written by Addison Schuhardt.
https://schuhardt.net
Contact: a@schuhardt.net

This script is designed to generate color gradient-pattern desktop wallpaper images.
Information regarding and changes to this script can be found here: https://github.com/aschuhardt/py_wallpaper
"""

import sys
import numpy as np
import argparse
from PIL import Image, ImageFilter

def main():
    #get values parsed from command-line arguments
    args = getArgs()
    filename = args.filename
    width = args.width
    height = args.height
    radius = args.radius
    offsetVar = args.offset

    #calculate x/y modulo values (k where n % k > 2)
    xMod = getMod(width)
    yMod = getMod(height)

    #fill array [w,h,3] with random values between 0 and 255
    baseWidth = width % xMod
    baseHeight = height % yMod

    #choose a random base color
    baseColor = []
    try:
        baseColor = hex_to_rgb(args.basecolor)
    except:
        baseColor = getRandColor()

    #fill a w*h*3 array with the base color
    arr = np.full((baseWidth, baseHeight, 3), baseColor, dtype=int)

    #populate arrays of length w*h with random integer values
    #   between -variation and +variation
    #these are used to store R/G/B offset values which will be applied to each
    #   channel of each pixel in the base image later.
    offsetAmtsR = np.random.randint(-offsetVar, offsetVar, baseWidth * baseHeight, dtype=int)
    offsetAmtsG = np.random.randint(-offsetVar, offsetVar, baseWidth * baseHeight, dtype=int)
    offsetAmtsB = np.random.randint(-offsetVar, offsetVar, baseWidth * baseHeight, dtype=int)

    #initialize an index to keep track of where in the offset arrays we are at
    offsetIx = 0

    #iterate through each "pixel" in the picture
    #Note: I'm not worried about taking a performance hit here since the
    #   dimensions of the base image are typically in the single-digits.
    #   Therefore, any expected performance loss here is negligable.
    for x in range(baseWidth):
        for y in range(baseHeight):
            #alias the values of the element we're currently looking at
            r = arr[x, y, 0]
            g = arr[x, y, 1]
            b = arr[x, y, 2]

            #offset them by the amount gathered from each channel's
            #   respective offset array at position "offsetIx"
            arr[x, y, 0] = offsetColor(r, offsetAmtsR[offsetIx])
            arr[x, y, 1] = offsetColor(g, offsetAmtsG[offsetIx])
            arr[x, y, 2] = offsetColor(b, offsetAmtsB[offsetIx])

            #increment the offset index
            offsetIx += 1

    #create an image from those array values
    img = Image.fromarray(arr.astype('uint8')).convert('RGBA')

    #resize the low-res image to the desired dimensions
    #Note: this results in a "tiled" looking image, consisting of a bunch
    #   of colored squares aligned in a grid.
    img = img.resize((width, height))

    #apply blur
    img = img.filter(ImageFilter.GaussianBlur(radius))

    #save image
    img.save(filename)

    #print debug info
    msg =  "Created new wallpaper image"
    msg += " at " + filename
    msg += " with parmeters:"
    msg += " width=" + str(width)
    msg += " height=" + str(height)
    msg += " blur-radius=" + str(radius)
    msg += " xMod=" + str(xMod)
    msg += " yMod=" + str(yMod)

    print(msg)

def getMod(n):
    #find the lowest number k that matches the pattern:
    #   n % k > 2
    for k in range(3, n):
        if n % k > 2:
            return k

def hex_to_rgb(value):
    #converts a hexidecimal representation of a color to a 3-tuple
    #   representing its RGB counterpart
    value = value.lstrip('#')
    lv = len(value)
    return np.asarray(tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

def offsetColor(n, offset):
    #offsets the given RGB value (n) by the given amount (offset)
    n += offset
    if n > 255:
        return 255
    elif n < 0:
        return 0
    else:
        return n

def getArgs():
    #set up parser for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", nargs="?", type=str, default="output.png", help="The path+name of the desired output file")
    parser.add_argument("-w", "--width", nargs="?", type=int, default=1366, help="The image width")
    parser.add_argument("-t", "--height", nargs="?", type=int, default=768, help="The image height")
    parser.add_argument("-r", "--radius", nargs="?", type=int, default=128, help="The radius of the Gaussian blur pass")
    parser.add_argument("-o", "--offset", nargs="?", type=int, default=50, help="The max amount each pixel's color channels will be offset")
    parser.add_argument("-c", "--basecolor", nargs="?", type=str, default="", help="A hexidecimal (#FFFFFF) representation of a color to use as the image's base")
    return parser.parse_args()

def getRandColor():
    #returns a random value between 0 and 255
    arr = np.random.rand(3) * 255
    return arr.astype(dtype=int)

if __name__ == "__main__":
    main()
