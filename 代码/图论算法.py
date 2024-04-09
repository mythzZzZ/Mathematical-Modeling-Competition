
# # 图的代码基础

# import  networkx as nx
# import matplotlib.pyplot as plt

# #造图
# nf = nx.Graph()
# #添加节点
# nf.add_node('JFK')
# nf.add_nodes_from(['SFO','LAX','ATL','FLO','DFW','HNL'])

# #添加连线
# nf.add_edges_from([('JFK','SFO'),('JFK','LAX'),('LAX','ATL'),('FLO','ATL'),
#                    ('ATL','JFK'),('FLO','JFK'),('DFW','HNL'),('OKC','DFW'),
#                    ('OGG','DFW'),('OGG','LAX')])

# print(nf.number_of_edges()) #查看连线数


# #绘制网络图
# nx.draw(nf,with_labels = True)
# plt.show()

# print(nx.info(nf))                  #返回基本信息
# print(nx.density(nf))               #返回图的密度
# print(nx.diameter(nf))              #返回图的直径，直径是最大的偏心率
# print(nx.clustering(nf))            #计算节点的聚类系数  
# print(nx.transitivity(nf))          #计算图的传递性
# print(list(nf.neighbors('OGG')))    #计算节点的邻居
# print(nx.degree_centrality(nf))     #计算节点的度中心性
# print(nx.closeness_centrality(nf))  #计算节点的紧密度中心性
# print(nx.betweenness_centrality(nf))#计算节点的最短路径介数中心性


###########################################################################
# 图的最短路径
# import networkx as nx

# G = nx.Graph()
# G.add_edge('A','B',weight = 4)
# G.add_edge('B','D',weight = 2)
# G.add_edge('A','C',weight = 3)
# G.add_edge('C','D',weight = 5)
# G.add_edge('A','D',weight = 6)
# G.add_edge('C','F',weight = 7)
# G.add_edge('A','G',weight = 1)
# G.add_edge('H','B',weight = 2)

# # 改变图的布局
# pos = nx.spring_layout(G)

# #生成图的邻接矩阵
# mat = nx.to_numpy_matrix(G)
# print(mat)

# #计算图之间的最短路径 dijkstra_path
# path = nx.dijkstra_path(G,source='H',target='F')
# print('H->F 最短路径:',path)
# #计算最短距离
# distance = nx.dijkstra_path_length(G,source='H',target='F')
# print('H->F 最短距离:',distance)


# #图中一点到所有点的最短路径
# path = nx.shortest_path(G,source='H')
# #图中一点到所有点最短的距离
# d = nx.shortest_path_length(G,source='H')
# for node in G.nodes():
#     print("H到%s的最短路径为:%s" % (node,path[node]))
#     print(f"H到{node}的最短距离为:{d[node]}")


# #图中所有点到一点的路径
# path = nx.shortest_path(G,target='H')
# #图中所有点到一点的距离
# d = nx.shortest_path_length(G,target='H')
# for node in G.nodes():
#     print("%s到H的最短路径为:%s" % (node,path[node]))
#     print(f"{node}到H的最短距离为:{d[node]}")


# # 任意两点间最短的距离
# p = nx.shortest_path_length(G)
# p = dict(p)
# print(p)


# #最小生成树
# T = nx.minimum_spanning_tree(G)
# print(sorted(T.edges(data=True)))



###########################################################################
# # 图的最小花费最大流
# # 有向图
# import networkx as nx
# import matplotlib.pylab as plt
# G = nx.DiGraph() #构造有向图
# # 构造图
# G.add_edges_from([
#     ('s','v1',{'capacity':8,'weight':2}),
#     ('s','v3',{'capacity':7,'weight':8}),
#     ('v1','v3',{'capacity':5,'weight':5}),
#     ('v1','v2',{'capacity':9,'weight':2}),
#     ('v3','v4',{'capacity':9,'weight':3}),
#     ('v2','v3',{'capacity':2,'weight':1}),
#     ('v4','t',{'capacity':10,'weight':7}),
#     ('v2','t',{'capacity':5,'weight':6}),
#     ('v4','v2',{'capacity':6,'weight':4})
# ])
# # 力导向布局算法默认分配的位置
# pos = nx.spring_layout(G)
# # 调整节点的位置 它将节点 't' 的 x 坐标设置为 1，y 坐标设置为 0 满足可视化的需求
# pos['t'][0] = 1;pos['t'][1] = 0
# pos['s'][0] = -1;pos['s'][1] = 0
# pos['v1'][0] = -0.33;pos['v1'][1] = 1
# pos['v3'][0] = -0.33;pos['v3'][1] = -1
# pos['v2'][0] = 0.33;pos['v2'][1] = 1
# pos['v4'][0] = 0.33;pos['v4'][1] = -1


# #获取节点的capacity 返回一个字典
# edge_label1 = nx.get_edge_attributes(G,'capacity')
# print(edge_label1)
# #获取节点的weight 
# edge_label2 = nx.get_edge_attributes(G,'weight')
# edge_label = {}
# #遍历key  key为('s', 'v1').....
# for i in edge_label1.keys():
#     #把两个属性拼在一起
#     edge_label[i] = f'(C:{edge_label1[i]},w:{edge_label2[i]})'
# print(edge_label)


# #显示图像


# nx.draw_networkx(G,pos,with_labels=True,font_size=15) #画基本图像
# nx.draw_networkx_edge_labels(G,pos,edge_label,font_size=15) #在图像中添加权重

# #计算每两个个节点的最小费用最大流
# mincostFlow = nx.max_flow_min_cost(G,'s','t')
# print(mincostFlow)

# #最小费用的值
# mincost = nx.cost_of_flow(G,mincostFlow)

# #把节点的最小费用最大流存入到图的label里面
# for i in mincostFlow.keys():
#     for j in mincostFlow[i].keys():
#         edge_label[(i,j)] += ',F = '+str(mincostFlow[i][j])

# nx.draw_networkx(G,pos,with_labels=True,font_size=15) #画基本图像
# nx.draw_networkx_edge_labels(G,pos,edge_label,font_size=15) #在图像中添加权重

# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()





