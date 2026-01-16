def longest_palindromic_substring(s):
    max = ''
    for i in range(len(s)):
        if len(s) % 2 == 0:
            L = i
            R = i + 1
        else:
            L = R = i

        while L>=0 and R < len(s) and s[L] == s[R]:
            if len(s[L: R+1]) >= len(max):
                max = s[L: R+1]
                print('max:',i,max)
            L -= 1
            R += 1

    return max