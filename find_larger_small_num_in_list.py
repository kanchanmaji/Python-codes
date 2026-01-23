def find_largest_smallest(nums):
    largest = nums[0]   # start with first element
    smallest = nums[0]
    
    for num in nums:    # loop through each element
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    return largest, smallest  # return both

nums = [1, 2, 35, 4]
largest, smallest = find_largest_smallest(nums)
print("Largest:", largest)
print("Smallest:", smallest)