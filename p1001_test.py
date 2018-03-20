import unittest
import p1001

class Test(unittest.TestCase):
    def test1(self):
        got = (
            "1427  0\n"
            "876652098643267843\n"
            "5276538\n"
        )
        expect = (
            "2297.0716\n"
            "936297014.1164\n"
            "0.0000\n"
            "37.7757"
        )

        self.assertEqual(p1001.solution(got), expect)
