import unittest
from machinetranslation.translator import english_to_french, french_to_english

class testing(unittest.TestCase):
    def test_en_fr (self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_fr_en (self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")

    def test_null (self):
        self.assertEqual(english_to_french(" ")," ")
        self.assertEqual(french_to_english(" ")," ")

if __name__ == "__main__":
    unittest.main()