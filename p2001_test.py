import unittest
import p2001

class Test(unittest.TestCase):
    def test1(self):
        got = (
            "1 2\n"
            "2 1\n"
            "0 3"
        )
        expect = "1 1"

        self.assertEqual(p2001.solution(got), expect)
