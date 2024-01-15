
import time
from src.utils import *
from logger import *
from exception import *

color = Color()
class PortalC:
    def __init__(self):
        pass

    def desc(self, player_name, player_hints, player_level, player_health, player_armour):
        draw_circle(10)
        print("  " * 15, end=' ')
        sentence = "**********  WELCOME TO PORTAL C  **********"
        words = sentence.split()
        for word in words:
            print(color.RED + word + color.RESET, end=' ', flush=True)
            time.sleep(0.5)

        print("\n") 
        #print("  " *2, end=' ')
        sentence_b = "Portal C, the gateway back to reality, yet guarded by the final challenge. Solve the puzzle of Missionaries and Cannibals to bridge the gap between the realms and emerge victorious."
        words = sentence_b.split()
        for word in words:
            print(color.GREEN + word + color.RESET, end=' ', flush=True)
            time.sleep(0.2)
        print("\n")

        print(color.GREEN + f"\nProfile chosen name: {player_name}" + color.RESET)
        print(color.GREEN + f"{player_name}'s Hints left: {player_hints}" + color.RESET)
        print(color.GREEN + f"{player_name}'s health: {player_health}" + color.RESET)
        print(color.GREEN + f"{player_name}'s Armour: {player_armour}" + color.RESET) 


    def last_portal(self, player_name):
        boat_side = 'Right'
        missionaries_on_right = 3
        cannibals_on_right = 3
        missionaries_on_left = 0
        cannibals_on_left = 0
        b = 0
        run = True
        print("  " * 10, end=' ')
        sentence_mc = "**********  MISSIONARIES AND CANNIBALS  **********"
        words = sentence_mc.split()
        for word in words:
            print(color.RED + word + color.RESET, end=' ', flush=True)
            time.sleep(0.5)
        print("\n")
        print(color.RED+"  " * 22+"RULES"+color.RESET)
        sentence_r1 = "1. Number of missionaries on either side should never be less than number of cannibals"
        words = sentence_r1.split()
        for word in words:
            print(color.GREEN + word + color.RESET, end=' ', flush=True)
            time.sleep(0.2)
        print("\n")
        sentence_r2 = "2. Only one or 2 people can travel through boat at a time and always need one to travel from either side."
        words = sentence_r2.split()
        for word in words:
            print(color.GREEN + word + color.RESET, end=' ', flush=True)
            time.sleep(0.2)
        print("\n")
        sentence_r3 = "3. You win the game when all missionaries and cannibals on the right go to the left side"
        words = sentence_r3.split()
        for word in words:
            print(color.GREEN + word + color.RESET, end=' ', flush=True)
            time.sleep(0.2)
        print("\n")
        
        
        print(color.YELLOW+f'Missionaries = {missionaries_on_left}'+color.RED+F' Cannibals = {cannibals_on_left} '+color.BLUE+ ' |-----B| ' + color.YELLOW + f' Missionaries = {missionaries_on_right}'+color.RED+f' Cannibals = {cannibals_on_right}'+color.RESET)

        while run:
            try:
                missionaries = int(input(color.YELLOW+"\nMissionaries: "))
                cannibals = int(input(color.RED+"Cannibals: "+color.RESET))
                b = missionaries + cannibals

                if 1 <= b <= 2:
                    print(color.GREEN+"\nVALID MOVE\n"+color.RESET)
                else:
                    print(color.RED+"\nPLEASE ENTER A NUMBER BETWEEN 0 to 3\n"+color.RESET)
                    continue

                if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
                    print(color.RED+"\nPLEASE ENTER A NUMBER BETWEEN 0 to 3\n"+color.RESET)
                

                if boat_side == 'Right':
                    missionaries_on_right -= missionaries
                    cannibals_on_right -= cannibals
                    missionaries_on_left += missionaries
                    cannibals_on_left += cannibals
                    boat_side = 'Left'
                    print(color.YELLOW+f'Missionaries = {missionaries_on_left}'+color.RED+F' Cannibals = {cannibals_on_left} '+color.BLUE+ ' |B-----| ' + color.YELLOW + f' Missionaries = {missionaries_on_right}'+color.RED+f' Cannibals = {cannibals_on_right}'+color.RESET)
                else:
                    missionaries_on_left -= missionaries
                    cannibals_on_left -= cannibals
                    missionaries_on_right += missionaries
                    cannibals_on_right += cannibals
                    boat_side = 'Right'
                    print(color.YELLOW+f'Missionaries = {missionaries_on_left}'+color.RED+F' Cannibals = {cannibals_on_left} '+color.BLUE+ ' |-----B| ' + color.YELLOW + f' Missionaries = {missionaries_on_right}'+color.RED+f' Cannibals = {cannibals_on_right}'+color.RESET) 

                if 0 < missionaries_on_right < cannibals_on_right or 0 < missionaries_on_left < cannibals_on_left:
                    print(color.RED+"\nYou Lose, GAME OVER"+color.RESET)
                    run = False
                elif missionaries_on_left == 3 and cannibals_on_left == 3:
                    logging.info(f"Player {player_name} won the game ")
                    print(color.GREEN+'\nYou win\n')
                    sentence = "**********  After traversing the intricate dimensions, unlocking the mysteries of the enigmatic portals, and mastering the arcane challenges, the lost souls finally reunite with their mortal vessel, awakening to a new beginning in the realm of the living.  **********"
                    words = sentence.split()
                    for word in words:
                        print(word + color.RESET, end=' ', flush=True)
                        time.sleep(0.2)
                    run = False
                    exit()
            except ValueError:
                print(color.RED + "\nPlease enter a valid number.")
                print(color.GREY + "**" * 20 + "\n" + color.RESET)



