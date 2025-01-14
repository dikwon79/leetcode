class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        odd = 0
        for c,val in count.items():
            ans+=val//2
            odd = odd or val%2
        return ans*2 + odd

        