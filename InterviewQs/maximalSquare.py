def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    def get_sum_of_square(matrix, iM, iN, size):
        for m in range(size):
            for n in range(size):
                if iM==0 and iN==0 and size==4:
                    print(matrix[iN+n][iM+m])
                if matrix[iN+n][iM+m]=="0":
                    return -1
        print(size)
        return size**2

    m,n = len(matrix[0]), len(matrix)
    biggest_possible_square = min(m,n)
    while biggest_possible_square > 0:
        desired_sum = biggest_possible_square**2
        for iM in range(0,m-biggest_possible_square+1):
            for iN in range(0,n-biggest_possible_square+1):
                if get_sum_of_square(matrix, iM, iN, biggest_possible_square) == desired_sum:
                    return desired_sum
        biggest_possible_square -= 1
    return 0

matrx = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]

for line in matrx:
    print(line)
print(maximalSquare(matrx))
