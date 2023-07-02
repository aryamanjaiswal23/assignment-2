def has_duplicates(nums):
    return len(nums) != len(set(nums))


print(has_duplicates([1, 2, 3, 4, 2, 3, 6, 4]))
