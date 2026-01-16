def repeatedNTimes(nums : str):
    nums = nums.split(' ')
    Nums = [int(i) for i in nums]
    seen = set()
    for i in Nums:
        if i in seen:
            return i
        else:
            seen.add(i)

# # Done!
# n = '2 1 2 5 3 2'
# output =repeatedNTimes(n)
# print("Input:",n)
# print("Output:",output)