"""
605. Can Place Flowers
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        """TO determine if flower pot can be planted in a list without breaking adjacent rule"""
        no_planted = 0
        for i in range(len(flowerbed)):
            print(i)
            #print(flowerbed[i])
            if flowerbed[i] == 0:
                previous = (i == 0 or flowerbed[i - 1] == 0 )
                after = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if previous and after:
                    no_planted += 1
                    flowerbed[i] = 1

                    if no_planted >= n:
                        return True

        return no_planted >= n

list = [1,0,0,0,1]
n = 1
solution = Solution()
ans = solution.canPlaceFlowers(list, n)
print(ans)