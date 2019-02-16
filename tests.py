from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_password_hashing(self):
		u = User(username = 'susan')
		u.set_password('cat')
		self.assertFalse(u.checking_password('dog'))
		self.assertTrue(u.checking_password('cat'))


	def test_avatar(self):
		u = User(username='john', email='john@example.com')
		self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
										'd4c74594d841139328695756648b6bd6'
										'?d=identicon&s=128'))

	def test_follow(self):
		u1 = User(username='john', email='john@example.com')
		u2 = User(username='susan', email='susan@example.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		self.assertEqual(u1.followed.all(), [])
		self.assertEqual(u2.followers.all(), [])

		u1.follow(u2)
		db.session.commit()
		self.assertTrue(u1.is_following(u2))
		self.assertEqual(u1.followed.count(), 1)
		self.assertEqual(u1.followed.first().username, 'susan')
		self.assertEqual(u2.followers.count(), 1)
		self.assertEqual(u2.followers.first().username, 'john')

		u1.unfollow(u2)
		db.session.commit()
		self.assertFalse(u1.is_following(u2))
		self.assertEqual(u1.followed.count(), 0)
		self.assertEqual(u2.followers.count(), 0)

	





