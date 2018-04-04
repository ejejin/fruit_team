
from n1_read_file_name import read_file_name
from n2_get_branch_list import get_branch_list_all, get_branch_list_each_tree
from n3_set_branch_address import showcase_set_branch_address
from n4_set_histo_xrange import set_histo_xrange
from n5_set_histograms import set_histograms, test
import n55_set_histograms

#from nn_fill_histograms import fill_histograms

def main():

    FileNameList = read_file_name("../../../root_generator/tree/root2_tree.root")  # [filename ,filename.root, absolute path filename.root]
#print(FileNameList)

    BranchListAll = get_branch_list_all(FileNameList[2])   # set{b1,b2,b3, ....}
#print(BranchListAll)

    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])  #{'tree1': ['b1', 'b2', 'b3'...], 'tree2': ['b1', 'b4', 'b5...'],...}
#print(BranchListEachTree)

    DicNumpyArray_branch = showcase_set_branch_address(BranchListAll, FileNameList[2])  #  !!! This is just a showcase of SetBranchAddress, not really set !!! 
#print(DicNumpyArray_branch)                             # mess ordered, {'b3': array([ 0.]), 'b1': array([ 0.]), 'b2': array([ 0.])}

    histo_xrange = set_histo_xrange(FileNameList[2], BranchListAll)   #{'tree1': {'b3': [-1.8, 20.8], 'b1': [-5.1, 5.2], 'b2': [-0.0, 1.1]}, 'tree2': {'b3': [-3.4, 4.6], 'b1': [-4.4, 5.2], 'b2': [-0.0, 1.1]} ...}
#print(histo_xrange)


    DicHistList = set_histograms(FileNameList[2], FileNameList[0], histo_xrange)
    print("\n")
    print(DicHistList) 

#    AA = n55_set_histograms.SET_HIST()
#    AA1 = AA.set_histograms(FileNameList[2], FileNameList[0], histo_xrange)
#    print(AA1)


if __name__ == "__main__":
    main()




