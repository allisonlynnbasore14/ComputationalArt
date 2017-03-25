""" Make an awesome random computation art piece! """

import random
from PIL import Image
import math


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    # TODO: implement this
    #Here is the plan, take a random number between the min and max depth. this is the number of times the function 
    #for getting a random function is called. A random function from the lis of functions is chosen and put into a list
    #A list is started that will collect each new run to get a new function from the bank

    #I might do something where, everytime a new function is added to the output, it counts +1. and it stops when it reaches the number generated randomlly
    if min_depth == 1:
        b = random.randint(1,2) #picking one of the base functions
        if b == 1:
            return ["y"] 
        if b == 2:
            return ["x"]
    else: 
        a = random.randint(1,6) #picking a random function
        if a == 1:
            return ["prod", build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]
        if a == 2:
            return ["avg", build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]
        if a ==3:
            return ["sin", build_random_function(min_depth - 1, max_depth - 1)]
        if a == 4:
            return ["cos", build_random_function(min_depth - 1, max_depth - 1)]
        if a == 5:
            return  ["half", build_random_function(min_depth - 1, max_depth - 1)]
        if a == 6:
            return ["third", build_random_function(min_depth - 1, max_depth - 1)]
        """
        a = randint
        if a is for prod or val:
            return [someFunc, build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]
        else:
            return [someFunc, build_random_function(min_depth - 1, max_depth - 1)]

        """


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5, 0.5, 0.5))
     #Create some computat
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    # TODO: I bet there is a more concise was to do this with a dictionary
    
    
    if len(f) == 3:
        a = evaluate_random_function(f[1],x,y)
        c = evaluate_random_function(f[2],x,y)
        return evaluate_random_function([str(f[0])],a,c)
    if len(f) == 2:
        b =evaluate_random_function(f[1],x,y)
        return evaluate_random_function([str(f[0])],b,y)
    if len(f) == 1:
        if f == ["prod"]:
            return x*y
        if f == ["avg"]:
            return (x*y)/2
        if f == ["half"]:
            return x*5
        if f == ["third"]:
            return x*3
        if f == ["sin"]:
            return  math.sin(x)
        if f == ["cos"]:
            return math.cos(x)
        if f == ["x"]:
            return x
        if f == ["y"]:
            return y

    


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    #Here is teh equation I calculated for finding the ratio fro transfer. m1 and M1 are the min 
    #and max of input and m2 and M2 are the mini and max of the output
    #val = x*(M1-m1)+m1   then x*(M2-m2)+m2 = output. The x is found int eh first equation and use
    #used in the second
    x = (val-(input_interval_start))/(input_interval_end - input_interval_start)
    output = x*(output_interval_end - output_interval_start) + output_interval_start
    
    return output

    


def color_map(cat):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval( cat, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    #this is going to ask build random for a randomly generated function list that evalute will unpack and impliment
    red_function = build_random_function(7,9)
    #red_function = ["prod",["prod",["half",["half",["third"]]]]]
    green_function = build_random_function(7,9)
    blue_function = build_random_function(7,9)
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


generate_art("myart4.png", 350, 350)

