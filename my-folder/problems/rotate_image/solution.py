class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # l, r = 0, len(matrix) - 1
        # while l < r:
        #     for i in range(r - l):
        #         top, bottom = l, r
        #         # use temp variable (top left)
        #         top_left = matrix[top][l + i]

        #         # move bottom left into top left
        #         matrix[top][l + i] = matrix[bottom - i][l]

        #         # move top right into bottom left
        #         matrix[bottom - i][l] = matrix[bottom][r - i]
                
        #         #move top left into bottom right
        #         matrix[bottom][r - i] = matrix[top + i][r]

        #         # move temp variable (top left) into top right 
        #         matrix[top + i][r] = top_left
        #     l += 1
        #     r -= 1


        n = len(matrix)
        for i in range(n) :
            for j in range(i,n) :
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n) :
           matrix[i].reverse()