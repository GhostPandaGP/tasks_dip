# Hi, here's your problem today. This problem was recently asked by Facebook:
#
# Starting at index 0, for an element n at index i, you are allowed to jump
# at most n indexes ahead. Given a list of numbers, find the minimum number
# of jumps to reach the end of the list.


def jumpToEnd(nums):
    result = 0
    step = 0
    while step < len(nums):
        currency = nums[step]
        result += 1

        if currency + step + 1 >= len(nums):
            return result

        i = currency - 1
        tmp_max = -1
        for e in range(step + 1, currency + step + 1):
            number = nums[e] - i
            if tmp_max < number:
                tmp_max = number
                step = e
            i -= 1

    return result


print(f"result: {jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])}")
# 2
