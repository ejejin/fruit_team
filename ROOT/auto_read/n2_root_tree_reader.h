#ifndef _ROOT_TREE_READER_H_
#define _ROOT_TREE_READER_H_

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include "TTree.h"
#include "TFile.h"
#include "n2_read_tree_name.h"

class n2_root_tree_reader
{
    public:
        ifstream infile;
        n2_root_tree_reader();
        vector<TTree*> Vtree;
        vector<TTree*> Read_tree(string *str);

//        vector<TH1F*> MakeHistos(string *str, int NBIN = 100, double LOW = -1, double HIGH = 1);
//        vector<TH1F*> vhisto;
};

n2_root_tree_reader::n2_root_tree_reader()
{
//    cout<<"The input root file : "<<str->data()<<endl;
}

vector<TTree*> n2_root_tree_reader::Read_tree(string *str)
{
    TFile *file = new TFile(str->data(),"READ");
	n2_read_tree_name *Name = new n2_read_tree_name();
    vector<string> VName;
    string stemp = str->data();
    VName = Name->NameOfTree(&stemp);
//    VName = Name->NameOfTree(&(str->data()));
    cout<<endl<<"!!! Number of trees : "<<VName.size()<<endl;
    Vtree.clear(); 
    for(int i1=0; i1<VName.size(); i1++)
    {
        TTree *t = new TTree();
	    string stemp2 = VName.at(i1);
        cout<<"!!! Tree name : "<<stemp2<<endl;
        const char* ctemp2 = stemp2.data();
        t = (TTree*)file->Get(ctemp2);
        Vtree.push_back(t);
    }

    return Vtree;
}
/*
vector<TH1F*> n2_root_tree_reader::MakeHistos(string *str, int NBIN = 100, double LOW = -1, double HIGH = 1)
{
    TFile *file = new TFile(str->data(),"READ");
    n2_read_tree_name *Name = new n2_read_tree_name();
    


    return vhisto;
}
*/

#endif
