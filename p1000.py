from sys import stdin

def add(a, b):
    return a + b

if __name__ == '__main__':
    [a, b] = map(int, stdin.read().split())

    print(add(a, b))
