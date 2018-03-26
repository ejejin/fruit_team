
import sys
sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func")

from Tree_to_D1H_Components import Tree_to_D1H_Components
Infile = "../root2_tree.root"
Tree_to_D1H_Components(Infile)

from Tree_to_D1H_CutnGenerate import REGENERATE_TREE_WITH_CUT
NEW_Tree_PATH = REGENERATE_TREE_WITH_CUT(Infile,"./")

from Tree_to_D1H_Convert import CONVERT_WORKING
HistROOT_PATH = CONVERT_WORKING(NEW_Tree_PATH,"./")


sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootHist_TXT/func")
from D1H_rootHist_TXT_conversion import D1H_roothist_to_txt
D1H_roothist_to_txt("root2_tree_cut_tree_hist.root", ".")

