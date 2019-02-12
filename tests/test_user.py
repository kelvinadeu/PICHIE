import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        '''
        set up will run before every test
        '''
        self.new_user = User(id = 1, username = "Adeu", email = "kelvinadeu25@gmail.com", password_hash = "0713730881")

    def test_instance(self):
        '''
        test case to check if new instance is created
        '''
        self.assertTrue(isinstance(self.new_user, User))

    def test_password_setter(self):
        '''
        test to check if password is being hashed
        '''
        self.assertTrue(self.new_user.password_0713730881 is not None)
