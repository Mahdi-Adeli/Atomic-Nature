from picture import Picture
from color import Color

def check_luminance(c):
  red = c.getRed()
  green = c.getGreen()
  blue = c.getBlue()

  return (.114 * blue) + (.299 * red) + (.587 * green) 

# we use this 3 function when we are changing the picture color.

def change_to_black(c):
  return Color( 0 , 0 , 0)

def change_to_white(c):
  return Color( 255 , 255 , 255)

def change_to_red(c):
  return Color(255 ,0 ,0)


      


