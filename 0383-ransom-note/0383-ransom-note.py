class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dic = Counter(ransomNote)
        magazine_dic = Counter(magazine)

        for letter in ransomNote:
            if ransomNote_dic[letter] > magazine_dic[letter]:
                return False
        
        return True