def scrambled_keyword(s : str,p : str):
    substring_len = len(p)
    result = []

    # Counting frequency of every char of "p"
    freq_anum = {}
    for i in p:
        if i in freq_anum:
            freq_anum[i] += 1
        else:
            freq_anum[i] = 1

    for i in range(len(s) - substring_len+1):
        substr = s[i : i+substring_len]

        # Counting frequency of every char of "substr"
        freq_s = {}
        for j in substr:
            if j in freq_s:
                freq_s[j] += 1
            else:
                freq_s[j] = 1

        if freq_s == freq_anum:
            result += [i]

    return result

# Done!
# s = 'cbaebabacd'
# p = 'abc'
# output = scrambled_keyword(s,p)
# print("S:",s)
# print("P:",p)
# print("Output:",output)