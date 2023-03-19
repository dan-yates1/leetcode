import re


class Solution:
    def number_different_integers(self, word: str) -> int:
        match = re.findall('\d+', word)
        match = map(int, match)
        return len(set(match))


if __name__ == "__main__":
    solution = Solution()
    print(solution.number_different_integers("gi851a851q8510v"))
