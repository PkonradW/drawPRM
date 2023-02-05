import sys
from PIL import Image, ImageDraw
import os
import random
import collections


# constants for graph and image construction
def imagethings():
    x_size = 500
    y_size = 500
    filename = "img01.png"
    # create new image
    image = Image.new(mode="RGB", size=(200, 70), color="red")
    # save the file
    image.save(filename)
    # open the file
    os.system(filename)
    filename = "hopper.jpg"
    with Image.open(filename) as im:
        draw = ImageDraw.Draw(im)
        draw.line((0, 0) + im.size, fill=128)
        draw.line((0, im.size[1], im.size[0], 0), fill=128)

        # write to stdout
        im.save(filename)
        os.system(filename)
