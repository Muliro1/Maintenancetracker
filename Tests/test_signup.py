import unittest

from signup import Signup

class testSignup(unittest.TestCase):
	def setUp(self):
		self.User1 = Signup('mulirokhaemba@gmail.com', 'Michael', 'Muliro', 'Muliro1', 'rebirth')
	def test_set_email(self):
		self.User1.set_email()
		self.assertEqual(self.User1.user_info[0]['email'], 'mulirokhaemba@gmail.com')
	def test_set_names(self):
		self.User1.set_names()
		self.assertEqual(self.User1.user_info[0]['names'], 'Michael Muliro')
	def test_username(self):
		self.User1.set_username()
		self.assertEqual(self.User1.user_info[0]['username'], 'Muliro1')
	def test_password(self):
		self.User1.set_password()
		self.assertEqual(self.User1.user_info[0]['password'], 'rebirth')



if __name__ == '__main__':
	unittest.main()

