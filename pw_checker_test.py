import unittest
from unittest.mock import patch
from password_checker import password_checker


class PasswordTestCase(unittest.TestCase):
    """Tests for password checker"""

    @patch('builtins.input', side_effect=["password123", "CommonPassword", "19cR4cKm387!asdf"])
    def test_password_checker(self, mock_input):
        """Does the password checker work?"""
        result = password_checker()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
