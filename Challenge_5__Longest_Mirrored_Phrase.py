def longest_palindromic_substring():
    s = input()
    Max = ''
    for i in range(len(s)):
        # Checking while Centre is single character
        L = R = i
        while L>=0 and R < len(s) and s[L] == s[R]:
            if len(s[L: R+1]) >= len(Max):
                Max = s[L: R+1]
            L -= 1
            R += 1

        # Checking while Centre is two characters
        L = i
        R = i + 1
        while L>=0 and R < len(s) and s[L] == s[R]:
            if len(s[L: R+1]) >= len(Max):
                Max = s[L: R+1]
            L -= 1
            R += 1

    print(Max)

# Done!
longest_palindromic_substring()