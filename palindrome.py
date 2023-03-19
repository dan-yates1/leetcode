class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        print(reverse)
        if (int(reverse) == x and x > 0):
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(102))