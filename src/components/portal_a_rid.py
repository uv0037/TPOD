class PortalA:
    def __init__(self):
        pass

    def choose_portal(player):
        while True:
             
                if portal_level in [4, 6]:  
                    print(f"Monster level {portal_level}. Defeat the monster!")
                
                else:  # Regular levels with riddles
                    if portal_level <= 7:  
                        print(f"Riddle {portal_level} for Portal {chr(64 + portal_choice)}")
                    # Implement riddle for the level
                        player.portal_level += 1  # Move to the next level
                    else:
                        print("Congratulations! You completed all levels.")
            # Implement saving at any point functionality
            elif portal_choice == 3:
                print("Game Saved.")
                break  # Save and quit
            else:
                print("Invalid choice. Please choose again.")
