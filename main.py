
from logger import logging
from exception import CustomException
from src.components.register import *
from src.components.portal_a import *
from src.components.portal_b import *
from src.utils import Color, draw_circle
import time

color = Color()

draw_circle(10)

print("  "*10, end=' ')
sentence = "**************  WELCOME TO THE PORTALS OF DISORIENTATION  **************"
words = sentence.split()  
for word in words:
    print(color.RED+word+color.RESET, end=' ', flush=True)
    time.sleep(0.5)

profile = Profile()
profile.select_profile()
profile_data = profile.load_profile(profile.profile_selected)


class Player:
    def __init__(self, name, hints, level, health):
        self.player_name = name
        self.player_hints = hints
        self.player_level = level
        self.player_health = health

player = Player(profile_data['Name'],profile_data['Hints'],profile_data['Level'],profile_data['Health'])

def profile_details(name, hints, level, health):
    print(color.GREEN +"\nProfile choosen name: " + name + color.RESET)
    print(color.GREEN + player.player_name  + "'s Hints left: " + str(hints) + color.RESET)
    print(color.GREEN + player.player_name  + "'s level: "+ str(level ) + color.RESET)
    print(color.GREEN + player.player_name  + "'s health: " + str(health) + color.RESET)
profile_details(player.player_name, player.player_hints, player.player_level, player.player_health)

def main_menu():
    while True:
        print(color.RED +"  "*22+ "*********  OPTIONS  *********" + color.RESET)
        print(color.YELLOW+"\n1. STORY MODE"+color.RESET)
        print(color.YELLOW+"2. CHANGE PROFILE"+color.RESET)
        print(color.YELLOW+"3. SETTINGS"+color.RESET)
        print(color.YELLOW+"4. QUIT GAME"+color.RESET)
        try:
            case = int(input(color.BLUE+"\nEnter your choice: "+ color.RESET))
            if case == 1:
                story_mode()
                break
            elif case == 2:
                profile.select_profile()
                profile_data = profile.load_profile(profile.profile_selected)
                player_new = Player(profile_data['Name'],profile_data['Hints'],profile_data['Level'],profile_data['Health'])
                profile_details(player_new.player_name, player_new.player_hints, player_new.player_level, player_new.player_health)
                main_menu()
                break
            elif case == 3:
                settings()
            elif case == 4:
                exit()
        except ValueError:
                    print(color.RED+"\nPlease enter a valid number for the choice.")
                    print(color.BLUE+"Redirecting you to menu"+color.RESET)
                    print(color.GREY+"**"*20+"\n"+color.RESET)
def story_mode():
    if player.player_level<=1:
        while True:
            print(color.RED +"  " *22 + "*********  OPTIONS  *********" + color.RESET)
            print(color.YELLOW+"\n1. NEW GAME"+ color.RESET)
            print(color.YELLOW+"2. WAR GEAR"+ color.RESET)
            print(color.YELLOW+"3. BACK"+ color.RESET)
            try:
                new_case = int(input(color.BLUE+"\nEnter your choice: "+ color.RESET))
                execute_story_mode_case_new(new_case)
            except ValueError:
                    print(color.RED+"\nPlease enter a valid number for the choice.")
                    print(color.BLUE+"Redirecting you to previous menu"+color.RESET)
                    print(color.GREY+"**"*20+"\n"+color.RESET)
    else:
        while True:
            print(color.RED +"  " *22 + "*********  OPTIONS  *********" + color.RESET)
            print(color.YELLOW+"\n1. NEW GAME"+ color.RESET)
            print(color.YELLOW+"2. RESUME"+ color.RESET)
            print(color.YELLOW+"3. WAR GEAR"+ color.RESET)
            print(color.YELLOW+"4. BACK"+ color.RESET)
            try:
                case = int(input(color.BLUE+"\nEnter your choice: "+ color.RESET))
                execute_story_mode_case(case)
            except ValueError:
                    print(color.RED+"\nPlease enter a valid number for the choice.")
                    print(color.BLUE+"Redirecting you to previous menu"+color.RESET)
                    print(color.GREY+"**"*20+"\n"+color.RESET)
def execute_story_mode_case_new(new_case):
    if new_case == 1:
        new_game()
    elif new_case == 2:
        war_gear()
    elif new_case == 3:
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




def new_game():
    try:
        print(color.RED+ "  " *22 +"*********  PORTALS  *********"+color.RESET)
        print(color.YELLOW+"1. PORTAL A"+color.RESET)
        print(color.YELLOW+"2. PORTAL B"+color.RESET)
        print(color.YELLOW+"3. GO TO MAIN MENU"+color.RESET)
        print(color.YELLOW+"4. QUIT"+color.RESET)
        portal_choice = int(input(color.BLUE+"\nEnter your choice: "+ color.RESET))

        if portal_choice == 1:
            #print(color.RED+"  "*22 + "*********  WELCOME TO PORTAL A  *********"+color.RESET)
            print("  "*22, end=' ')
            sentence = "**********  WELCOME TO PORTAL A  **********"
            words = sentence.split()  
            for word in words:
                print(color.RED+word+color.RESET, end=' ', flush=True)
                time.sleep(0.5)
            b = 0 
            player.player_level = 1
            play_level(player.player_name, player.player_hints, player.player_level, player.player_health, b)
        elif portal_choice == 2:
            #print(color.RED+"  "*22 + "*********  WELCOME TO PORTAL B  *********"+color.RESET)
            print("  "*22, end=' ')
            sentence = "**********  WELCOME TO PORTAL B  **********"
            words = sentence.split()  
            for word in words:
                print(color.RED+word+color.RESET, end=' ', flush=True)
                time.sleep(0.5)
            b = 1 
            player.player_level = 1    
            play_level_b(player.player_name, player.player_hints, player.player_level, player.player_health, b)
        elif portal_choice == 3:
            main_menu()
        elif portal_choice == 4:
            exit()
        else:
            print("\n Please enter correct choice")

                

    except Exception as e:
        CustomException(e, sys)


     


def resume():
    try:
        print("ERROR")
        if profile_data['Portal_b_stump'] == 1:
            play_level_b(player.player_name, player.player_hints, player.player_level, player.player_health)
        elif profile_data['Portal_b_stump'] == 0:
            play_level(player.player_name, player.player_hints, player.player_level, player.player_health)
        else:
            print("ERROR")
        
    except Exception as e:
        CustomException(e, sys)

main_menu()
'''
def war_gear():
    # Logic for accessing war gear

def settings():
    # Logic for game settings

# Initial call to start the game
main_menu()


def execute_case(case):
    if case == 1:
        story_mode()
    elif case == 2:
        profile.select_profile()
    elif case == 3:
        settings()
    elif case == 4:
        exit()
    else:
        story_mode()


def story_mode():
    print("*********OPTIONS*********")
    print("\n 1. NEW GAME")
    print("\n 2. RESUME")
    print("\n 3. WAR GEAR")
    print("\n 4. BACK")
    case = int(input("\n Enter your choice: "))
    execute_story_mode_case(case)


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


def new_game():
    new_profile_level = 1
    profile.level = new_profile_level

    print("\n 1: PORTAL A")
    print("\n 2: PORTAL B")
    
    case = int(input("\n Give your choice: "))
    choose_portal(case)


def choose_portal(case):
    if case == 1:
        portala()
    elif case == 2:
        portalb()
    else:
        portala() 

class Player:
    def __init__(self, portal_level=1):
        self.portal_level = portal_level

player = Player()
portal = Portal()
play_level(player, portal)


'''

