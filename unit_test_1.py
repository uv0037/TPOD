import unittest
from mock import patch
from src.components.portal_b import solve_riddle  

class TestRiddle(unittest.TestCase):
    def test_correct_answer(self):
        level = 1
        riddle = "I'm a speedy messenger, carrying information fast. Emails and files, in the blink of an eye, I cast. What am I?"
        answer = "internet"
        
        with patch('builtins.input', return_value="internet"):
            result = solve_riddle(level, riddle, answer)
        
        self.assertTrue(result)

    def test_incorrect_answer(self):
        level = 2
        riddle = "I'm a connection hub, linking devices together. Wi-Fi waves dance, in my invisible tether. What am I?"
        answer = "router"
        
        with patch('builtins.input', return_value="abc"):
            result = solve_riddle(level, riddle, answer)
        
        self.assertFalse(result)

    def test_case_insensitive_answer(self):
        level = 3
        riddle = "I'm a pocket-sized marvel, a world in your hand. Apps and messages at your command. What am I?"
        answer = "SMARTPHONE"
        
        with patch('builtins.input', return_value="smartphone"):
            result = solve_riddle(level, riddle, answer)
        
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
