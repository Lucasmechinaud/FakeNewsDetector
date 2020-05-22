from django.test import TestCase
from polls import views

# Create your tests here.
class WrongInput(TestCase):
    def test_is_a_string(self):
        #score_creation should not work if we don't have a string
        self.assertRaises(views.NotAStringError,views.score_creation, 12)