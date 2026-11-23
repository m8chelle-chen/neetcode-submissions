class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        while i < len(flowerbed):
            if(flowerbed[i] == 1):
                print(i, "no")
                i += 2
            elif (i == len(flowerbed) - 1 and flowerbed[i - 1] != 1) or (flowerbed[i + 1] != 1):
                print(i, "yes")
                count += 1
                i += 2
            else:
                print(i, "noo")
                if flowerbed[i + 1] == 1:
                    i += 3
                else:
                    i += 2

        return count >= n
        