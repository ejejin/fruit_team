#include <vector>
#include <stdio.h>
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"
#include "TLeaf.h"
#include <cstring>
#include <string.h>
#include "n2_root_tree_reader.h"
#include "n3_branch_reader.h"
#include "n4_leaf_reader.h"

void code_test()
{
    string str = "/Users/leejunho/Desktop/MG5_aMC_v2_6_1/bin/VBSww/Events/run_01/10M.root";
//    string str = "/Users/leejunho/Desktop/git/My_git/My_temp/n41_VBSWW_ExROOT/VBSWW_GEN_output.root";  
//    string str = "/Users/leejunho/Desktop/tensorflow/self_trees/self_tree_mem_EN90000_LN2_E5000_NN50_B500_adam_L1e-05_DR0.0.root";  

    n2_root_tree_reader *tree_reader = new n2_root_tree_reader();
    vector<TTree*> vtree;
    n3_branch_reader *branch_reader = new n3_branch_reader();
    vector<TBranch*> vbranch;
    n4_leaf_reader *leaf_reader = new n4_leaf_reader();
    vector<TLeaf*> vleaf;

    vtree = tree_reader->Read_tree(&str);
    int tree_size = vtree.size();  // make a tree vector
//    cout<<endl;
    for(int i1=0; i1<tree_size; i1++)
    {
        TTree* tree = new TTree();
        tree = vtree.at(i1);     // read in a tree 
        cout<<"============================================================="<<endl;
        cout<<"!! Name of the tree : "<<tree->GetName()<<endl;
        vbranch = branch_reader->Read_branch(tree);  //make a branch vector

        cout<<endl;    
        for(int i2=0; i2<vbranch.size(); i2++)
        {
            TBranch* branch = new TBranch();
            branch = vbranch.at(i2);  // read in a branch
            cout<<"    ! Name of the Branch/Leaf : "<<branch->GetName()<<endl;
            vleaf = leaf_reader->Read_leaf(branch);    // make a leaf vector
/*            
            if(vleaf.size()==0)
            {       //write here what you want to do on the single leaf, which is not contained in a branch
            }
            else 
            {
                for(int i3=0; i3<vleaf.size(); i3++)
                {    //write here what you want to do on the leaf, which is contained in a branch
                }
            }
*/
        }
        cout<<endl;
    }
}
