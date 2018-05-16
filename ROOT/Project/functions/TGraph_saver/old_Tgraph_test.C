//root -l -q Tgraph_test.C\('"/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"'\)

#include <vector>
#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <cstring>
#include "../ROOT_txt_reader/n1_ROW_VECTOR.h"
#include "../ROOT_txt_reader/n2_COL_VECTOR.h"

using namespace std;

void Tgraph_test(string file)
{
    vector<string> R_STR;
    vector<vector<string>> R_STR_split;   // Row string splited
    n1_ROW_VECTOR* row_vector = new n1_ROW_VECTOR();
    R_STR = row_vector->MAKE_ROW_VECTOR(&file);
    R_STR_split = row_vector->MAKE_ROW_VECTOR_split(R_STR);

    vector<vector<string>> C_STR_split; 
    n2_COL_VECTOR* col_vector = new n2_COL_VECTOR();
    C_STR_split = col_vector->MAKE_COL_VECTOR_split(R_STR_split);

    TCanvas *c1 = new TCanvas();
    c1->SetGrid();

    const Int_t NUM = C_STR_split.at(0).size();
    cout<<NUM<<endl;

    Double_t x[NUM], y[NUM];
    for(Int_t i=0; i<NUM; i++)
    {
        if(i==0) continue;
        x[i] = atof((C_STR_split.at(1).at(i)).data());
        y[i] = atof((C_STR_split.at(2).at(i)).data());
    }
//    cout<<x[NUM-1]<<endl;
    cout<<C_STR_split.at(1).at(0)<<endl;
    cout<<C_STR_split.at(2).at(0)<<endl;
    TGraph *gr = new TGraph(NUM,x,y);
    gr->Draw("AP");
    
    c1->Update();
    c1->GetFrame()->SetBorderSize(12);
    c1->Modified();
    c1->SaveAs("test.pdf");

//    cout<< C_STR_split.at(0).size()<<endl;
/*
    for(int i=0; i<R_STR_split.size(); i++)
    {
        for(int j=0; j<R_STR_split.at(i).size(); j++)
        {
            cout<<R_STR_split.at(i).at(j)<<" ";
        }
        cout<<endl;
    }


    for(int i=0; i<C_STR_split.size(); i++)
    {
        for(int j=0; j<C_STR_split.at(i).size();j++)
        {
            cout<<C_STR_split.at(i).at(j)<<" ";
        }
        cout<<endl;
    }
*/
}


