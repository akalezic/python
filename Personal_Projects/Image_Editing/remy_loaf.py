"""
File: remy_loaf.py
------------------
This program takes a photo of my cousins' corgi Remy and resizes and
pastes an image of a loaf of bread over his body, as I often jokingly
call him a loaf of bread.
"""
from simpleimage import SimpleImage
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter

INTENSITY_THRESHOLD = 1.6

def main():
    # opens the background image
    back = Image.open('images/remy.jpg')
    # opens the foreground image
    image = Image.open('images/bread.png')
    # this is just to see how much the image needs to be adjusted to fit remy
    print(image.width)
    print(image.height)
    # adjusts image to fit remy's body better
    image_resize = image.resize((440,370))
    # rotates resized image slightly clockwise so it lines up with remy's body better
    rotated = image_resize.rotate(-7)
    # creates copy of the background image
    back_im = back.copy()
    # pastes the rotated and resized image onto the image at pixel location 265 x 110
    back_im.paste(rotated, (265,110), rotated)
    # saves the image to the images folder as a jpg of quality 95
    back_im.save('images/remyloaf.jpg',quality = 95)
    # shows the final pasted image in python
    back_im.show()

if __name__ == '__main__':
    main()