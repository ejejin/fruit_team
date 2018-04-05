from ROOT import gSystem, gROOT
from ROOT import gBenchmark
gBenchmark.Start("All in One")
import sys
import os

sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rawTxt_Tree_root")
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")
Jinfile = ["../output_files/tea_0319Mon_LA_s_P_n_N.txt",]
for Infile in Jinfile:
    from Raw_text_to_Tree_root import Raw_text_to_Tree_root
    To_Tree = Raw_text_to_Tree_root(Infile,".")

#    from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
#    NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(To_Tree,".")
    NEW_Tree_PATH = To_Tree

    #from Tree_to_D2H_Convert import CONVERT_WORKING2D
    from Tree_to_D1H_Convert import CONVERT_WORKING
    HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"")
    #CONVERT_WORKING2D(NEW_Tree_PATH,"")


    sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootHist_TXT/func")
    from D1H_rootHist_TXT_conversion import D1H_roothist_to_txt
    TXT_FILE_LIST =  D1H_roothist_to_txt(HistROOT_PATH, "")

    sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
    from c1_basic_statistic import *
    from c3_Fit_Gaus_histo_plotting import Fit_Gaus_histo
    for Input_file in TXT_FILE_LIST:
        print("The file Name is :",Input_file)
        Fit_Gaus_histo(Input_file)

gBenchmark.Show("All in One")
