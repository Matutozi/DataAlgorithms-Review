class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #to write this code we need an helper function that finds the gcd
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a

        str1_len = len(str1)
        str2_len = len(str2)
        length_gcd = gcd(str1_len, str2_len)

        candidate = str1[:length_gcd]
        print(candidate)

        if candidate * (str1_len // length_gcd) == str1 and candidate * (str2_len // length_gcd)== str2:
            return candidate    
        else:
            return ""
        

solution = Solution()
ans = solution.gcdOfStrings("ABCABCABC", "ABC")
print(ans)