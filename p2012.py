from sys import stdin

def solution(s):
    [f] = map(int, (s.split()))

    remainder = (4 * 60) - ((12 - f) * 45)

    if remainder >= 0:
        return "YES"
    return "NO"

if __name__ == "__main__":
    print(solution(stdin.read()))

