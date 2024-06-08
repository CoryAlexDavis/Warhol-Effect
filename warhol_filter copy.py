"""
file: warhol_filter.py
This program generates the Warhol effect based on the original image.
"""
#andy_warhol effect that has patches that recolor randomly after each creation

from simpleimage import SimpleImage

from PIL import Image

import random

DEFAULT_IMAGE = 'images/simba-sq.jpg'

NUM_SIDES = random.randint(0, 2)

#define main function
def main():
    # create user input
    user_choice = user_input()
    #create 5 filters that generates a random combinations of red, green, and blue
    new_pics = from_list(user_choice)



    #b = random_filter(user_choice)
    #c = random_filter(user_choice)
    #d = random_filter(user_choice)
    #e = random_filter(user_choice)
    #f = random_filter(user_choice)
    finished_image = canvas(new_pics)
    finished_image.show()


def user_input():
    selection = input('Enter a file name (or press return for default): ')
    if selection == '':
        selection = DEFAULT_IMAGE
    else:
        selection = str("images/" + selection)
    return selection

def random_filter(filename):
    image = SimpleImage(filename)
    num = roll_dice()
    for pixel in image:
        if 2 <= num <= 5:
            pixel.red *= float(NUM_SIDES / roll_dice())
            pixel.green *= 0.7
            pixel.blue *= 0.7
        elif 6 <= num <= 9:
            pixel.green *= float(NUM_SIDES / roll_dice())
            pixel.red *= 0.7
            pixel.blue *= .07
        elif 10 <= num <= 13:
            pixel.blue *= float(NUM_SIDES / roll_dice())
            pixel.green *= 0.7
            pixel.red *= 0.7
        elif 14 <= num <= 18:
            average = (pixel.red + pixel.blue + pixel.green) // 3
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image

def roll_dice():
    die1 = random.randint(1, 11)
    die2 = random.randint(1, 11)
    total = die1 + die2
    value = total
    return value

def from_list(choice):
    list_of_images = []
    for i in range(6):
        picture = random_filter(choice)
        list_of_images.append(picture)
    return list_of_images

def canvas(list_of_images):
    for image in range(len(list_of_images)):
        #image = list_of_images[(len(list_of_images) - 1)]
        height = image.height
        width = image.width
        canvas = SimpleImage.blank((width * 3), (height * 2))
        form_image(height, width, image, list_of_images, canvas)
        #for y in range(height):
            #for x in range(width):
                #pixel = image.get_pixel(x, y)
                #canvas.set_pixel(x, y, pixel)
                #copy and set image 1
                #pixel_one = .get_pixel(x, y)
                #canvas.set_pixel(x, y, pixel_one)
                #copy and set image 2
                #pixel_two = b.get_pixel(x, y)
                #canvas.set_pixel((width - 1) + (x + 1), y, pixel_two)
                #copy and set image 3
                #pixel_three = c.get_pixel(x, y)
                #canvas.set_pixel((width * 2 - 1) + (x + 1), y, pixel_three)
                #copy and set image 4
                #pixel_four = d.get_pixel(x, y)
                #canvas.set_pixel(x, (height - 1) + (y + 1), pixel_four)
                #copy and set image 5
                #pixel_five = e.get_pixel(x, y)
               # canvas.set_pixel((width - 1) + (x + 1), (height - 1) + (y + 1), pixel_five)
                #copy and set image 6
                #pixel_six = f.get_pixel(x, y)
                #canvas.set_pixel((width * 2 - 1) + (x + 1), (height - 1) + (y + 1), pixel_six)
        canvas.show()
    return canvas

def form_image(height, width, image, list_of_images, canvas):
    for y in range(height):
        for x in range(width):
            if len(list_of_images) == 5:
                pixel_one = image.get_pixel(x, y)
                canvas.set_pixel(x, y, pixel_one)
            if len(list_of_images) == 4:
                pixel_two = image.get_pixel(x, y)
                canvas.set_pixel((width - 1) + (x + 1), y, pixel_two)
            if len(list_of_images) == 3:
                pixel_three = image.get_pixel(x, y)
                canvas.set_pixel((width * 2 - 1) + (x + 1), y, pixel_three)
            if len(list_of_images) == 2:
                pixel_four = image.get_pixel(x, y)
                canvas.set_pixel(x, (height - 1) + (y + 1), pixel_four)
            if len(list_of_images) == 1:
                pixel_five = image.get_pixel(x, y)
                canvas.set_pixel((width - 1) + (x + 1), (height - 1) + (y + 1), pixel_five)
            if len(list_of_images) == 0:
                pixel_six = image.get_pixel(x, y)
                canvas.set_pixel((width * 2 - 1) + (x + 1), (height - 1) + (y + 1), pixel_six)
    return canvas


if __name__=='__main__':
    main()