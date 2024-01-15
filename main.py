
from logger import logging
from exception import CustomException
from src.components.register import *
from src.components.portal_a import *
from src.components.portal_b import *
from src.utils import Color, draw_circle
import time
import sys

color = Color()

draw_circle(10)

print("  " * 10, end=' ')
sentence = "**************  WELCOME TO THE PORTALS OF DISORIENTATION  **************"
words = sentence.split()
for word in words:
    print(color.RED + word + color.RESET, end=' ', flush=True)
    time.sleep(0.5)

profile = Profile()
profile.select_profile()
profile_data = profile.load_profile(profile.profile_selected)


class Player:
    def __init__(self, name, hints, level, health, armour):
        self.player_name = name
        self.player_hints = hints
        self.player_level = level
        self.player_health = health
        self.player_armour = armour
        self.update_profile(name, hints, level, health, armour)

    def update_profile(self, name, hints, level, health, armour):
        self.player_name = name
        self.player_hints = hints
        self.player_level = level
        self.player_health = health
        self.player_armour = armour


player = Player(profile_data['Name'], profile_data['Hints'], profile_data['Level'], profile_data['Health'], profile_data['Armour'])



def profile_details(name, hints, level, health):
    print(color.GREEN + f"\nProfile chosen name: {name}" + color.RESET)
    print(color.GREEN + f"{name}'s Hints left: {hints}" + color.RESET)
    print(color.GREEN + f"{name}'s level: {level}" + color.RESET)
    print(color.GREEN + f"{name}'s health: {health}" + color.RESET)


profile_details(player.player_name, player.player_hints, player.player_level, player.player_health)  #display player profile stats


def main_menu():
    while True:
        print(color.RED + "  " * 22 + "*********  OPTIONS  *********" + color.RESET)
        print(color.YELLOW + "\n1. STORY MODE" + color.RESET)
        print(color.YELLOW + "2. CHANGE PROFILE" + color.RESET)
        print(color.YELLOW + "3. GAME MAP" + color.RESET)
        print(color.YELLOW + "4. QUIT GAME" + color.RESET)
        try:
            case = int(input(color.BLUE + "\nEnter your choice: " + color.RESET))
            if case == 1:
                story_mode()
                break
            elif case == 2:
                profile.select_profile()
                profile_data_new = profile.load_profile(profile.profile_selected)
                player.update_profile(profile_data_new['Name'], profile_data_new['Hints'], profile_data_new['Level'],
                                    profile_data_new['Health'], profile_data_new['Armour'])  #update the variables and return them.
                profile_details(player.player_name, player.player_hints, player.player_level,
                                player.player_health)
                main_menu()
                break
            elif case == 3:
                print(color.GREEN+"\n")
                time.sleep(1)
                print("PORTAL A  OR  PORTAL B\n")
                time.sleep(1)
                print("       Level 1 (Riddle level)")
                time.sleep(1)
                print("       Level 2 (Riddle level)")
                time.sleep(1)
                print("       Level 3 (Riddle level)")
                time.sleep(1)
                print("       Level 4 (Monster level)\n")
                time.sleep(1)
                print("       PORTAL C\n")
                time.sleep(1)
                print("LAST LEVEL (Missionaries and Cannibals)\n")
                time.sleep(1)
                print("      GAME COMPLETED!"+color.RESET)
            elif case == 4:
                exit()
        except ValueError:
            print(color.RED + "\nPlease enter a valid number for the choice.")
            print(color.BLUE + "Redirecting you to menu" + color.RESET)
            print(color.GREY + "**" * 20 + "\n" + color.RESET)


def story_mode():
    if player.player_level <= 1:
        while True:
            print(color.RED + "  " * 22 + "*********  OPTIONS  *********" + color.RESET)
            print(color.YELLOW + "\n1. NEW GAME" + color.RESET)
            print(color.YELLOW + "2. BACK" + color.RESET)
            try:
                new_case = int(input(color.BLUE + "\nEnter your choice: " + color.RESET))
                execute_story_mode_case_new(new_case)
            except ValueError:
                print(color.RED + "\nPlease enter a valid number for the choice.")
                print(color.BLUE + "Redirecting you to previous menu" + color.RESET)
                print(color.GREY + "**" * 20 + "\n" + color.RESET)
    else:
        while True:
            print(color.RED + "  " * 22 + "*********  OPTIONS  *********" + color.RESET)
            print(color.YELLOW + "\n1. NEW GAME" + color.RESET)
            print(color.YELLOW + "2. RESUME" + color.RESET)
            print(color.YELLOW + "3. WAR GEAR" + color.RESET)
            print(color.YELLOW + "4. BACK" + color.RESET)
            try:
                case = int(input(color.BLUE + "\nEnter your choice: " + color.RESET))
                execute_story_mode_case(case)
            except ValueError:
                print(color.RED + "\nPlease enter a valid number for the choice.")
                print(color.BLUE + "Redirecting you to previous menu" + color.RESET)
                print(color.GREY + "**" * 20 + "\n" + color.RESET)
            except Exception as e:
                CustomException(e, sys)


