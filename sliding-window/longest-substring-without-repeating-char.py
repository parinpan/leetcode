# Leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    l, r, res = 0, 0, 0
    counter = {}
    
    while l < len(s) and r < len(s):
        if s[r] in counter:
            counter = {}
            l += 1
            r = l
            
        res = max(res, r - l + 1)
        counter[s[r]] = 1
        r += 1
            
    return res


if __name__ == '__main__':
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("anviaj") == 5
