# Hi, here's your problem today. This problem was recently asked by AirBNB:
#
# Given a non-empty list of words, return the k most frequent words.
# The output should be sorted from highest to lowest frequency,
# and if two words have the same frequency,
# the word with lower alphabetical order comes first.
# Input will contain only lower-case letters.

# Input: ["daily", "interview", "pro", "pro",
# "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]


class Solution(object):

    def topKFrequent(self, words, k):
        dictionary = {}
        for word in words:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

        sort_dict = sorted([{"key": k, "value": v} for k, v in dictionary.items()],
                           reverse=True,
                           key=lambda x: x["value"])

        result = []
        for i in range(k):
            result.append(sort_dict[i]["key"])

        return result


if __name__ == '__main__':
    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
    k = 2
    print(Solution().topKFrequent(words, k))
    # ['pro', 'daily']
