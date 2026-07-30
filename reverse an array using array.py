nums = [5, 7, 3, 2, 6, 1, 5, 9]

def func(nums, left, right):
    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)

func(nums, 1, 5)

print(nums)