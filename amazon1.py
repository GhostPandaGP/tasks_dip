# Hi, here's your problem today. This problem was recently asked by Amazon:
#
# The h-index is a metric that attempts to measure the productivity and citation
# impact of the publication of a scholar. The definition of the h-index is
# if a scholar has at least h of their papers cited h times.


def hIndex(publications):

    # arr = [0, 0, 0, 0, 0, 0]

    arr = []
    for publication in publications:
        for i in range(publication + 1):

            if len(arr) <= i:
                arr.extend([0] * (i - len(arr) + 1))

            arr[i] += 1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= i:
            return i


print(hIndex([5, 3, 3, 1, 0]))
print(hIndex([3, 5, 0, 1, 3]))
print(hIndex([3, 5, 0, 1, 3, 3, 5, 0, 1, 3, 3, 5, 0, 1, 3, 3, 5, 0, 1, 3]))
# 3
