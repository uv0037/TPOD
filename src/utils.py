import math

class Color:
    def __init__(self):
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.GREY = '\033[90m'
        self.RESET = '\033[0m'
        self.ORANGE = '\033[33m'
        self.PURPLE = '\033[35m'



def draw_circle(radius):
    offset = "  " * (radius + 1)

    for y in range(-radius, radius + 1):
        print(offset, end='')
        for x in range(-radius, radius + 1):
            distance = math.sqrt(x ** 2 + y ** 2)
            if radius - 0.5 <= distance <= radius + 0.5:
                print('\033[96m●\033[0m', end='  ')  
            elif radius - 1.5 <= distance <= radius + 1.5:
                print('\033[93m*\033[0m', end='  ') 
            else:
                print('  ', end=' ')  # Empty space for outside the circle
        print()




