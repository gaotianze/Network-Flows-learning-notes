# Dijkstra Algorithm - Dial's Implementation By TianzeGao 20210605
def dijkstra_dial(A):
    n = len(A)
    permanent = {1: 0}
    now_node = 1
    pre_len = 0
    permanent_list = [0]
    bucket_group=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] # 定义了9个桶
    exit=0

    while exit==0:
        print("第" + str(len(permanent)) + "轮")
        for i in range(0, n):  # 更新临时标号
            if A[now_node - 1][i] != 0 and A[now_node - 1][i] != 999 and i not in permanent_list:
                bucket_group[A[now_node - 1][i]+pre_len].append(i+1)
                for j in range(A[now_node - 1][i]+pre_len+1,len(bucket_group)): # 实现# min[d(i)+Cij, d(j)]
                    if i+1 in bucket_group[j]:
                        bucket_group[j].remove(i+1)
                        break
                for j in range(A[now_node - 1][i]+pre_len):
                    if i+1 in bucket_group[j]:
                        bucket_group[A[now_node - 1][i]+pre_len].remove(i+1)
                        break

        # 看现在是否所有桶均为空,否则记录第一个不为空的桶的编号
        sum=0
        for i in range(0,len(bucket_group)):
            if len(bucket_group[i])!=0 and sum==0:
                discover=i # discover就是当前最小路长的值，在这个桶里的就是要选择的永久标号点
            sum+=len(bucket_group[i])
        if sum==0:
            exit=1
        else:
            permanent_list.append(bucket_group[discover][0]-1)
            permanent[bucket_group[discover][0]]=discover
            now_node=bucket_group[discover][0]
            bucket_group[discover].pop(0)
            pre_len=discover
        if exit!=1:
            print("现在桶里有什么：" + str(bucket_group))
            print("已经在这个桶里取了一个点变成永久标号点：" + str(discover) + "号桶的——" +str(now_node)+"号点")
            print(permanent)
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
    '''A = [[0,2,4,999,999,999],
             [999,0,1,4,2,999],
             [999,999,0,999,3,999],
             [999,999,999,0,999,2],
             [999,999,999,3,0,2],
             [999,999,999,999,999,0]]'''  # 备用测试案例

    dijkstra_dial(A)
