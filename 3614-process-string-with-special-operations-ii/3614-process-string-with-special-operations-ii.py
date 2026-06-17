class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        length = 0

        for ch in s:
            if ch == '*':
                if length > 0:
                    length -= 1

            elif ch == '#':
                length *= 2

            elif ch == '%':
                pass

            else:
                length += 1

            lengths.append(length)

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            curr_len = lengths[i]

            if ch == '%':
                k = curr_len - 1 - k

            elif ch == '#':
                prev_len = curr_len // 2
                k %= prev_len

            elif ch == '*':
                pass

            else:
                prev_len = curr_len - 1

                if k == prev_len:
                    return ch

        return '.'