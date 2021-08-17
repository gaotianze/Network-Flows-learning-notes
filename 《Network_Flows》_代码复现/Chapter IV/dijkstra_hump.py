# Dijkstra-Hump Algorithm By TianzeGao 20210605
def dijkstra_hump(A):
    n = len(A)
    permanent = {1: 0}
    d_i = {}  # 用字典存储标号--i:d(i)
    now_node = 1
    pre_len = 0
    permanent_list = [0]

    while len(permanent) != 6:
        print("第" + str(len(permanent)) + "轮")
        for i in range(0, n):  # 更新临时标号
            if A[now_node - 1][i] != 0 and A[now_node - 1][i] != 999 and i not in permanent_list:
                if i + 1 in d_i.keys():
                    d_i[i + 1] = min(A[now_node - 1][i] + pre_len, d_i[i + 1])  # min[d(i)+Cij, d(j)]
                else:
                    d_i[i + 1] = A[now_node - 1][i] + pre_len
        print("现存所有临时标号：" + str(d_i))

        # 此处相当于一个Hump，能自动找出最小值
        now_node=min(d_i, key=d_i.get)
        min_value=d_i[now_node]
        print("最小临时标号为：" + str(min_value) + "；所以新增永久标号点" + str(now_node))

        permanent[now_node] = min_value
        d_i.pop(now_node)
        pre_len = min_value
        permanent_list.append(now_node - 1)
        print("现存所有永久标号：" + str(permanent) + "\n")
    print("###结束###")


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
         [999,999,999,999,999,0]]'''  # 备用测试案例

    dijkstra_hump(A)
