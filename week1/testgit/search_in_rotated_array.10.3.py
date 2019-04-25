def rotated_index(array, index, pivot):
    return (index + pivot) % len(array)

class RotatedArray(object):
    
    def __init__(self, array, pivot=0):
        self.array = array
        self.pivot = pivot
    
    def __getitem__(self, index):
        return self.array[rotated_index(self.array, index, self.pivot)]
    
    def __len__(self):
        return len(self.array)
    

def pivot_is_right(median_el, right_el):
    return median_el > right_el


def x_is_right_fabric(x):
    return lambda median_el, right_el: median_el < x


def bin_search(array, go_right):
    left, right = 0, len(array) - 1
    while left < right:
        medium = (left + right) // 2
        left, right = (medium + 1, right) if go_right(array[medium], array[right]) else (left, medium)
    return left


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = bin_search(nums, pivot_is_right)
        rotated_array = RotatedArray(nums, pivot)
        target_index = bin_search(rotated_array, x_is_right_fabric(target))
        print pivot, target_index
        return rotated_index(nums, target_index, pivot) if nums and rotated_array[target_index] == target else -1