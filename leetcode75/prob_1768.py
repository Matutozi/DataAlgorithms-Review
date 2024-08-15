class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        merged_word = ""
        #find the shorter of the two lengths
        min_word = min(word1_len, word2_len)
        for i in range(min_word):
            merged_word += word1[i]
            merged_word += word2[i]

        
        if word1_len > word2_len:
            merged_word += word1[min_word::]
        elif word2_len > word1_len:
            merged_word += word2[min_word::]

        return merged_word
    


def merge(word1, word2):
    merged= ""
    for i in range(max(len(word1), len(word2))):
        
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
    return merged


ans = (merge("abc", "cdfuhiihe"))
print(ans)