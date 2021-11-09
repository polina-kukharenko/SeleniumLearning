import unittest
from Chapter1.lesson6_step11 import test_registration


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        welcome_text = test_registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Actual result: {welcome_text}")

    def test_reg2(self):
        welcome_text = test_registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Actual result: {welcome_text}")


if __name__ == "__main__":
    unittest.main()
