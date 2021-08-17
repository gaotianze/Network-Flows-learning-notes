# 基于个人理解的深度优先算法 20210520 TianzeGao
def search_depth_first(g, s):
    s -= 1
    marked_nodes = [s]
    node_list = [s]
    current_node=s
    while len(node_list) != 0:
        for arc in range(0, len(g[0])):
            if g[current_node][arc] == 1:
                g[current_node][arc] = 0
                for node in range(current_node + 1, len(g)):
                    if g[node][arc] == -1:
                        if node not in marked_nodes:
                            node_list.insert(0,node)
                            marked_nodes.append(node)
                            current_node = node_list[0]
                            break
        if 1 not in g[current_node]:
            node_list.remove(current_node)
            if len(node_list) != 0:
                current_node = node_list[0]

    print("可达点为：")
    print(sorted([i+1 for i in marked_nodes]))
    return 0


if __name__ == '__main__':
    G = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
         [-1, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, -1, -1, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, -1, 0, -1, 1, -1, 0],
         [0, 0, 0, 0, -1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, -1, 0, -1]]
    search_depth_first(G, 1)  # 输入G矩阵和几号点
