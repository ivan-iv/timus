import unittest
import p2012

class Test(unittest.TestCase):
    def test1(self):
        got = "7"
        expect = "YES"

        self.assertEqual(p2012.solution(got), expect)

    def test2(self):
        got = "5"
        expect = "NO"

        self.assertEqual(p2012.solution(got), expect)
