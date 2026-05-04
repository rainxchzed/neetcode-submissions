class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        S, E = 0, len(matrix) - 1

        while S <= E:
            M = (S + E) // 2
            print(M)
            if matrix[M][len(matrix[M]) - 1] < target:
                S = M + 1
            elif matrix[M][len(matrix[M]) - 1] > target:
                E = M - 1

                print("Number in matrix exist")
                L, R = 0, len(matrix[M]) - 1

                while L <= R:
                    m = (L + R) // 2

                    if matrix[M][m] > target:
                        R = m - 1
                    elif matrix[M][m] < target:
                        L = m + 1
                    else:
                        return True
            else:
                return True
            
        return False

