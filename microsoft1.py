class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome(node: Node):
    string = "" + node.val
    a = node
    while a.next:
        a = a.next
        string += a.val

    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next


if __name__ == '__main__':
    print(is_palindrome(node))
    # True
