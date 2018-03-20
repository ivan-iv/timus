from sys import stdin

def solution(s):
    [pass1, pass2] = map(int, s.split())

    if pass1 % 2 != 0 and pass2 % 2 == 0:
        return "no"

    return "yes"

if __name__ == "__main__":
    print(solution(stdin.read()))
