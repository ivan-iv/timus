import unittest
import p1409

class Test(unittest.TestCase):
    def test1(self):
        got = '4 7'
        expect = '6 3'
        self.assertEqual(p1409.solution(got), expect)
