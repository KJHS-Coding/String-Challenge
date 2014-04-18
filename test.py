import unittest
from src import  pangrams, vowels

class TestExercises(unittest.TestCase):
    
    def test_pangrams_quick_fox(self):
        self.assertTrue(pangrams.ispangram(
            'The quick brown fox jumps over a lazy dog.'),
            msg = 'Your algorithm needs to check for pangrams!'
        )

    def test_pangrams_fat_hags(self):
        self.assertTrue(pangrams.ispangram(
            'Fat hag dwarves quickly zap jinx mob.'),
            msg = ('Check your ispangram() algorithm.  '
            'Does it account for any sentence?')
        )

    def test_pangrams_fail(self):
        self.assertFalse(pangrams.ispangram(
            'This is not a pangram!'),
            msg = ('Check your ispangram() algorithm '
            'again because it lets non-pangrams pass!')
        )



if __name__ == "__main__":
    unittest.main()
