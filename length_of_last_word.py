class Solution:
    def length_of_last_word(self, s: str) -> int:
        word_lst = s.split()
        return len(word_lst[-1])


if __name__ == "__main__":
    solution = Solution()
    print(solution.length_of_last_word("   fly me   to   the moon  "))
