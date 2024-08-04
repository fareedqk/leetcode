class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        arr = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            arr.append(temp)
        return arr