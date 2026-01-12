def repeatedNTimes(nums: list):
    seen = set()
    for i in nums:
        if i in seen:
            return i
        else:
            seen.add(i)


