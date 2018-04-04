from ROOT import gBenchmark
gBenchmark.Start("All in One")
import sys

sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rawTxt_Tree_root")
#Infile = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/concrete.txt"
#Infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BINANCE_DATA.txt"
Infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BBINA.txt"
#Infile = "soomin.txt"
from Raw_text_to_Tree_root import Raw_text_to_Tree_root
To_Tree = Raw_text_to_Tree_root(Infile,".")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")

from Tree_to_D1H_Components import Tree_to_D1H_Components
#To_Tree = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root"
Tree_to_D1H_Components(To_Tree)


from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(To_Tree,".")

from Tree_to_D2H_Convert import CONVERT_WORKING2D
from Tree_to_D1H_Convert import CONVERT_WORKING
HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"")
CONVERT_WORKING2D(NEW_Tree_PATH,"")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootHist_TXT/func")
from D1H_rootHist_TXT_conversion import D1H_roothist_to_txt
TXT_FILE_LIST =  D1H_roothist_to_txt(HistROOT_PATH, "")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from c1_basic_statistic import *
from c2_basic_histo_plotting import Basic_histo
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
    Basic_histo(Input_file)

gBenchmark.Show("All in One")
