import unittest
import main

class TestStringMethods(unittest.TestCase):

  def test_file_read(self):
    words = main.words_list()
    self.assertEqual(len(words), 1786)
    self.assertEqual(words[1], "ABILITY")

  def test_solution(self):
    self.assertEqual(main.solution(), 162)

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()