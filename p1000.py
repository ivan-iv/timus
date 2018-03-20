from sys import stdin

def solution(s):
    [a, b] = map(int, s.split())

    return a + b

if __name__ == "__main__":
    print(solution(stdin.read()))
