class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            reverse_x = int("".join(reversed(list(str(x)))))
            if reverse_x >= pow(2, 31):
                return 0
            else:
                return reverse_x
        else:
            reverse_x = -int("".join(reversed(list(str(-x)))))
            if reverse_x < -pow(2,31):
                return 0
            else:
                return reverse_x