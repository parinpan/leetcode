# Leetcode: https://leetcode.com/problems/rotate-array/

def rotate(nums, k):
    if len(nums) == 0 or len(nums) == 1 or k == 0:
        return

    window = len(nums) - (k % len(nums))

    for i, num in enumerate(nums[window:] + nums[:window]):
        nums[i] = num


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
