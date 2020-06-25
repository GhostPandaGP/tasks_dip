# Hi, here's your problem today. This problem was recently asked by Uber:
#
# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Note: be sure that pop() and top() handle being called on an empty stack.


class minStack(object):
    def __init__(self):
        self.elements = []
        self.min_elements = []
        self.length = 0

    def push(self, element):
        self.elements.append(element)

        if self.length == 0:
            self.min_elements.append(element)
        else:
            if element < self.min_elements[self.length - 1]:
                self.min_elements.append(element)
            else:
                self.min_elements.append(self.min_elements[self.length - 1])

        self.length += 1
        return True

    def pop(self):

        if self.length == 0:
            return False

        a = self.elements[self.length - 1]
        del self.elements[self.length - 1]
        del self.min_elements[self.length - 1]
        self.length -= 1
        return a

    def top(self):
        return self.elements[self.length - 1] if self.length > 0 else False

    def get_min(self):
        return self.min_elements[self.length - 1] if self.length > 0 else False


if __name__ == '__main__':
    x = minStack()
    x.push(-2)
    x.push(0)
    x.push(-3)
    print(x.get_min())
    # -3
    x.pop()
    print(x.top())
    # 0
    print(x.get_min())
    # -2