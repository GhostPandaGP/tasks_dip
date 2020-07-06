# Hi, here's your problem today. This problem was recently asked by Amazon:
#
# You are given an array of integers. Return the length of the longest
# consecutive elements sequence in the array.
#
# For example, the input array [100, 4, 200, 1, 3, 2] has the longest
# consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.


def longest_consecutive(nums):
    array = sorted(nums)

    max_len = 1
    tmp_len = 1
    last_number = array[0]
    for i in range(1, len(array)):
        if array[i] == last_number + 1:
            tmp_len += 1
        else:
            if max_len < tmp_len:
                max_len = tmp_len
            tmp_len = 1

        last_number = array[i]

    return max_len if max_len > tmp_len else tmp_len


if __name__ == '__main__':
    print(longest_consecutive([100, 4, 200, 1, 3, 2, 201, 202, 203]))
