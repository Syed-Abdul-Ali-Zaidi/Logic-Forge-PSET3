def longest_palindromic_substring(s):
    for i in range(len(s)):
        if len(s) % 2 == 0:
            L = i
            R = i + 1
        else:
            L = R = i
        max = ''
        while L>=0 and R < len(s) and s[L] == s[R]:
            max = s[L: R+1]
            L -= 1
            R += 1

    return max