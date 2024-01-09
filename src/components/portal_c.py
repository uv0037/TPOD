
import time
from src.utils import Color

class PortalC:
    def __init__(self):
        pass

    def desc(self):
        color = Color()
        print("  " * 22, end=' ')
        sentence = "**********  WELCOME TO PORTAL C  **********"
        words = sentence.split()
        for word in words:
            print(color.RED + word + color.RESET, end=' ', flush=True)
            time.sleep(0.5)

        print("\n") 

        sentence_b = "Portal C, the gateway back to reality, yet guarded by the final challenge. Solve the puzzle of Missionaries and Cannibals to bridge the gap between the realms and emerge victorious."
        words = sentence_b.split()
        for word in words:
            print(color.GREEN + word + color.RESET, end=' ', flush=True)
            time.sleep(0.2)




    def last_portal(self):
        boat_side = 'Right'
        missionaries_on_right = 3
        cannibals_on_right = 3
        missionaries_on_left = 0
        cannibals_on_left = 0
        b = 0
        run = True

        while run:
            missionaries = int(input("M: "))
            cannibals = int(input("C: "))
            print(f'M = {missionaries_on_left} C = {cannibals_on_left} |-----B| M = {missionaries_on_right} C = {cannibals_on_right}')
            b = missionaries + cannibals

            if 1 <= b <= 2:
                print("Valid move")
            else:
                print('Invalid move')
                continue

            if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
                print('Invalid move')
                continue

            if boat_side == 'Right':
                missionaries_on_right -= missionaries
                cannibals_on_right -= cannibals
                missionaries_on_left += missionaries
                cannibals_on_left += cannibals
                boat_side = 'Left'
                print(f'M = {missionaries_on_left} C = {cannibals_on_left} |B------| M = {missionaries_on_right} C = {cannibals_on_right}')
            else:
                missionaries_on_left -= missionaries
                cannibals_on_left -= cannibals
                missionaries_on_right += missionaries
                cannibals_on_right += cannibals
                boat_side = 'Right'
                print(f'M = {missionaries_on_left} C = {cannibals_on_left} |------B| M = {missionaries_on_right} C = {cannibals_on_right}')

            if 0 < missionaries_on_right < cannibals_on_right or 0 < missionaries_on_left < cannibals_on_left:
                print("You Lose")
                print("Game over")
                run = False
            elif missionaries_on_left == 3 and cannibals_on_left == 3:
                print('You win')
                print("Game over")
                run = False



