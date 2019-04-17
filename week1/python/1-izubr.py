class Solution(object):
    def permute(self, nums):
        def rec_permutation(result, left_set):
            if not left_set:
                return [result]
            lists = []
            for el in left_set:
                lists = lists + rec_permutation(result + [el], left_set - set([el]))
            return lists
        return rec_permutation([], set(nums))
