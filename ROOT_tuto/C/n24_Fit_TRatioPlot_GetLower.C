#include "TStyle.h"
#include "TCanvas.h"
#include "TH1.h"
#include "TRatioPlot.h"


void n24_Fit_TRatioPlot_GetLower()
{
    gStyle->SetOptStat(0); // removing the box of stats????
    auto c1 = new TCanvas("c1", "fit residual simple"); 
    auto h1 = new TH1D("h1","h1",50,-5,5);
    h1->FillRandom("gaus",2000);
    h1->Fit("gaus");
    h1->GetXaxis()->SetTitle("x");
    c1->Clear();  // Fit does not draw into correct pad
    auto rp1 = new TRatioPlot(h1);
    rp1->Draw();
    rp1->GetLowerRefYaxis()->SetTitle("ratio");   // !!!!! GetLowerRefYaxis
    rp1->GetLowYaxis()->SetNdivisions(505); 
    rp1->GetUpperRefYaxis()->SetTitle("entries");
//    rp1->GetXaxis()->SetTitle("range");   // !!!!!this is not working, the x-axis title need to be set via h1
    c1->Update();
 
}
