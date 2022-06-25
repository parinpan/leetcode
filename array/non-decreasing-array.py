# Leetcode: https://leetcode.com/problems/non-decreasing-array/

def checkPossibility(nums):
    l, r = 0, 1
    counter, nums_len = 0, len(nums)
    
    while r < len(nums) and counter <= 1:
        if nums[l] <= nums[r]:
            l += 1
            r += 1
            continue
            
        if l == 0 or r == nums_len - 1:
            pass
        elif nums[l - 1] <= nums[r]:
            nums[l] = nums[l - 1]
        elif nums[l] <= nums[r + 1]:
            nums[r] = nums[l]
        else:
            counter = 100 # considered as max number
        
        l += 1
        r += 1
        counter += 1
        
    return counter <= 1


if __name__ == '__main__':
    assert checkPossibility([4,2,3]) == True
    assert checkPossibility([4,2,1]) == False
    assert checkPossibility([1, 5, 4, 6]) == True
