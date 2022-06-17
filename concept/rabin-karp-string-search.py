LETTER_SIZE = 26
LARGEST_PRIME = pow(2, 64) - 59


def char_to_num(char):
    return ord(char) - ord('A') + 1


def hash(s):
    hash_code = 0
    s_length = len(s)

    for i in range(0, s_length):
        hash_code += (char_to_num(s[i]) * pow(LETTER_SIZE, s_length - i - 1)) % LARGEST_PRIME

    return hash_code


def roll(previous_hash, previous_char, next_char, most_significant):
    hash_code = previous_hash - ((hash(previous_char) * most_significant) % LARGEST_PRIME) 
    hash_code = (hash_code * LETTER_SIZE) % LARGEST_PRIME
    return hash_code + hash(next_char)


def compare(s1, s2):
    return s1 == s2


def find(s, substr):
    if len(s) < len(substr):
        return False

    s_len = len(s)
    substr_len = len(substr)
    hash_code = hash(substr)

    l = 0
    current_hash = hash(s[:substr_len])
    most_significant = pow(LETTER_SIZE, substr_len - 1)

    while l <= s_len - substr_len:
        if current_hash == hash_code and compare(s[l:l+substr_len], substr):
            return True

        l = l + 1
        r = l + substr_len - 1

        if r >= s_len:
            break

        current_hash = roll(current_hash, s[l-1], s[r], most_significant)

    return False


if __name__ == '__main__':
    assert find("", "abc") == False
    assert find("abcd", "abce") == False
    assert find("RaBinKaRp", "rabinkarp") == False
    assert find("algorithmisgood:)", "good") == True
    assert find("weknowabcisagoodcompany", "abc") == True
