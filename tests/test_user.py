import unittest
from triptranquil.session.session import get_session
from triptranquil.models.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        session = get_session()
        user = User(name="Test User", email="test@example.com")
        session.add(user)
        session.commit()
        self.assertIsNotNone(user.id)

if __name__ == "__main__":
    unittest.main()
