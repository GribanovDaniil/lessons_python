class Solution:
    def countSquares(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))

#сложность O(n**2)
#алгоритм ищет сколько в исходной матрице, квадратных матриц, состоящих только из единиц.


