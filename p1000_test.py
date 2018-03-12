import unittest
import p1000

class Test1000(unittest.TestCase):
    def test(self):
        self.assertEqual(p1000.add(1, 1), 2)
