import sys
import random
import logging
import logger
from exception import CustomException
from src.components.register import Profile
from src.utils import Color
import time




color = Color()
profile = Profile()

class PortalA:
    def __init__(self):
        self.levels = {
            1: ["I stand tall and proud, yet my roots are hidden below. Birds rest on my branches, and my leaves sway in the breeze. What am I?", "I'm a flowing ribbon, winding through valleys and plains. People build bridges over me, and fish call me home. What am I?", "I'm silent in the night, a celestial display. Countless twinkling lights, far, far away. What am I?"],
            2: ["I'm covered in white, sparkling and cold. I transform landscapes and bring joy to the young and old. What am I?", "I'm a fortress of rock, standing tall and grand. Climbers challenge me, and eagles understand. What am I?", "I'm a buzzing melody, sipping nectar with grace. Wings painted in hues, a delicate embrace. What am I?"],
            3: ["I'm a golden globe in the sky, warming the earth below. Sunflowers turn to face me, and shadows gently grow. What am I?", "I'm a silent hunter, prowling in the night. Sharp eyes and stealthy moves, always out of sight. What am I?", "I'm a dance of colors, painted in the sky. Rain brings me to life, as I arch and amplify. What am I?"],
            4: ["I'm a carpet of green, soft underfoot. Picnics are enjoyed on me, and I provide shade for a respite. What am I?", "I'm a silver crescent, pulling the tide. Waves dance to my rhythm, a celestial guide. What am I?", "I'm a tiny architect, spinning threads with skill. My intricate webs decorate corners, waiting patiently and still. What am I?"],
            5: ["I'm a gentle breeze, carrying scents of bloom. Petals fall in my embrace, and I bring spring's perfume. What am I?", "I'm a crown of petals, a symbol of love. Red is my signature, sent from above. What am I?"],
        }
        self.answers = [
                    ["tree", "River", "stars"],
                    ["Snow", "Mountain", "Butterfly"],
                    ["Sun", "Owl", "Rainbow"],
                    ["Grass", "Moon", "Spider"],
                    ["Wind", "Rose"],
                ]
        self.hints = [
            ["I provide shade on a sunny day.", "Follow my current to find the answer.", "Make a wish upon me."],
            ["Winter's blanket on the ground.", "Look up to find my peaks.", "My life begins as a caterpillar."],
            ["Daylight is my time to shine.", "I'm known for my wisdom.", "Find me after the storm."],
            ["Lawns are made of me.", "I control the ocean's flow.", "I catch my prey in a silky trap."],
            ["I rustle leaves in the trees.", "I'm often given on special occasions."]

        ]
portal = PortalA()

class Monster:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
    
def solve_riddle(level, riddle, answer):
    try:
        print(color.PURPLE+f"\nRiddle for Level {level}:"+color.RESET+color.YELLOW+f" {riddle}"+color.RESET)
        player_answer = input(color.BLUE+"Your answer: "+color.RESET).strip().lower()  

        if player_answer == answer.lower(): 
            print(color.GREEN+"\nCORRECT ANSWER"+color.RESET)
            print(color.GREEN+"Proceeding to the next riddle."+color.RESET)  
            return True
        else:
            print(color.RED+"\nIncorrect answer!"+color.RESET)
            return False
    except Exception as e:
        raise CustomException(e, sys)

def create_monster():
    return Monster("SHADOWFANG", health=120, attack_power=15)
        


        

