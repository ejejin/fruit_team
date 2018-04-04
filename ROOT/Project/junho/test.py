import sys
sys.path.append("../functions")
from D1H_rootHist_TXT_conversion import D1H_txt_to_roothist, D1H_roothist_to_txt

#D1H_txt_to_roothist("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/Height1_F.txt","")
D1H_txt_to_roothist("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/Height1_F.txt","~/Desktop")
D1H_roothist_to_txt("py-fillrandom.root","~/Desktop")


