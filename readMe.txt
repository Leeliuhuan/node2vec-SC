graph folder ----edgelist file
emd folder -----the output of produce_emd.py
SCdata folder ----- data set for simulation experiments

Running steps.
1, put the data to be processed into the graph folder, such as dolphins.edgelist.
2, run produce_emd.py through a terminal, e.g. for example
       "python3 main.py --input graph/dolphins.edgelist --output emb/dolphins.emd --p 1 --q 1 --dimensions 128"
   The results of the run will be automatically saved to the emd folder with the file extension .emd.
3, save the emd file in .txt format to SCdata/input
4, run main.py (note the data file path of the code)