def fight(player_name, player_hints, player_level, player_health, monster):
    try:
        #print(color.BLUE+"\nA wild"+color.RED+f" {(monster.name).upper()} "+color.BLUE+"appears!"+color.RESET)
        sentence = f"\nA wild {(monster.name).upper()} appears!"
        words = sentence.split()  
        for word in words:
            print(color.BLUE+word+color.RESET, end=' ', flush=True)
            time.sleep(0.5)
        while player_health > 0 and monster.is_alive():
            try:
                print(color.YELLOW + f"\n\n1. Attack monster {monster.name}" + color.RESET)
                print(color.YELLOW + "2. Surrender" + color.RESET)
                print(color.YELLOW + "3. Save and Quit" + color.RESET)
                choice = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))

                if choice == 1:
                    player_attack = random.randint(20, 30)  
                    monster.take_damage(player_attack)
                    print(color.GREEN+ f"You attack the {monster.name} with power {player_attack}. Its health is now {monster.health}" + color.RESET)

                    if not monster.is_alive():
                            break  

                    monster_attack = random.randint(15, 30)
                    player_health -= monster_attack
                    print(color.RED+ f"The {monster.name} attacks you with power {monster_attack}. Your health level is now {player_health}" + color.RESET)
                elif choice == 2:
                    player_health = 0
            
                elif choice == 3:
                    profile.save_player_data(player_name, player_hints, player_level, player_health)
                    exit()
            except ValueError:
                            print(color.RED+"\nPlease enter a valid number for the choice.")
                            print(color.BLUE+"Redirecting you to main menu"+color.RESET)
                            print(color.GREY+"**"*20+"\n"+color.RESET)

        if player_health <= 0:
            print(color.RED+"You've been defeated. Game Over!"+color.RESET)
            exit()
        elif not monster.is_alive():
            print(color.GREEN+f"You defeated the {monster.name}!"+color.RESET)
            


    except Exception as e:
        raise CustomException(e, sys)



def play_level(player_name, player_hints, player_level, player_health, b):
    try:
        name = player_name
        current_hints = player_hints
        current_level = player_level
        current_health = player_health
        portal_b_stump = b
        while current_level <= 6:   

            ans = portal.answers

            for level in range(current_level, len(portal.levels) + 1):
                print(color.ORANGE+f"\nSUB - PORTAL LEVEL : {level} "+color.RESET)
                riddles = portal.levels[level]
                for idx, riddle in enumerate(riddles):    
                    while not solve_riddle(level, riddle, ans[level - 1][idx]):
                        try:
                            print(color.YELLOW + "\n1. Try again or go back." + color.RESET)
                            print(color.YELLOW + "2. Help with hint" + color.RESET)
                            print(color.YELLOW + "3. Save and Quit\n" + color.RESET)
                            choice = int(input(color.BLUE+"Enter your choice: "+color.RESET))

                            if choice == 1:
                                solve_riddle(level, riddle, ans[level - 1][idx])
                            elif choice == 2:
                                if current_hints > 0:
                                    print(color.GREEN + f"\nProfile choosen name: {name}" + color.RESET)
                                    print(color.GREEN + f"{name}'s Hints left: {current_hints}" + color.RESET)
                                    print(color.GREEN +f"\nI hope this hint might help:- {portal.hints[level - 1][idx]}\n" + color.RESET)
                                    current_hints -= 1
                                    solve_riddle(level, riddle, ans[level - 1][idx])
                                else:
                                    print(color.RED+"\nNo hints left"+color.RESET)
                                    solve_riddle(level, riddle, ans[level - 1][idx])
                            elif choice == 3:
                                profile.save_player_data(name, current_hints, level, current_health, portal_b_stump)
                                exit()
                        except ValueError:
                            print(color.RED+"\nPlease enter a valid number for the choice.")
                            print(color.BLUE+"Redirecting you to main menu"+color.RESET)
                            print(color.GREY+"**"*20+"\n"+color.RESET)
                current_level += 1
            print(color.GREEN+"\nProceeding to the next SUB-PORTAL.\n"+color.RESET)
            if current_level == 6:  
                print(color.PURPLE+f"Monster level {current_level}. Prepare for a fight!"+color.RESET)
                monster = create_monster()
                fight(name, current_hints, current_level, current_health, monster)
                current_level += 1
                break    
            logging.info(f"Player {player_name} proceeding to level ")  
   
    except Exception as e:
        raise CustomException(e, sys)

