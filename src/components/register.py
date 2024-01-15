import os
import sys
import json
from pathlib import Path
import logging
import logger
from exception import CustomException
from src.utils import Color


color = Color()

class Profile:
    def __init__(self) -> None:
        pass

    def load_profiles(self):  
        try:
            profiles = []
            file_dir = "player_profiles/"
            for filename in os.listdir(file_dir):
                if filename.endswith('_profile.json'):
                    profiles.append(filename.replace('_profile.json', ''))
            return profiles
        except Exception as e:
            raise CustomException(e, sys)

    def load_profile(self, profile_name):
        try:  
            filename = f"player_profiles/{profile_name}_profile.json"
            with open(filename, 'r') as file:
                self.profile_data = json.load(file)
                return self.profile_data
        except Exception as e:
            raise CustomException(e, sys)
        
            

    def create_new_profile(self, name, hints=3, level=1, health=100, armour=0, b=0):
        try: 
            profile_data = {
                "Name": name,
                "Hints": hints,
                "Level": level,
                "Health": health,
                "Armour": armour,
                "Portal_b_stump": b
            }

            profile_filename = f"player_profiles/{name.replace(' ', '_')}_profile.json"

            filepath = Path(profile_filename)

            if not filepath.exists():
                with open(filepath, 'w') as file:
                    json.dump(profile_data, file)
                print(color.BLUE+"PROFILE CREATED, username - "+color.GREEN+f"{name}"+color.RESET)
                logging.info(f"Created profile: {filepath}")
                
            else:
                print(color.RED+"\nUSER NAME ALREADY EXISTS")
                print(color.BLUE+"Please create profile using a unique user name\n"+color.RESET)
                logging.info(f"Profile already exists: {filepath}")
        except Exception as e:
            raise CustomException(e, sys)

    def select_profile(self):
        try:  
            while True:
                profiles = self.load_profiles() 
                print("\n"+color.GREY+"*"*20+color.RESET)
                print(color.YELLOW + " AVAILABLE PROFILES:" + color.RESET)
                print(color.GREY+"*"*20+color.RESET)
                for index, profile in enumerate(profiles, start=1):
                    print(color.GREEN + f"{index}. {profile}" + color.RESET)
    
                print(color.YELLOW + "\n1. SELECT PROFILE" + color.RESET)
                print(color.YELLOW + "2. CREATE NEW PROFILE" + color.RESET)
                print(color.YELLOW + "3. DELETE PROFILE" + color.RESET)
                print(color.YELLOW + "4. QUIT" + color.RESET)
                try:
                    self.choice = int(input(color.BLUE + "\nSelect your choice: " + color.RESET))
                    if self.choice == 1:
                        self.profile_selected = input(color.BLUE + "\nSelect your user name from available profiles: " + color.RESET)
                        if self.profile_selected in profiles:
                            print(color.BLUE+f"\nLoading profile: "+color.GREEN+f"{self.profile_selected}"+color.RESET)
                            self.load_profile(self.profile_selected)
                            break
                        else:
                            print(color.RED+"\nProfile not found or please check the profile name"+color.RESET)
                            print(color.BLUE+"Redirecting you to main menu"+color.RESET)
                            print(color.GREY+"**"*20+"\n"+color.RESET)
                            continue
                    elif self.choice == 2:
                        self.new_profile = input(color.BLUE + "\nEnter your user name: " + color.RESET)
                        self.create_new_profile(self.new_profile)
                        continue
                    elif self.choice == 3:
                        self.delete_profile = input(color.BLUE + "\nEnter the profile name to be deleted: " + color.RESET)
                        self.delete_file(self.delete_profile)
                        continue
                    elif self.choice == 4:
                        exit()
                    else:
                        print(color.BLUE + "\nPlease enter correct choice" + color.RESET)
                        continue
                except ValueError:
                    print(color.RED+"\nPlease enter a valid number for the choice.")
                    print(color.BLUE+"Redirecting you to main menu"+color.RESET)
                    print(color.GREY+"**"*20+"\n"+color.RESET)

        except Exception as e:
            raise CustomException(e, sys)


      

    def delete_file(self, filename):
        try:
            file_path = f"player_profiles/{filename}_profile.json"

            if os.path.exists(file_path) and file_path.endswith('_profile.json'):
                os.remove(file_path)
                print(color.GREEN+f"\nProfile deleted '{filename}' deleted successfully."+color.RESET)
                logging.info(f"Profile deleted '{filename}' deleted successfully.")
            else:
                print(color.RED+f"Profile - '{filename}' not found."+color.RESET)
        except Exception as e:
            raise CustomException(e, sys)
        
    

    def save_player_data(self, player_name, player_hints, player_level, player_health, player_armour, b):
        try:
            player_data = {
                "Name": player_name,
                "Hints": player_hints,
                "Level": player_level,
                "Health": player_health,
                "Armour": player_armour,
                "Portal_b_stump": b
            }

            filename = f"player_profiles/{player_name}_profile.json"

            with open(filename, 'w') as file:
                json.dump(player_data, file)
        except Exception as e:
            raise CustomException(e, sys)

