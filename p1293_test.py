import unittest
import p1293

class Test(unittest.TestCase):
    def test1(self):
        got = "5 2 3"
        expect = 60

        self.assertEqual(p1293.solution(got), expect)
