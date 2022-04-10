def find_first_duplicates(nums):
    num_set = set()
    no_duplicate = 0

    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])
    return no_duplicate
print(find_first_duplicates([1,2,3,2,1]))
