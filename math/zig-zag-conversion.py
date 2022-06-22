# Leetcode: https://leetcode.com/problems/zigzag-conversion/

def convert(s, numRows):
    diff = numRows * 2 - 2
            
    if diff <= 0:
        return s

    answer = ""
    s_len = len(s)

    for r in range(0, numRows):
        suffix_idx = diff - (r * 2)
        
        for i in range(r, s_len, diff):
            answer += s[i]
            
            if i + suffix_idx < s_len and r != 0 and r != numRows - 1:
                answer += s[i + suffix_idx]

    return answer


if __name__ == '__main__':
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("ABCD", 3) == "ABDC"
    assert convert("A", 1) == "A"
