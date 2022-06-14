# Leetcode: https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    def check_freq(window):
        for char in window:
            if window[char] != 0:
                return False

        return True

    l, r = 0, 0
    window = {}
    letters = {}

    for char in s1:
        letters[char] = True
        window[char] = window.get(char, 0) + 1

    while r < len(s1):
        window[s2[r]] = window.get(s2[r], 0) - 1
        r = r + 1

    while l < len(s2) and r < len(s2):
        if check_freq(window):
            return True

        window[s2[r]] = window.get(s2[r], 0) - 1

        if s2[r] in letters or window[s2[r]] < 1:
            window[s2[l]] = window.get(s2[l], 0) + 1
            l = l + 1
            r = r + 1

    return check_freq(window)

if __name__ == '__main__':
    assert checkInclusion("ab", "eidbaooo") == True
    assert checkInclusion("ab", "eidboaoo") == False
    assert checkInclusion("adc", "dcda") == True
