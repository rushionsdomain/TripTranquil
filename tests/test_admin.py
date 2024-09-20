import unittest
from triptranquil.session.session import get_session
from triptranquil.models.admin import Admin

class TestAdmin(unittest.TestCase):
    def test_create_admin(self):
        session = get_session()
        admin = Admin(name="Admin User", email="admin@example.com", admin_code="ADM123")
        session.add(admin)
        session.commit()
        self.assertIsNotNone(admin.id)

if __name__ == "__main__":
    unittest.main()
