# Label-correcting-dequeue Algorithm By TianzeGao 20210607
def label_correcting_dequeue(A):
    n = len(A)
    d_i = []
    pred = []
    for j in range(n):
        d_i.append(99)  # 初始化
        pred.append(0)
    d_i[0] = 0
    node_list=[0]
    node_list_history=[0]

    while len(node_list)!=0:
        i=node_list[0]
        node_list.pop(0)
        for j in range(n):
            if A[i][j] != 0 and A[i][j] != 999:
                if d_i[j] > A[i][j] + d_i[i]:
                    d_i[j] = A[i][j] + d_i[i]
                    pred[j]=i
                    if j in node_list_history:
                        node_list.insert(0,j)
                    else:
                        node_list.append(j)
                        node_list_history.append(j)
    print(d_i)

if __name__ == '__main__':
    # 以999代表∞
    A = [[0, 6, 4, 999, 999, 999],
         [999, 0, 2, 2, 999, 999],
         [999, 999, 0, 1, 2, 999],
         [999, 999, 999, 0, 999, 7],
         [999, 999, 999, 1, 0, 3],
         [999, 999, 999, 999, 999, 0]]

    '''A = [[0,1,2,999,999,999],
         [999,0,7,3,999,999],
         [999,999,0,999,5,999],
         [999,999,5,0,10,13],
         [999,999,999,999,0,4],
         [999,999,999,999,999,0]]  # 备用测试案例'''

    label_correcting_dequeue(A)
