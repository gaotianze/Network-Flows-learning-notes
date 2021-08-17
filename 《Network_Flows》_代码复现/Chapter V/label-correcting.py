# Label-correcting Algorithm By TianzeGao 20210605
def label_correcting(A):
    n = len(A)
    d_i = []
    pred = []
    for j in range(n):
        d_i.append(99)  # 初始化
        pred.append(0)
    d_i[0] = 0

    # 遍历所有弧的思路：从头开始A矩阵中所有不为0也不为M的值，就是弧，对其验证 min[d(i)+Cij, d(j)] (此处仅执行了一个轮回)
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0 and A[i][j] != 999:
                if d_i[j] > A[i][j] + d_i[i]:
                    d_i[j] = A[i][j] + d_i[i]
                    pred[j]=i
    print(d_i)

if __name__ == '__main__':
    # 以999代表∞
    A = [[0, 6, 4, 999, 999, 999],
         [999, 0, 2, 2, 999, 999],
         [999, 999, 0, 1, 2, 999],
         [999, 999, 999, 0, 999, 7],
         [999, 999, 999, 1, 0, 3],
         [999, 999, 999, 999, 999, 0]]

    A = [[0,1,2,999,999,999],
         [999,0,7,3,999,999],
         [999,999,0,999,5,999],
         [999,999,5,0,10,13],
         [999,999,999,999,0,4],
         [999,999,999,999,999,0]]  # 备用测试案例

    label_correcting(A)
