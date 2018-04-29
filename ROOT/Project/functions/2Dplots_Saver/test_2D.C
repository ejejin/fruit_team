//root -l -q test_2D.C\('"/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_re_tree_cut_hist2D.root"'\)

#include <iostream>
#include "TFile.h"
#include "TH2D.h"
#include "TCanvas.h"

using namespace std;
//void test_2D(string File)
void test_2D()
{
    TFile *file = new TFile("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_re_tree_cut_hist2D.root","READ");
//    cout<<File<<endl;
//    TFile *file = new TFile(File.data(),"READ");
    TCanvas *can = new TCanvas();
    TH2D* tdhist = (TH2D*)file->Get("Aqi_Beijing_day_re_f_X_SO2_Y_PM2p5");
    tdhist->SetDirectory(0);
//    tdhist->SetName("tdhist");
//    tdhist->Print();
    double ymin, ymax, xmin, xmax, xbin, ybin;
    ymin = tdhist->GetYaxis()->GetXmin(); ymax=tdhist->GetYaxis()->GetXmax();
    xmin = tdhist->GetXaxis()->GetXmin(); xmax=tdhist->GetXaxis()->GetXmax(); 
    ybin = (ymax-ymin)/70;
    xbin = (xmax-xmin)/70;
    tdhist->Rebin2D(int(xbin),int(ybin));
    tdhist->Draw("lego");   //surf3
//    tdhist->Draw("surf3 same");
    can->SaveAs("test.pdf");

    file->Close();
}


