from django.test import TestCase
import unittest
from polls import views

# Create your tests here.
class WrongInput(unittest.TestCase):
    def test_is_not_an_int(self):
        #score_creation should not work if we don't have an integrer
        self.assertRaises(views.NotAStringError,views.score_creation, 12)

if __name__ == "__main__":
    unittest.main()