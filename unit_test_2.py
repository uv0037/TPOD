import unittest
from unittest.mock import patch
from src.components.portal_a import fight, Monster 

class TestFightFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '3', '2'])  
    def test_fight_with_mocked_input(self):
        player_name = "TestPlayer"
        player_hints = 3
        player_level = 1
        player_health = 100
        player_armour = 0
        monster = Monster("SHADOWFANG", health=120, attack_power=15)

        with patch('sys.stdout', return_value=None): 
            fight(player_name, player_hints, player_level, player_health, player_armour, monster)



if __name__ == '__main__':
    unittest.main()
