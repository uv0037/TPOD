from logger import logging
from src.components.register import *
from src.components.portal_a_rid import *
from color import Color

color = Color()

print(color.RED + "**************WELCOME TO THE PORTALS OF DISORIENTATION**************" + color.RESET)

profile = Profile()
profile.select_profile()

profile_data = profile.load_profile(profile.choice)

print(color.GREEN +"Profile choosen name: " + str(profile_data['Name']) + color.RESET)
player_name = profile_data['Name']
print(color.GREEN + profile_data['Name'] + "'s Hints left: " + str(profile_data['Hints']) + color.RESET)
player_hints = profile_data['Hints']
print(color.GREEN +profile_data['Name'] + "'s level: "+ str(profile_data['Level']) + color.RESET)
player_level = profile_data['Level']
print(color.GREEN + profile_data['Name'] + "'s health: " + str(profile_data['Health']) + color.RESET)
player_health = profile_data['Health']



def main_menu():
    print(color.RED + "\n*********OPTIONS*********" + color.RESET)
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
    print(color.RED + "\n*********OPTIONS*********" + color.RESET)
    if player_level==1:
        print(color.YELLOW+"\n 1. NEW GAME"+ color.RESET)
        print(color.YELLOW+"\n 2. WAR GEAR"+ color.RESET)
        print(color.YELLOW+"\n 3. BACK"+ color.RESET)
    else:
        print(color.YELLOW+"\n 1. NEW GAME"+ color.RESET)
        print(color.YELLOW+"\n 2. RESUME"+ color.RESET)
        print(color.YELLOW+"\n 3. WAR GEAR"+ color.RESET)
        print(color.YELLOW+"\n 4. BACK"+ color.RESET)
    case = int(input(color.BLUE+"\n Enter your choice: "+ color.RESET))
    
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

main_menu()


def new_game():
    print(color.RED+ "\n*********PORTALS*********"+color.RESET)
    print(color.YELLOW+"1. Portal A"+color.RESET)
    print(color.YELLOW+"2. Portal B"+color.RESET)
    print(color.YELLOW+"3. Save and Quit"+color.RESET)
    
    portal_choice = int(input("Enter your choice: "))

    if portal_choice == 1 or portal_choice == 2:
        portal_level = player_level 

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
        portala() '''




