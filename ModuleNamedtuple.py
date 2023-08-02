from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(red=55, green=155, blue=255)

print(color.red)
