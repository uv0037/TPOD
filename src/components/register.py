import os
import sys
import json
from pathlib import Path
from logger import logging 
from exception import CustomException
from color import Color


color = Color()

class Profile:

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
            #print(f"Profile loaded for {self.profile_data}")
                return self.profile_data
        except Exception as e:
            raise CustomException(e, sys)
        
            

    def create_new_profile(self, name, hints=5, level=1, health=100):
        try: 
            profile_data = {
                "Name": name,
                "Hints": hints,
                "Level": level,
                "Health": health
            }

            profile_filename = f"player_profiles/{name.replace(' ', '_')}_profile.json"

            filepath = Path(profile_filename)

            if not filepath.exists():
                with open(filepath, 'w') as file:
                    json.dump(profile_data, file)
                logging.info(f"Created profile: {filepath}")
            else:
                logging.info(f"Profile already exists: {filepath}")
        except Exception as e:
            raise CustomException(e, sys)

    def select_profile(self):
        try:  
            profiles = self.load_profiles()  

            print(color.YELLOW+"Available Profiles:"+color.RESET)
            for index, profile in enumerate(profiles, start=1):
                print(color.GREEN+ f"{index}. {profile}" + color.RESET)
        
            print(color.YELLOW+"\n 1. Select profile"+color.RESET)
            print(color.YELLOW+"\n 2. Create new profile"+color.RESET)
            print(color.YELLOW+"\n 3. Delete profile"+color.RESET)
            print(color.YELLOW+"\n 4. Quit"+color.RESET)
            self.choice = int(input(color.BLUE+"\nSelect you choice: "+color.RESET))
            if self.choice==1:
                self.profile_selected = input(color.BLUE+"\nSelect your profile name: "+color.RESET)
                if self.profile_selected in profiles:
                    print(f"\nLoading profile: {self.profile_selected} ")
                    self.load_profile(self.profile_selected)
                else:
                    print("Profile not found") 
            elif self.choice==2:
                self.new_profile = input(color.BLUE+"\nEnter your profile name: "+color.RESET)
                self.create_new_profile(self.new_profile)
                self.select_profile()
            elif self.choice==3:
                self.delete_profile = input(color.BLUE+"\nEnter the profile name to be deleted: "+color.RESET)
                self.delete_json_file(self.delete_profile)
                self.select_profile()
            else:
                exit()
        except Exception as e:
            raise CustomException(e, sys)
              

    def delete_json_file(self, filename):
        try:
            file_path = f"player_profiles/{filename}_profile.json"

            if os.path.exists(file_path) and file_path.endswith('_profile.json'):
                os.remove(file_path)
                print(f"Profile deleted '{filename}' deleted successfully.")
                logging.info(f"Profile deleted '{filename}' deleted successfully.")
            else:
                print(f"Profile - '{filename}' not found.")
        except Exception as e:
            raise CustomException(e, sys)
        
    

    def save_player_data(self, player_name, player_hints, player_level, player_health):
        try:
            player_data = {
                "Name": player_name,
                "Hints": player_hints,
                "Level": player_level,
                "Health": player_health,
                
            }

            filename = f"player_profiles/{player_name}_profile.json"

            with open(filename, 'w') as file:
                json.dump(player_data, file)
        except Exception as e:
            raise CustomException(e, sys)




        
        






