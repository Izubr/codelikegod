import math

class Solution(object):
    def inc(bin_vect, pos, ones):
        while bin_vect[pos]:
            ones -= 1
            bin_vect[pos] = 0
            pos += 1
        bin_vect[pos] = 1
        return ones + 1
    
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        size = math.log(num)
        bin_vect = [0] * (size + 1)
        ones = 0
        result = []
        for i in range(num):
            result.append(inc(bin_vect, 0, ones))
        return result

