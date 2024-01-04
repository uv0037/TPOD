import math

def draw_circle(radius):
    # Calculate the offset for centering the circle
    offset = "  " * (radius + 1)

    for y in range(-radius, radius + 1):
        print(offset, end='')
        for x in range(-radius, radius + 1):
            distance = math.sqrt(x ** 2 + y ** 2)
            if radius - 0.5 <= distance <= radius + 0.5:
                print('\033[96m●\033[0m', end='  ')  # Cyan color circle using '●' character
            elif radius - 1.5 <= distance <= radius + 1.5:
                print('\033[93m•\033[0m', end='  ')  # Yellow color circle using '•' character
            else:
                print('  ', end=' ')  # Empty space for outside the circle
        print()


