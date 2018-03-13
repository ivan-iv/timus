from sys import stdin
import math

def solution(s):
    numbers = reversed(list(map(int, s.split())))
    sqrts = ["{:.4f}".format(math.sqrt(x)) for x in numbers]
    
    return "\n".join(sqrts)

if __name__ == "__main__":
    print(solution(stdin.read()))
