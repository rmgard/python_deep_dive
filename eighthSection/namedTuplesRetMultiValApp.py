from random import randint, random
from collections import namedtuple

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

color = random_color()

''' So below we use namedtuple() to create a function that has
    callable local variables. so in pycharm when i call
    color = random_color2()
    color.SOMEVAR
    SOMEVAR will start populating with options such as green, blue, etc.

    '''

Color = namedtuple('Color', 'red green blue alpha')

def random_color2():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

