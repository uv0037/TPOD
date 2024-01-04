import sys
import random
from color import Color
from logger import logging
from exception import CustomException
from src.components.register import Profile




color = Color()
profile = Profile()

class PortalA:
    def __init__(self):
        self.levels = {
            1: ["What has keys but can't open locks?", "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "What gets wetter as it dries?"],
            2: ["I'm tall when I'm young, and I'm short when I'm old. What am I?", "What has a head, a tail, but no body?", "The more you take, the more you leave behind. What am I?"],
            3: ["What has many keys but can't open a single lock?", "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?", "I'm light as a feather, yet the strongest person can't hold me for more than five minutes. What am I?"],
            4: ["What has a neck but no head?", "What is full of holes but can still hold water?", "What belongs to you but is used more by others?"],
            5: ["What can be cracked, made, told, and played?", "What has keys but can't open locks?", "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"],
            6: ["What has hands but cannot clap?", "What has a head and a tail but no body?", "What is always in front of you but can't be seen?"],
            7: ["What has keys but can't open locks?", "What gets wetter as it dries?", "What can be cracked, made, told, and played?"]
        }
        self.answers = [
                    ["piano", "echo", "towel"],
                    ["candle", "coin", "footsteps"],
                    ["piano", "pencil", "breath"],
                    ["neck", "sponge", "name"],
                    ["a joke", "piano", "echo"],
                    ["a clock", "a coin", "tomorrow"],
                    ["piano", "towel", "a joke"]
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
            print("Correct answer!")
            return True
        else:
            print("Incorrect answer!")
            return False
    except Exception as e:
        raise CustomException(e, sys)

def create_monster(level):
    if level == 4:
        return Monster("Shadowfang", health=120, attack_power=15)
    elif level == 6:
        return Monster("Frostclaw", health=150, attack_power=20)
        


        

def fight(player_health, monster):
    try:
        print(f"A wild {monster.name} appears!")
        while player_health > 0 and monster.is_alive():
            player_attack = random.randint(20, 30)  
            monster.take_damage(player_attack)
            print(f"You attack the {monster.name} with power {player_attack}. Its health is now {monster.health}")

            if not monster.is_alive():
                break  

    
            monster_attack = random.randint(15, 25)
            player_health -= monster_attack
            print(f"The {monster.name} attacks you with power {monster_attack}. Your armour level is now {player_health}")

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
            riddles_level = portal.levels.items()
            ans = portal.answers
            for level, riddles in riddles_level:
                print(f"Level : {level}")
                for idx, riddle in enumerate(riddles):
                        
                    if not solve_riddle(current_level, riddle, ans[current_level - 1][idx]):
                        print(color.YELLOW + "1. Try again or go back." + color.RESET)
                        print(color.YELLOW + "2. Save and Quit" + color.RESET)
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            print("Try again.")
                            solve_riddle(current_level, riddle, ans[current_level - 1][idx])
                            #play_level(player_name, player_hints, player_level, player_health)
                            #return  # Break the loop to retry the same level
                            
                        elif choice == 2:
                            profile.save_player_data(name, current_hints, current_level, current_health)
                            exit()
                        else:
                            print("Please enter correct choice")
                    else:
                        print("Proceeding to the next level.")
                current_level += 1
                if current_level in [4, 6]:  
                    print(f"Monster level {current_level}. Prepare for a fight!")
                    monster = create_monster(current_level)  
                    fight(current_health, monster)        

                #for idx, riddle in enumerate(riddles, start=1):
                    

            #if current_level == 4 or current_level == 6:
             #   break  # Break out of the loop for monster levels
        
        if current_level > len(portal.levels):
            print("Congratulations! You've completed all levels.")
            
    except Exception as e:
        raise CustomException(e, sys)


'''

    else:  # Regular levels with riddles
        riddles = portal.levels[current_level]
        answers = [
            ["piano", "echo", "towel"],
            ["candle", "coin", "footsteps"],
            ["piano", "pencil", "breath"],
            ["neck", "sponge", "name"],
            ["a joke", "piano", "echo"],
            ["a clock", "a coin", "tomorrow"],
            ["piano", "towel", "a joke"]
        ]  # Answers for the riddles

        for idx, riddle in enumerate(riddles):
            if not solve_riddle(current_level, riddle, answers[current_level - 1][idx]):
                print("Try again or go back.")
                play_level(player, portal)  # Recursive call if the answer is incorrect
                return
            else:
                print("Proceeding to the next level.")
                player.portal_level += 1

        print("Congratulations! You've completed all riddles in this level.")

   ''' 

