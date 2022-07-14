def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        
        nums[j + 1] = key

    return nums


if __name__ == '__main__':
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([3, 3, 2, 2, 1, 1, 0, -1, 10]) == [-1, 0, 1, 1, 2, 2, 3, 3, 10]
