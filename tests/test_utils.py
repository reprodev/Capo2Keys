import unittest
from utils import slugify

class TestUtils(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
        self.assertEqual(slugify("Song! @# Title"), "song-title")
        self.assertEqual(slugify("  Trim Me  "), "trim-me")
        self.assertEqual(slugify(""), "chord-sheet")
        self.assertEqual(slugify(None), "chord-sheet")

if __name__ == '__main__':
    unittest.main()
