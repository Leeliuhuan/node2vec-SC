graph文件夹----edgelist格式文件
emb文件夹-----produce_emd.py的输出
SCdata文件夹-----进行仿真实验的数据集

运行步骤：
1，将待处理数据放入graph文件夹中，如dolphins.edgelist；
2，将produce_emd.py以终端形式运行，如在终端处键入
       “python3 main.py --input graph/dolphins.edgelist --output emb/dolphins.emd --p 1 --q 1 --dimensions 128”
     运行结果自动保存到emb文件夹中，文件以.emd扩展名形式保存；
3， 将emd文件以.txt形式保存在SCdata/input中
4，运行main.py （注意代码的数据文件路径）