//root -l -q TwoD_profileX_pol_fitter.C\('"/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_re_tree_cut_hist2D.root"'\)

#include "TROOT.h"
#include "TKey.h"
#include "TFile.h"
#include "TSystem.h"
#include "TTree.h"
#include "TH2D.h"
#include <vector>
#include "n1_read_2d_histos.h"
using namespace std;

void TwoD_profileX_pol_fitter(string File)
{
    gStyle->SetOptStat(0);
//    gStyle->SetOptStat(1000000001);
    gStyle->SetOptFit(1);
    string infile= File;
    vector<TH2D*> TwoD_histos;
    vector<string> TwoD_histos_Name;
    n1_read_2d_histos* READ_2d = new n1_read_2d_histos();
    TwoD_histos = READ_2d->TwoD_HISTs(&infile);
    TwoD_histos_Name = READ_2d->TwoD_HISTs_Name(&infile);
    
    for(int i=0; i<TwoD_histos.size(); i++)
    {
        TCanvas *c1 = new TCanvas();
        c1->Divide(3,2);
        string SAVENAME, SAVENAME_pdf;
        SAVENAME = TwoD_histos_Name.at(i);
        SAVENAME_pdf = TwoD_histos_Name.at(i)+"_profileX_pol_2D.pdf";
        for(int j=0; j<6; j++)
        {
            c1->cd(j+1);
            TProfile *prof = TwoD_histos.at(i)->ProfileX();
            prof->SetMarkerStyle(7);
            prof->SetDirectory(0);
            if(j==0) prof->Fit("pol1");
            else if(j==1) prof->Fit("pol2");
            else if(j==2) prof->Fit("pol3");
            else if(j==3) prof->Fit("pol4");
            else if(j==4) prof->Fit("pol5");
            else if(j==5) {/*prof->SetStats(1111);*/prof->Draw();}
//            else if(j==3) TwoD_histos.at(i)->Draw();
            c1->Modified();
            c1->Update();
            prof->Clear();
        }    
        c1->SaveAs(SAVENAME_pdf.data());
        c1->Clear();
    }
}

