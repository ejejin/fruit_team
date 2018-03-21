#ifndef _BRANCH_FROM_TREE_H_
#define _BRANCH_FROM_TREE_H_

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"
#include "n3_read_branch_name.h"

class n3_branch_reader
{
    public:
        
        n3_branch_reader();
        vector<TBranch*> vbranch;
        vector<TBranch*> Read_branch(TTree *tree);
        TBranch* br = new TBranch();
//        void Reset();
};

n3_branch_reader::n3_branch_reader()
{
//    cout<<"!!branch from tree invoked!!"<<endl;
}

vector<TBranch*> n3_branch_reader::Read_branch(TTree *tree)
{
//    target = (TBranch*)tree->GetBranch("target_train");
//    output = (TBranch*)tree->GetBranch("output_train");
//    vbranch.push_back(target);
//    vbranch.push_back(output);
    n3_read_branch_name *Name = new n3_read_branch_name();
    vector<string> VName = Name->NameOfBranch(tree);
    vbranch.clear();
    for(int i1=0; i1<VName.size(); i1++)
    {
        cout<<"    ! branch name : "<<VName.at(i1)<<endl;
        const char* temp = VName.at(i1).data();
        br = (TBranch*)tree->GetBranch(temp);
        vbranch.push_back(br);
    }   
    cout<<endl<<"///////////////////////branches//////////////////////////"<<endl; 
    return vbranch;

}
/*
void n3_branch_reader::Reset()
{
    vbranch.clear();
    
}
*/
#endif

