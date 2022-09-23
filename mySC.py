import networkx as nx
from sklearn.cluster import SpectralClustering
import pandas as pd
import numpy as np

def get_graph1(filename):
    """
        read common adjacency matrix data
        :param filename: filename
        :return: adjacency matrix
    """
    print(f'----------{filename}----------')
    M = pd.read_csv(filename, header=None, sep='\t')
    return np.array(M)

def get_graph21(filename):
    """
        read emd data
        :param filename: filename
        :return: matrix
    """
    print(f'----------{filename}----------')
    M = pd.read_csv(filename, header=None, sep='\t')
    M = pd.DataFrame((x.split(" ") for x in M[0])).drop(0)
    M = M.values.astype(float) 
    M = M[np.lexsort(M[:, ::-1].T)]  
    M = np.delete(M, 0, axis=1)

    return M

def outputToCluList(clusters, filename):
    """
        output cluster sets
        :param clusters: clusters
        :param filename: saved filename
        :return: txt file
    """
    clu_lists = [[]]
    for i in range(len(clusters)):
        clu_list = []
        clu_list.append(clusters[i])
        clu_lists.append(clu_list)
    # convert to txt
    df = pd.DataFrame(clu_lists).drop(index = 0)
    df.to_csv(filename + '-clu.txt', encoding='gbk', sep='\t', header = None, index=False, float_format='%.0f')

def mySC_main(inpath, outpath, datasets, clu):
    for i in range(len(clu)):
        if ("emd" in datasets[i]):
            data = get_graph21(inpath + datasets[i] + ".txt")
        else:
            data = get_graph1(inpath + datasets[i] + ".txt")

        sc = SpectralClustering(clu[i])

        res = [i + 1 for i in sc.fit_predict(data)]
        print(f"clustering:")
        print(res)
        outputToCluList(res, outpath + datasets[i])

if __name__ == "__main__":
    inpath = "SCdata/input/"
    outpath = "SCdata/output/"
    # datasets = ['dolphins', 'dolphins-emd', "football", 'football-emd', "karate", "karate-emd", "lesmis", "lesmis-emd", 'email', 'email-emd', "jazz", "jazz-emd", "polbooks", "polbooks-emd", "protein", "protein-emd"]
    # cul = [2, 2, 12, 12, 2, 2, 11, 11, 23, 23, 5, 5, 3, 3, 13, 13]

    datasets = ["lesmis", "lesmis-emd"]
    clu = [11, 11]
    mySC_main(inpath, outpath, datasets, clu)