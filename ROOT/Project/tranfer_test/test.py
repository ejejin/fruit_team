from ROOT import gBenchmark
gBenchmark.Start("All in One")


import sys
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")

from Tree_to_D1H_Components import Tree_to_D1H_Components
Infile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/TestIn2_1.root"
Tree_to_D1H_Components(Infile)


from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(Infile,"./")
#print(NEW_Tree_PATH)


from Tree_to_D1H_Convert import CONVERT_WORKING
HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"./")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootHist_TXT/func")
from D1H_rootHist_TXT_conversion import D1H_roothist_to_txt
TXT_FILE_LIST =  D1H_roothist_to_txt(HistROOT_PATH, ".")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from c1_basic_statistic import *

for Input_file in TXT_FILE_LIST:
    print("The file Name is :",Input_file)
    MODE = most_frequent_bin(Input_file);      print("MODE :",MODE)
    DATA_RANGE = c1_data_range(Input_file);    print("DATA_RANGE :",DATA_RANGE)
    MEDIAN = c1_median(Input_file);            print("MEDIAN :",MEDIAN)
    Total_ENTRY = c1_total_ENTRY(Input_file);  print("Total_ENTRY :",Total_ENTRY)
    MEAN = c1_mean(Input_file);                print("MEAN :",MEAN)
    VARIANCE = c1_variance(Input_file);        print("VARIANCE :",VARIANCE)
    STD = c1_standard_deviation(Input_file);   print("STD :",STD)
    print("\n")


gBenchmark.Show("All in One")
