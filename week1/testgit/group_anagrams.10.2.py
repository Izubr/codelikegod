from collections import defaultdict

def sorted_str(string):
    return ''.join(sorted(list(string)))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        key_sorted_strings = defaultdict(list)
        for string in strs:
            key_sorted_strings[sorted_str(string)].append(string)
        return key_sorted_strings.values()
