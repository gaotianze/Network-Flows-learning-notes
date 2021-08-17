# 基于个人理解的拓扑排序算法 20210520 TianzeGao
def topological_ordering(g):
    order=[]
    current_node = 0
    length=len(g[0])

    while len(order)<len(g):
        # 先找起始点
        for i in range(0,len(g)):
            if -1 not in g[i] and len(g[i])==length:
                current_node=i
                break

        if current_node not in order:
            order.append(current_node)

        for arc in range(0, length):  # 删除从start出发的弧
            if g[current_node][arc] == 1:
                for i in range(0,len(g)):
                    g[i][arc]=0

        g[current_node].append(0)
    print([i+1 for i in order])
    return 0


if __name__ == '__main__':
    G = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
         [-1, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, -1, -1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, -1, 0, -1, 1, -1, 0],
         [0, 0, 0, 0, -1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, -1, 0, -1]]
    topological_ordering(G)  # 输入G矩阵,输出的是当前点序下的拓扑排序
