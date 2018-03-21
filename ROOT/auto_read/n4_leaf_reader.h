#ifndef _LEAF_READER_H_
#define _LEAF_READER_H_

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "TBranch.h"
#include "TLeaf.h"
#include "n4_read_leaf_name.h"

class n4_leaf_reader
{
    public:
        n4_leaf_reader();
        vector<TLeaf*> vleaf;
        vector<TLeaf*> Read_leaf(TBranch *branch);
        TLeaf *lf = new TLeaf();
};

n4_leaf_reader::n4_leaf_reader()
{

}

vector<TLeaf*> n4_leaf_reader::Read_leaf(TBranch *branch)
{
    n4_read_leaf_name *Name = new n4_read_leaf_name();
    vector<string> VName = Name->NameOfLeaf(branch);
    if(VName.size() == 0) cout<<"    .. Itself is a leaf .."<<endl;
    else cout<<"    .. Has "<<VName.size()<<" leaves"<<endl;
    vleaf.clear();
    for(int i1=0; i1<VName.size();i1++)
    {
        cout<<"        leaf name : "<<VName.at(i1)<<endl;
        const char* temp = VName.at(i1).data();
        lf = (TLeaf*)branch->GetLeaf(temp);
        vleaf.push_back(lf);
    }
    if(VName.size()==0) cout<<"        ** No sub **"<<endl;
    cout<<"-------------------------------------------------------------"<<endl;
    return vleaf;
}

#endif




