class Solution:
    def longest_common_prefix(self, strs):
        prefix = ""
        longest_word = max(strs, key=len)
        shortest_word = min(strs, key=len)
        for i, o in zip(longest_word, shortest_word):
            if i == o:
                prefix += i
            else:
                break
        return prefix


if __name__ == "__main__":
    solution = Solution()
    print(solution.longest_common_prefix(["hello", "hell", "hel"]))
