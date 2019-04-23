class Solution(object):
        def rotate_coord(self, x, y, size):
            return y, size - 1 - x

        def rotate(self, matrix):
            size = len(matrix)
            for i in range(size // 2):
                for j in range((size + 1) // 2):
                    prev_coord = matrix[i][j]
                    i_new, j_new = i, j
                    for _ in range(4):
                        i_new, j_new = self.rotate_coord(i_new, j_new, size)
                        prev_coord, matrix[i_new][j_new] = matrix[i_new][j_new], prev_coord
            return matrix
