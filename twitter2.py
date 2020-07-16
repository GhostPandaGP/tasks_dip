# Hi, here's your problem today. This problem was recently asked by Twitter:
#
# Given an array of integers of size n, where all elements are between 1
# and n inclusive, find all of the elements of [1, n]
# that do not appear in the array. Some numbers may appear more than once.

# Input: [4,5,2,6,8,2,1,5]
# Output: [3,7]


class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        last_number = nums[0]
        result = []

        for i in range(1, len(nums)):

            if last_number == nums[i]:
                continue
            if last_number == nums[i] + 1:
                last_number += 1
            else:
                result.extend(range(last_number + 1, nums[i]))
                last_number = nums[i]

        if nums[i] < len(nums):
            result.extend(range(nums[i] + 1, len(nums) + 1))

        return result


if __name__ == '__main__':
    nums = [4, 6, 2, 6, 7, 2, 1, 1, 1]
    print(Solution().findDisappearedNumbers(nums))
    # [3, 5]
