"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times.
So for example, 3[abc] should be expanded to abcabcabc.
Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.
"""
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
brackets = {
    'start': '[',
    'end': ']',
}

def decodeString(s):
    tmp_ass = []
    result = ""
    i = 0
    while i != len(s):
        l = s[i]
        if l in numbers:
            tmp_ass.append({
                "number": int(l),
                "string": '',
            })
            i += 1
        elif l == brackets['end']:
            index_le = len(tmp_ass) - 1

            if index_le == 0:
                result += tmp_ass[index_le]['string'] * tmp_ass[index_le]['number']
            else:
                tmp_ass[index_le - 1]['string'] += tmp_ass[index_le]['string'] * tmp_ass[index_le]['number']

            del tmp_ass[index_le]
        else:
            tmp_ass[len(tmp_ass) - 1]['string'] += l
        i += 1

    return result

print(decodeString('2[a2[b]c]'))
# abbcabbc