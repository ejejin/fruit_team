#Author : JUNHO LEE

def Tree_to_D1H_Components(filename):
    from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad
    import os
    import numpy
    from n1_read_file_name import read_file_name
    from n2_get_branch_list import get_branch_list_each_tree

    
    FileNameList = read_file_name(filename)
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])
#    print(BranchListEachTree)

    for i in range(len(BranchListEachTree)):
        print("compenets below :")
#        print(type(BranchListEachTree.keys()))
        print("The Tree name is : ",BranchListEachTree.keys()[i])
        for j in range(len(BranchListEachTree.values()[i])):
            print("        it contains : ", BranchListEachTree.values()[i][j])
        print("")


def main():
    filename = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root1_tree.root"
    Tree_to_D1H_Components(filename) 

if __name__ =="__main__":
    main()

