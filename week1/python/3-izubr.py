def find_pointer_after_write_sum(chars, pos, summ):
    summ = str(summ)
    for i in range(len(summ)):
        chars[pos + i] = summ[i]
    return pos + len(summ) - 1
    
    
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append(None)
        n_same_char = 1
        prev_char = chars[0]
        write_pointer = 0
        for read_pointer in range(1, len(chars)):
            if chars[read_pointer] == chars[read_pointer - 1]:
                n_same_char += 1
            else:
                chars[write_pointer] = prev_char
                if n_same_char > 1:
                    write_pointer = find_pointer_after_write_sum(chars, write_pointer + 1, n_same_char)
                    n_same_char = 1
                write_pointer += 1
                prev_char = chars[read_pointer]
        chars = chars[:write_pointer]
        return len(chars)
