#ifndef _READ_TREE_NAME_H_
#define _READ_TREE_NAME_H_

#include "TROOT.h"
#include "TKey.h"
#include "TFile.h"
#include "TSystem.h"
#include "TTree.h"
#include <vector>


class n2_read_tree_name
{
    public:
        n2_read_tree_name();
        vector<string> NameOfTree(string *str);
        vector<string> Vstr;
        TFile *file1 = new TFile();
};

n2_read_tree_name::n2_read_tree_name()
{
//    cout<<"!!!read tree name invoked!!!"<<endl;
}

vector<string> n2_read_tree_name::NameOfTree(string *str)
{
//    TFile *file = new TFile(str->data(),"READ");
//    cout<<"input file name : "<<file->GetName()<<endl;
    file1 = new TFile(str->data(),"READ");
    TKey *key;
    TIter nextkey(file1->GetListOfKeys());
    while((key = (TKey*)nextkey()))
    {
        string classname = key->GetClassName();
        if(classname != "TTree") continue;
//        cout<<classname<<endl;
//        cout<<key->GetName()<<endl;
        Vstr.push_back(key->GetName());
//        Vstr.push_back(classname);
    }
    file1->Close();
    return Vstr;
    Vstr.clear();
}


#endif
