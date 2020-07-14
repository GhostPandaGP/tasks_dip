# Hi, here's your problem today. This problem was recently asked by Twitter:
#
# You are given the root of a binary tree. Find the level for the binary
# tree with the minimum sum, and return that value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10,
# and 4 + 1 + 2 = 7. So, the answer here should be 7.


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root):

    queue = [root]
    min_sum = root.val
    while queue:
        tmp = []
        tmp_min = 0
        for q in queue:
            tmp_min += q.val
            if q.left:
                tmp.append(q.left)
            if q.right:
                tmp.append(q.right)
        queue = tmp
        min_sum = min(tmp_min, min_sum)

    return min_sum


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)


if __name__ == '__main__':
    print(minimum_level_sum(node))
