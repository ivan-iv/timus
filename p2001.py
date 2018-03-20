from sys import stdin

def solution(s):
    a1, b1, _, b2, a3, _ = map(int, s.split())

    return "{} {}".format(a1 - a3, b1 - b2)

if __name__ == "__main__":
    print(solution(stdin.read()))

