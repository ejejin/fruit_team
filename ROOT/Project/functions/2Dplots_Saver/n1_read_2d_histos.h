#ifndef _N1_READ_2D_HISTOS_H_
#define _N1_READ_2D_HISTOS_H_

#include "TROOT.h"
#include "TKey.h"
#include "TFile.h"
#include "TSystem.h"
#include "TTree.h"
#include "TH2D.h"
#include <vector>
#include <string>
using namespace std;


class n1_read_2d_histos
{ 
    public:
        n1_read_2d_histos();
        vector<TH2D*> TwoD_HISTs(string *str);
        vector<string> TwoD_HISTs_Name(string *str);
        void Draw_n_Save_Histos();

        vector<TH2D*> TwoD_hists;
        vector<string> NAMES;
};

n1_read_2d_histos::n1_read_2d_histos()
{
}

vector<TH2D*> n1_read_2d_histos::TwoD_HISTs(string *str)
{
//    vector<TH2D*> TwoD_hists;
    TFile *file = new TFile(str->data(),"READ");    
    TKey *key;
    TIter nextkey(file->GetListOfKeys());
    while((key = (TKey*)nextkey()))
    {
        string classname = key->GetClassName();
        if(classname != "TH2D") {cout<<"This is not TH2D histo, error!"<<endl; continue;}
        TH2D *temphist = (TH2D*)key->ReadObj();
        temphist->SetDirectory(0);
//        key->Get->GetName();
//        cout<<classname<<endl;
//        cout<<key->GetName()<<endl;
//        Vstr.push_back(key->GetName());
//        Vstr.push_back(classname);
        TwoD_hists.push_back(temphist);
        
    }

    file->Close();
    return TwoD_hists;
}
vector<string> n1_read_2d_histos::TwoD_HISTs_Name(string *str)
{
//    vector<string> NAMES;
    TFile *file = new TFile(str->data(),"READ");
    TKey *key;
    TIter nextkey(file->GetListOfKeys());
    while((key = (TKey*)nextkey()))
    {
        string classname = key->GetClassName();
        if(classname != "TH2D") {cout<<"This is not TH2D histo, error!"<<endl; continue;}
        NAMES.push_back(key->GetName());
//        cout<<key->GetName()<<endl;
    }
    file->Close();
    return NAMES;        
}

void n1_read_2d_histos::Draw_n_Save_Histos()
{
    for(int i=0; i<TwoD_hists.size(); i++)
    {
          TCanvas *can = new TCanvas();
          string SAVENAME, SAVENAME_pdf;
          SAVENAME = NAMES.at(i);
          SAVENAME_pdf = NAMES.at(i)+".pdf";
          TwoD_hists.at(i)->Draw();
          can->SaveAs(SAVENAME_pdf.data());
          can->Clear();
    }

}

#endif
