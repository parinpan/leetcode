# Leetcode: https://leetcode.com/problems/maximal-square/submissions/

def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    answer = 0
    dp = [0] * (m * n)
    
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == "0":
                continue

            dp[n * i + j] = 1

            if i > 0 and j > 0:
                top, bottom, diagonal = dp[n * (i - 1) + j], dp[n * i + j - 1], dp[n * (i - 1) + j - 1]
                dp[n * i + j] += min(top, bottom, diagonal)

            # answer = max square length
            answer = max(answer, dp[n * i + j])
    
    return answer * answer


if __name__ == '__main__':
    assert maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
    assert maximalSquare([["0","1"],["1","0"]]) == 1
    assert maximalSquare([["0"]]) == 0
