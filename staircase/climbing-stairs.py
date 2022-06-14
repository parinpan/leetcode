# Leetcode: https://leetcode.com/problems/climbing-stairs/submissions/

def climbStairs(n):
    step = [0, 1, 2] + ([0] * n)
    
    for i in range(3, n + 1):
        step[i] = step[i - 1] + step[i - 2]
    
    return step[n]


if __name__ == '__main__':
    assert climbStairs(45) == 1836311903
