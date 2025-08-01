class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image            
solution = Solution()
print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))