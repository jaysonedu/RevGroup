import unittest
from app import app

class MyAppTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test the home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to MyApp", response.data)  # Update the string to match your homepage content.

    def test_404(self):
        """Test a route that does not exist."""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
