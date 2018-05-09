#ifndef _N1_TREE_TO_VECTOR_H_
#define _N1_TREE_TO_VECTOR_H_

#include <iostream>
#include <string>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"

class n1_tree_to_vector
{
    public:
        n1_tree_to_vector();
        vector<vector<string>> Tree_to_vector(TTree *tree);
};

n1_tree_to_vector::n1_tree_to_vector()
{
}

vector<vector<string>> n1_tree_to_vector::Tree_to_vector(TTree *tree)
{
    vector<vector<string>> Tree_vector;
    vector<string> vbranch_name;
    vector<double> branch_event;
    vector<double> VECTOR_temp;
    vector<double*> vTT;
    TBranch *branch;
    Long64_t Entry_num = tree->GetEntries();
    TIter nextbr(tree->GetListOfBranches());
    while((branch = (TBranch*)nextbr()))
    {
        string branchname = branch->GetName();
        vbranch_name.push_back(branchname);
    } 
    Tree_vector.push_back(vbranch_name);

    for(int i=0; i<vbranch_name.size(); i++)
    {
        VECTOR_temp.push_back(0);
    }
//    cout<<VECTOR_temp.size();
    for(int i=0; i<vbranch_name.size(); i++)
    {
        double temp_double=0;
        tree->SetBranchAddress(vbranch_name.at(i).c_str(),&VECTOR_temp.at(i));
    }

    for(Long64_t i=0; i<Entry_num; i++)
    {
        tree->GetEntry(i);
        vector<string> branch_content;
        for(int j=0; j<VECTOR_temp.size(); j++)
        {
//            cout<<VECTOR_temp.at(j)<<endl;
            string branchE = to_string((VECTOR_temp.at(j)));
            branch_content.push_back(branchE);
        }
        Tree_vector.push_back(branch_content);
        branch_content.clear();
    }      
    branch_event.clear();
    VECTOR_temp.clear();
    vbranch_name.clear();
    vTT.clear();
    return Tree_vector;
}

#endif




