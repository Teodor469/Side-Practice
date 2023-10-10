def find_missing_number(nums):
    #find the missing number in an array
    n = len(nums)
    expected_sum = (n* (n + 1)) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number