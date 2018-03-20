from sys import stdin

def solution(s):
    [n, a, b] = map(int, s.split())

    return a * b * n * 2

if __name__ == "__main__":
    print(solution(stdin.read()))

