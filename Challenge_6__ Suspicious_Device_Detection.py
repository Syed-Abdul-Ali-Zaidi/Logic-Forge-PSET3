def repeatedNTimes():
    nums = input()
    nums = nums.split(' ')
    Nums = [int(i) for i in nums]
    seen = set()
    for i in Nums:
        if i in seen:
            print(i)
            return
        else:
            seen.add(i)

# # Done!
repeatedNTimes()