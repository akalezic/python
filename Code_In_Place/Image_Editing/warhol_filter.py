"""
File: warhol_filter.py
----------------------
This program generates the Warhol effect based on the original image, in which a collage of
the same image is generated and each image has a filter of a different color over it.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 5
N_COLS = 5
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # creates nested for loop for the number of rows between 0 and the height with increments of patch size
    # and the number of columns between 0 and width with increments of patch size
    for i in range(0, HEIGHT, PATCH_SIZE):
        for w in range(0, WIDTH, PATCH_SIZE):
            # randomizes the patch color scale with a number between 0 and 1.75
            patch = make_recolored_patch(random.uniform(0,1.75), random.uniform(0,1.75), random.uniform(0,1.75))
            # nested for loop that goes over each pixel in the patch
            for x in range(PATCH_SIZE):
                for y in range(PATCH_SIZE):
                    # gets the pixel for each pixel in the image
                    pixel = patch.get_pixel(x, y)
                    # takes that pixel for the final image and assigns it to the appropriate placement in the new column
                    final_image.set_pixel(x + w, y + i, pixel)
    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

if __name__ == '__main__':
    main()