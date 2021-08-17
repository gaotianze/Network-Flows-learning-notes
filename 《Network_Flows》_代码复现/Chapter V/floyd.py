# Floyd Algorithm By TianzeGao 20210608
def floyd(A):
    M = 999
    pred = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            if A[i][j] != 0 and A[i][j] != M:
                row.append(i)
            else:
                row.append(-1)
        pred.append(row)

    for k in range(len(A)):
        for j in range(len(A)):
            for i in range(len(A)):
                if A[i][j] > A[i][k] + A[k][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    pred[i][j] = pred[k][j]
    print(A)


if __name__ == '__main__':
    # 以999代表∞
    M = 999
    A = [[0, 12, M, M, M, 16, 14],
         [12, 0, 10, M, M, 7, M],
         [M, 10, 0, 3, 5, 6, M],
         [M, M, 3, 0, 4, M, M],
         [M, M, 5, 4, 0, 2, 8],
         [16, 7, 6, M, 2, 0, 9],
         [14, M, M, M, 8, 9, 0]]

    # 算例地址：https://blog.csdn.net/ytuyzh/article/details/88617987

    floyd(A)
