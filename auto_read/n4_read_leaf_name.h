#ifndef _READ_LEAF_NAME_H_
#define _READ_LEAF_NAME_H_

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"
#include "TLeaf.h"

class n4_read_leaf_name
{
    public:
        n4_read_leaf_name();
        vector<string> NameOfLeaf(TBranch *branch);
        vector<string> Vstr;
};

n4_read_leaf_name::n4_read_leaf_name()
{
    
}

vector<string> n4_read_leaf_name::NameOfLeaf(TBranch *branch)
{
    TLeaf *leaf;
    TIter nextlf(branch->GetListOfBranches());
    while((leaf = (TLeaf*)nextlf()))
    {
        string leafname = leaf->GetName();
//        cout<<leafname<<endl;
        Vstr.push_back(leafname);
    }
    return Vstr;
    Vstr.clear();
}

#endif

















