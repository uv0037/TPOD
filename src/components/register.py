import os
import json
from pathlib import Path
from logger import logging 

class Profile:

    def load_profiles(self):  
        profiles = []
        file_dir = "player_profiles/"
        for filename in os.listdir(file_dir):
            if filename.endswith('_profile.json'):
                profiles.append(filename.replace('_profile.json', ''))
        return profiles

    def load_profile(self, profile_name):  
        filename = f"player_profiles/{profile_name}_profile.json"
        with open(filename, 'r') as file:
            profile_data = json.load(file)
            print(f"Profile '{profile_name}' loaded:")
            print(json.dumps(profile_data, indent=4))

    def create_new_profile(self, name, hints=5, level=1): 
        profile_data = {
            "Name": name,
            "Hints": hints,
            "Level": level
        }

        profile_filename = f"player_profiles/{name.replace(' ', '_')}_profile.json"

        filepath = Path(profile_filename)

        if not filepath.exists():
            with open(filepath, 'w') as file:
                json.dump(profile_data, file)
            logging.info(f"Created profile: {filepath}")
        else:
            logging.info(f"Profile already exists: {filepath}")

    def select_profile(self):  
        profiles = self.load_profiles()  

        print("Available Profiles:")
        for index, profile in enumerate(profiles, start=1):
            print(f"{index}. {profile}")
        
        choice = input("Select a profile by name or create a new one by directly putting your name: ")
        if choice in profiles:
            print(f"Loading profile: {choice}")
            self.load_profile(choice)  
        else:
            self.create_new_profile(choice)  


