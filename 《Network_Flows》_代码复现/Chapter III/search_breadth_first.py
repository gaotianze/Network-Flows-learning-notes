# 基于个人理解的广度优先算法 20210520 TianzeGao
def search_breadth_first(g, s):
    s -= 1
    marked_nodes = [s]
    node_list = [s]
    while len(node_list) != 0:
        current_node = node_list[0]
        for arc in range(0, len(g[0])):  # 从current_node开始遍历它的所有arc，如有为1的，则查找其与谁相连.
            if g[current_node][arc] == 1:
                for node in range(current_node + 1, len(g)):  # 从找到1的行开始，往下遍历，找出所有-1，mark，并加入List
                    if g[node][arc] == -1:
                        if node not in marked_nodes:
                            node_list.append(node)
                            marked_nodes.append(node)
        node_list.remove(current_node)

    print("可达点为：")
    print([i+1 for i in marked_nodes])
    return 0


if __name__ == '__main__':
    G = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
         [-1, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, -1, -1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, -1, 0, -1, 1, -1, 0],
         [0, 0, 0, 0, -1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, -1, 0, -1]]
    search_breadth_first(G, 1)  # 输入G矩阵和几号点
