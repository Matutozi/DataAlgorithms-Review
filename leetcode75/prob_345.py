"""
345. Reverse Vowels of a String
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """TO determine if flower pot can be planted in a list without breaking adjacent rule"""
        no_planted = 0
        for i in range(len(flowerbed)):
            #print(i)
            if flowerbed[i]  == 0:
                previous = (i == 0 or flowerbed[i - 1] == 0 )
                after = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if previous and after:
                    no_planted += 1
                    flowerbed[i] = 1

                    if no_planted >= n:
                        return True

        return no_planted >= n
