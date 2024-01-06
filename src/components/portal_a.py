import sys
import random
import logging
import logger
from exception import CustomException
from src.components.register import Profile
from src.utils import Color




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
            #6: ["What has hands but cannot clap?", "What has a head and a tail but no body?", "What is always in front of you but can't be seen?"],
            #7: ["What has keys but can't open locks?", "What gets wetter as it dries?", "What can be cracked, made, told, and played?"]
        }
        self.answers = [
                    ["tree", "River", "Stars"],
                    ["Snow", "Mountain", "Butterfly"],
                    ["Sun", "Owl", "Rainbow"],
                    ["Grass", "Moon", "Spider"],
                    ["Wind", "Rose"],
                    #["a clock", "a coin", "tomorrow"],
                    #["piano", "towel", "a joke"]
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
        print(f"Riddle for Level {level}: {riddle}")
        player_answer = input("Your answer: ").strip().lower()  

        if player_answer == answer.lower(): 
            print(color.GREEN+"CORRECT ANSWER"+color.RESET)
            print(color.GREEN+"Proceeding to the next riddle."+color.RESET)  
            return True
        else:
            print(color.RED+"Incorrect answer!"+color.RESET)
            return False
    except Exception as e:
        raise CustomException(e, sys)

def create_monster(level):
    if level == 6:
        return Monster("Shadowfang", health=120, attack_power=15)
    elif level == 7:
        return Monster("Frostclaw", health=150, attack_power=20)
        


        

def fight(player_health, monster):
    try:
        print(f"A wild {monster.name} appears!")
        while player_health > 0 and monster.is_alive():
            print(color.YELLOW + f"1. Attack monster {monster.name}" + color.RESET)
            print(color.YELLOW + "2. Surrender" + color.RESET)
            print(color.YELLOW + "3. Save and Quit" + color.RESET)
            choice = int(input("Enter your choice: "))

            if choice == 1:
                player_attack = random.randint(20, 30)  
                monster.take_damage(player_attack)
                print(color.GREEN+ f"You attack the {monster.name} with power {player_attack}. Its health is now {monster.health}" + color.RESET)

                if not monster.is_alive():
                    break  

                monster_attack = random.randint(15, 30)
                player_health -= monster_attack
                print(color.RED+ f"The {monster.name} attacks you with power {monster_attack}. Your armour level is now {player_health}" + color.RESET)
            elif choice == 2:
                player_health = 0
            
            elif choice == 3:
                profile.save_player_data(name, current_hints, current_level, current_health)
                exit()

        if player_health <= 0:
            print("You've been defeated. Game Over!")
        elif not monster.is_alive():
            print(f"You defeated the {monster.name}!")


    except Exception as e:
        raise CustomException(e, sys)



def play_level(player_name, player_hints, player_level, player_health):
    try:
        name = player_name
        current_hints = player_hints
        current_level = player_level
        current_health = player_health
        while current_level <= 7:   
            if current_level in [6, 7]:  
                print(f"Monster level {current_level}. Prepare for a fight!")
                monster = create_monster(current_level) 

                fight(current_health, monster) 
                break
            riddles_level = portal.levels.items()
            ans = portal.answers
            for level, riddles in riddles_level:
                print(f"Level : {level}")
                for idx, riddle in enumerate(riddles):
                        
                    while not solve_riddle(current_level, riddle, ans[current_level - 1][idx]):
                        print(color.YELLOW + "1. Try again or go back." + color.RESET)
                        print(color.YELLOW + "2. Help with hint" + color.RESET)
                        print(color.YELLOW + "3. Save and Quit" + color.RESET)
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            print("Try again.")
                            solve_riddle(current_level, riddle, ans[current_level - 1][idx])
                        elif choice == 2:
                            if current_hints > 0:
                                print(color.GREEN +"Profile choosen name: " + name + color.RESET)
                                print(color.GREEN + name + "'s Hints left: " + str(current_hints) + color.RESET)
                                print(color.GREEN +"I hope this hint might help:- " + portal.hints[current_level - 1][idx] + color.RESET)
                                current_hints -= 1
                                solve_riddle(current_level, riddle, ans[current_level - 1][idx])
                            else:
                                print(color.RED+"No hints left"+color.RESET)
                                solve_riddle(current_level, riddle, ans[current_level - 1][idx])
                        elif choice == 3:
                            profile.save_player_data(name, current_hints, current_level, current_health)
                            exit()
                        else:
                            print("Please enter correct choice") 
                current_level += 1
                print(color.GREEN+"Proceeding to the next SUB-PORTAL."+color.RESET)
                logging.info(f"Player {player_name} proceeding to level ")  
                   

        
        if current_level > len(portal.levels):
            print(color.GREEN+"Congratulations! You've completed all SUB - PORTALS."+color.GREEN)
            

            
    except Exception as e:
        raise CustomException(e, sys)

