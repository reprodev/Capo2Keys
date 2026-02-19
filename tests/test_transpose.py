import unittest
from transpose_chords import transpose_note, transpose_chord, transpose_text

class TestTranspose(unittest.TestCase):
    def test_transpose_note_sharps(self):
        self.assertEqual(transpose_note('C', 1), 'Db')
        self.assertEqual(transpose_note('C#', 1), 'D')
        self.assertEqual(transpose_note('E', 1), 'F')
        self.assertEqual(transpose_note('B', 1), 'C')

    def test_transpose_note_flats(self):
        self.assertEqual(transpose_note('Db', 1), 'D')
        self.assertEqual(transpose_note('Eb', 1), 'E')
        self.assertEqual(transpose_note('Bb', 2), 'C')

    def test_transpose_chord_simple(self):
        self.assertEqual(transpose_chord('C', 2), 'D')
        self.assertEqual(transpose_chord('Am7', 1), 'Bbm7')
        self.assertEqual(transpose_chord('Gmaj7', 3), 'Bbmaj7')

    def test_transpose_chord_slash(self):
        # transpose_chord handles single chords. 
        # Slash chords are handled in transpose_text by splitting.
        self.assertEqual(transpose_chord('C', 1), 'Db')
        self.assertEqual(transpose_chord('G', 1), 'Ab')

    def test_transpose_text_song(self):
        song = "[C]Hello [G/B]World\n[Am7]Testing"
        expected = "[Db]Hello [Ab/C]World\n[Bbm7]Testing"
        self.assertEqual(transpose_text(song, 1), expected)

    def test_smart_notes(self):
        # Verify the SMART_NOTES mapping
        self.assertEqual(transpose_note('G', 1), 'Ab')
        self.assertEqual(transpose_note('G#', 1), 'A')

if __name__ == '__main__':
    unittest.main()
