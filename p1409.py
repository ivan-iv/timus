from sys import stdin

def solution(s):
    [x, y] = map(int, s.split())

    return "{0} {1}".format(y - 1, x - 1)

if __name__ == "__main__":
    print(solution(stdin.read()))