def execute_story_mode_case_new(new_case):
    if new_case == 1:
        new_game()
    elif new_case == 2:
        main_menu()
    else:
        story_mode()


def execute_story_mode_case(case):
    if case == 1:
        new_game()
    elif case == 2:
        resume()
    elif case == 3:
        war_gear()
    elif case == 4:
        main_menu()
    else:
        story_mode()


def war_gear():
        print(color.YELLOW+"\n1. Take armour")
        print(color.YELLOW+"\n2. Back")
        try:
            case = int(input(color.BLUE + "\nEnter your choice: " + color.RESET))
            if case == 1:
                if player.player_level >= 2 and player.player_hints > 1:
                    player.player_armour = 50
                    print(color.GREEN + f"{player.player_name}'s armour: {player.player_armour}" + color.RESET)
                else:
                    print(color.RED+"\n Your are not eligible for armour"+color.RESET)
            elif case == 2:
                story_mode()
                   
        except ValueError:
            print(color.RED + "\nPlease enter a valid number for the choice.")
            print(color.BLUE + "Redirecting you to previous menu" + color.RESET)
            print(color.GREY + "**" * 20 + "\n" + color.RESET)
        except Exception as e:
            CustomException(e, sys)


def new_game():
    print(color.RED + "  " * 22 + "*********  PORTALS  *********" + color.RESET)    #game starts giving you options to start with.
    print(color.YELLOW + "\n1. PORTAL A" + color.RESET)
    print(color.YELLOW + "2. PORTAL B" + color.RESET)
    print(color.YELLOW + "3. GO TO MAIN MENU" + color.RESET)
    print(color.YELLOW + "4. QUIT" + color.RESET)
    try:
        portal_choice = int(input(color.BLUE + "\nEnter your choice: " + color.RESET))

        if portal_choice == 1:
            draw_circle(10)
            print("  " * 15, end=' ')
            sentence = "**********  WELCOME TO PORTAL A  **********"
            words = sentence.split()
            for word in words:
                print(color.RED + word + color.RESET, end=' ', flush=True)
                time.sleep(0.5)
            print("\n")
            sentence_a = "********** Step into Portal A, where the whispers of nature echo, and mysteries await amidst serene landscapes and ancient wonders. **********"
            words = sentence_a.split()
            for word in words:
                print(color.GREEN + word + color.RESET, end=' ', flush=True)
                time.sleep(0.2)
            
            player.player_hints = 3
            player.player_level = 1
            player.player_health = 100
            b = 0
            play_level(player.player_name, player.player_hints, player.player_level, player.player_health, player.player_armour, b)  #traverse to portal A
            logging.info(f" {player.player_name} enters portal A")
        elif portal_choice == 2:
            draw_circle(10)
            print("  " * 15, end=' ')
            sentence = "**********  WELCOME TO PORTAL B  **********"
            words = sentence.split()
            for word in words:
                print(color.RED + word + color.RESET, end=' ', flush=True)
                time.sleep(0.5)
            print("\n")
            sentence_b = "********** Welcome to Portal B, where the pulse of technology beats strong, revealing innovations and digital marvels in an ever-evolving world. **********"
            words = sentence_b.split()
            for word in words:
                print(color.GREEN + word + color.RESET, end=' ', flush=True)
                time.sleep(0.2)
            
            player.player_hints = 3
            player.player_level = 1
            player.player_health = 100
            b = 1
            play_level_b(player.player_name, player.player_hints, player.player_level, player.player_health, player.player_armour, b)  #traverse to portal B 
            logging.info(f" {player.player_name} enters portal A")
        elif portal_choice == 3:
            main_menu()
        elif portal_choice == 4:
            exit()
        else:
            new_game()
    except ValueError:
        print(color.RED + "\nPlease enter a valid number for the choice.")
        print(color.BLUE + "Redirecting you to previous menu" + color.RESET)
        print(color.GREY + "**" * 20 + "\n" + color.RESET)
    except Exception as e:
        CustomException(e, sys)


def resume():               #resume from the level the game was saved
    try:
        if profile_data.get('Portal_b_stump') == 1:
            play_level_b(player.player_name, player.player_hints, player.player_level, player.player_health, player.player_armour, 1)   
        elif profile_data.get('Portal_b_stump') == 0:
            play_level(player.player_name, player.player_hints, player.player_level, player.player_health, player.player_armour, 0)
        else:
            print("ERROR")
    except Exception as e:
        CustomException(e, sys)

if __name__=="__main__":
    main_menu()

