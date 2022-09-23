import pandas as pd
from sklearn import metrics
from collections import OrderedDict
import networkx as nx

'''
每次运行都要包括三个文件：
dolpins.txt         数据的邻接矩阵。以'\t'为分隔符。
dolpins_stan.txt    标准结果。列向量的形式。每一行都是一个节点的标准划分。
predicted.txt       算法聚类结果。列向量的形式。每一行都是一个节点的聚类结果。
'''


def Q(comm, graph, weight='weight'):
    partition = {}
    if graph.has_node(0):
        for i in range(len(comm)):
            partition[i] = comm[i]
    else:
        for i in range(1, len(comm) + 1):
            partition[i] = comm[i - 1]

    if type(graph) != nx.Graph:
        raise TypeError("Bad graph type, use only non directed graph")

    inc = dict([])
    deg = dict([])
    links = graph.size(weight=weight)
    if links == 0:
        raise ValueError("A graph without link has an undefined modularity")

    for node in graph:
        com = partition[node]
        deg[com] = deg.get(com, 0.) + graph.degree(node, weight=weight)
        for neighbor, datas in graph[node].items():
            edge_weight = datas.get(weight, 1)
            if partition[neighbor] == com:
                if neighbor == node:
                    inc[com] = inc.get(com, 0.) + float(edge_weight)
                else:
                    inc[com] = inc.get(com, 0.) + float(edge_weight) / 2.

    res = 0.
    for com in set(partition.values()):
        res += (inc.get(com, 0.) / links) - \
               (deg.get(com, 0.) / (2. * links)) ** 2
    return res


def convert(dataset):
    data = pd.read_csv(dataset, header=None, sep='\t')
    l = data.shape[0]   
    truth = [data[0][i] for i in range(l)]   
    return truth


def networkG(W):
    G = nx.from_numpy_matrix(W)
    return G

def cut_clu(data):
    data = pd.read_csv(data, header=None, sep='\t').values
    data = [data[i][0] for i in range(len(data))]
    return data


def evaluate(truth, predicted, G):
    res = OrderedDict()  
    NMI = metrics.normalized_mutual_info_score(truth, predicted)
    Modularity = Q(predicted, G)
    FMI = metrics.fowlkes_mallows_score(truth, predicted)
    ARI = metrics.adjusted_rand_score(truth, predicted)
    AMI = metrics.adjusted_mutual_info_score(truth, predicted)
    res["NMI"] = NMI
    res["Modularity"] = Modularity
    res["FMI"] = FMI
    res["ARI"] = ARI
    res["AMI"] = AMI
    return res

def evaluate_main(path, datasets):
    print("index", "NMI", "Modularity", "FMI", "ARI", "AMI", sep='\t\t')
    print()
    for dataset in datasets:
        print()
        if ('emd' in dataset):
            W = pd.read_csv(path + 'input/' + dataset[0:-4] + ".txt", header=None, sep='\t').values
            predicted = cut_clu(path + 'output/' + dataset + "-clu.txt")
        else:
            W = pd.read_csv(path + 'input/' + dataset + ".txt", header=None, sep='\t').values
            predicted = cut_clu(path + 'output/' + dataset + "-clu.txt")

        # print(f'--------------evaluation--------------')
        G = networkG(W)
        print(dataset, end='\t')
        if (dataset in ['email', 'email-emd', 'jazz', 'jazz-emd', 'polbooks', 'polbooks-emd', 'protein', 'protein-emd']):
            res = Q(predicted, G)
            print(res)
            print()
        else:
            if ('emd' in dataset):
               truth = convert(path + 'input/' + dataset[0:-4] + "_stan.txt")
            else:
              truth = convert(path + 'input/' + dataset + "_stan.txt")
            res = evaluate(truth, predicted, G)
            for k, v in res.items():
                print(v, end='\t')

if __name__ == "__main__":
    path = 'SCdata/'

    # datasets = ['dolphins', 'dolphins-emd','football', 'football-emd', 'karate', 'karate-emd', 'lesmis', 'lesmis-emd', 'email', 'email-emd', "jazz", 'jazz-emd', "polbooks", 'polbooks-emd', "protein", 'protein-emd']
    datasets = ['lesmis']
    evaluate_main(path, datasets)




