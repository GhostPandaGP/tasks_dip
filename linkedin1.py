# Hi, here's your problem today. This problem was recently asked by LinkedIn:
#
# Given a string, rearrange the string so that no character next to each other are the same.
# If no such arrangement is possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca


def rearrangeString(s):

    dictionary = {}
    for c in s:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    array = [{'key': x[0], 'value': x[1]} for x in dictionary.items()]
    array = sorted(array, key=lambda x: x['value'], reverse=True)

    new_string = ""
    j1 = 0
    j2 = 1
    flag = True  # when is flag = True, use j1
    for i in range(len(s)):

        if j1 == len(array) and flag or j2 == len(array) and not flag:
            return False

        if flag:
            j = j1
            if array[j]['value'] == 1:
                j1 = max(j1, j2) + 1
        else:
            j = j2
            if array[j]['value'] == 1:
                j2 = max(j1, j2) + 1

        new_string += array[j]['key']
        array[j]['value'] -= 1
        flag = not flag
        print(new_string)

    return new_string


if __name__ == '__main__':
    print(rearrangeString('addddabbccc'))
    # cbcabc
