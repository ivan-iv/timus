import unittest
import p1877

class Test(unittest.TestCase):
    def test1(self):
        got = (
            "0001\n"
            "0000"
        )
        expect = "no"

        self.assertEqual(p1877.solution(got), expect)

    def test2(self):
        got = (
            "0002\n"
            "0001"
        )
        expect = "yes"

        self.assertEqual(p1877.solution(got), expect)
