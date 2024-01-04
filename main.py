
from logger import logging
from exception import CustomException
from src.components.register import *
from portal_a import *
from color import Color
from spiral import draw_circle

color = Color()

draw_circle(10)
print(color.RED +"  "*10+ "**************  WELCOME TO THE PORTALS OF DISORIENTATION  **************" + color.RESET)

profile = Profile()
profile.select_profile()



class Player:
    def __init__(self):
        self.profile_data = profile.load_profile(profile.profile_selected)
        self.player_name = self.profile_data['Name']
        self.player_hints = self.profile_data['Hints']
        self.player_level = self.profile_data['Level']
        self.player_health = self.profile_data['Health']

player = Player()

def profile_details():
    print(color.GREEN +"Profile choosen name: " + player.player_name + color.RESET)
    print(color.GREEN + player.player_name  + "'s Hints left: " + str(player.player_hints) + color.RESET)
    print(color.GREEN + player.player_name  + "'s level: "+ str(player.player_level ) + color.RESET)
    print(color.GREEN + player.player_name  + "'s health: " + str(player.player_health ) + color.RESET)
profile_details()

def main_menu():
    print(color.RED +"  "*22+ "*********  OPTIONS  *********" + color.RESET)
    print(color.YELLOW+"\n 1. STORY MODE"+color.RESET)
    print(color.YELLOW+"\n 2. CHANGE PROFILE"+color.RESET)
    print(color.YELLOW+"\n 3. SETTINGS"+color.RESET)
    print(color.YELLOW+"\n 4. QUIT GAME"+color.RESET)
    case = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))
    
    execute_case(case)
    

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
        main_menu()

def story_mode():
    print(color.RED +"  " *22 + "*********  OPTIONS  *********" + color.RESET)
    if player.player_level==1:
        print(color.YELLOW+"\n 1. NEW GAME"+ color.RESET)
        print(color.YELLOW+"\n 2. WAR GEAR"+ color.RESET)
        print(color.YELLOW+"\n 3. BACK"+ color.RESET)
        new_case = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))
        execute_story_mode_case_new(new_case)
    else:
        print(color.YELLOW+"\n 1. NEW GAME"+ color.RESET)
        print(color.YELLOW+"\n 2. RESUME"+ color.RESET)
        print(color.YELLOW+"\n 3. WAR GEAR"+ color.RESET)
        print(color.YELLOW+"\n 4. BACK"+ color.RESET)
        case = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))
        execute_story_mode_case(case)

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
        print(color.YELLOW+"1. Portal A"+color.RESET)
        print(color.YELLOW+"2. Portal B"+color.RESET)
        print(color.YELLOW+"3. Quit"+color.RESET)
        portal_choice = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))

        if portal_choice == 1:
            print(color.RED+"  "*22 + "*********  WELCOME TO PORTAL A  *********"+color.RESET)
            #player.player_level = 1
            play_level(player.player_name, player.player_hints, player.player_level, player.player_health )
        elif portal_choice == 2:
            print(color.RED+"  "*22 + "*********  WELCOME TO PORTAL B  *********"+color.RESET)
        elif portal_choice == 3:
            new_game()
        else:
            print("\n Please enter correct choice")

                

    except Exception as e:
        CustomException(e, sys)


main_menu()        

'''
def resume():
    # Logic for resuming the game

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

