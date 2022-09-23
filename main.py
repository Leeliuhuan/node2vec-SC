import mySC
import evaluate
import pandas as pd
import numpy as np

if __name__ == "__main__":
    inpath = "SCdata/"
    outpath = "SCdata/output/"
    # datasets = ['dolphins', 'dolphins-emd', "football", 'football-emd', "karate", "karate-emd", "lesmis", "lesmis-emd", 'email', 'email-emd', "jazz", "jazz-emd", "polbooks", "polbooks-emd", "protein", "protein-emd"]
    # cul = [2, 2, 12, 12, 2, 2, 11, 11, 23, 23, 5, 5, 3, 3, 13, 13]

    datasets = ['dolphins', 'dolphins-emd']
    clu = [2, 2]

    print(f'--------------clustering--------------')
    mySC.mySC_main(inpath+'/input/', outpath, datasets, clu)
    print(f'--------------evaluation--------------')
    evaluate.evaluate_main(inpath, datasets)