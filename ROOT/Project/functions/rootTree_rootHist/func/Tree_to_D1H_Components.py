#Author : JUNHO LEE

def Tree_to_D1H_Components(filename):
    from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad
    import os
    import numpy
    from n1_read_file_name import read_file_name
    from n2_get_branch_list import get_branch_list_each_tree
    import collections
    
    FileNameList = read_file_name(filename)
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])
#    print(sorted(BranchListEachTree.items()[0][1]))
    print(BranchListEachTree)
#    print(BranchListEachTree.keys()[0])
#    print(len(BranchListEachTree))
#    print(BranchListEachTree.items())
#    print(BranchListEachTree.items()[1][1])
#    print(BranchListEachTree.keys()[1])
#    for i in range(len(BranchListEachTree)):     
    BranchListEachTree = {BranchListEachTree.keys()[0]:sorted(BranchListEachTree.items()[0][1])}
    print(BranchListEachTree)

    for i in range(len(BranchListEachTree)):
        print("compenets below :")
        print("The Tree name is : ",BranchListEachTree.keys()[i])
        for j in range(len(BranchListEachTree.values()[i])):
            print(j, "      it contains : ",j, BranchListEachTree.values()[i][j])
        print("")


def main():
#    filename = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/concrete_tree.root"
    filename = "../../../root_generator/tree/root2_tree.root"
    Tree_to_D1H_Components(filename) 

if __name__ =="__main__":
    main()

