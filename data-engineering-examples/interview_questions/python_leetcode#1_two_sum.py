# Link to Leetcode problem#1: https://leetcode.com/problems/two-sum/

# Solution#1: Brute-Force
# space complexity: O(1)
# time complexity: O(n2)

def twoSum1(nums: list[int], target: int) -> list[int]:
    nums_length = len(nums)
    for first in range(nums_length-1):
        for second in range(first+1, nums_length):
            if target == nums[first] + nums[second]:
                return [first, second]           

# Solution#2: 
# space complexity: O(n)
# time complexity: O(n)

# Edge Cases:
#   1.  target is zero
#   2.  the numbers in the resultset could be negative
#   3.  target could be negative

def twoSum2(nums: list[int], target: int) -> list[int]:  
    nums_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_map:
            return [nums_map[diff], i]
        else:
            nums_map[nums[i]] = i

def main():
        print("towSum1 output: ", twoSum1(nums=[1, 4, 7, 9, 14, 3, 2], target=9))
        print("towSum2 output: ", twoSum2(nums=[1, 4, 7, 9, 14, 3, 2], target=9))
        
        print("\ntowSum1 output: ", twoSum1(nums=[3, 2, 4], target=6))
        print("towSum2 output: ", twoSum2(nums=[3, 2, 4], target=6))

        print("\ntowSum1 output: ", twoSum1(nums=[2,7,11,15], target=9))
        print("towSum2 output: ", twoSum2(nums=[2,7,11,15], target=9))

        print("\ntowSum1 output: ", twoSum1(nums=[3,3], target=6))
        print("towSum2 output: ", twoSum2(nums=[3,3], target=6))

        print("\ntowSum1 output: ", twoSum1(nums=[3,0,2,3,0,1], target=0))
        print("towSum2 output: ", twoSum2(nums=[3,0,2,3,0,1], target=0))

if __name__ == "__main__":
    main()
