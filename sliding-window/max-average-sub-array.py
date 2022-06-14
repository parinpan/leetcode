# Leetcode: https://leetcode.com/problems/maximum-average-subarray-i/

def findMaxAverage(nums, k):
    prevSum = sum(nums[0:k]) if len(nums) > 0 else 0
    maxAvg = prevSum / k

    for i in range(1, len(nums) - k + 1):
        prevSum = prevSum + nums[i+k-1] - nums[i-1]
        maxAvg = max(maxAvg, prevSum / k)

    return maxAvg
    
 
if __name__ == '__main__':
  assert findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
