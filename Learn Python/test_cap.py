import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text1 = 'Gideon'.capitalize()
        text2 = 'Feyi'
        result = cap.cap_text(text1, text2)
        self.assertEqual(result, (text1, text2.capitalize()))


if __name__ == '__main__':
    unittest.main()