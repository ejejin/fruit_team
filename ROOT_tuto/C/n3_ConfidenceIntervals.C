#include "TGraph.h"
#include "TGraphErrors.h"
#include "TCanvas.h"
#include "TF2.h"
#include "TF1.h"
#include "TH1.h"
#include "TVirtualFitter.h"
#include "TRandom.h"

void n3_ConfidenceIntervals()
{
    TCanvas *can = new TCanvas("can","can",1200,500);
    can->Divide(3,1);

//***** first graph
    Int_t np = 100;
    TGraph *gr = new TGraph(np);
    gr->SetName("GraphNoError");
    Double_t x,y;       
    Int_t i;

    for(i=0; i<np; i++)
    {
        x = gRandom->Uniform(-1,1);
        y = -1 + 2*x + gRandom->Gaus(0,1);
        gr->SetPoint(i,x,y);
    }
//    can->cd(1);    gr->Draw();
    TF1 *fpol = new TF1("fpol","pol1",-1,1);
    fpol->SetLineWidth(2);
    gr->Fit(fpol,"Q");   // "Q" makes not printing of the fit result
//    gr->Draw();
    
    TGraphErrors *grint = new TGraphErrors(np);
    grint->SetTitle("Fitted line with .95 conf. band");
    for(i=0; i<np; i++)
    {
        grint->SetPoint(i, gr->GetX()[i], 0);     // SetPoint(Int_t i, Double_t x, Double_t y)
    }
//    grint->Draw();
    (TVirtualFitter::GetFitter())->GetConfidenceIntervals(grint, 0.95);   // set confidenceIntervals
//    grint->Draw();
    can->cd(1);
    grint->SetLineColor(kRed);
    grint->Draw("ap");
    gr->SetMarkerStyle(5);
    gr->SetMarkerSize(0.7);
    gr->Draw("psame");



//**** second histogram
    can->cd(2);
    Int_t nh = 500;
    TH1D *h = new TH1D("h","Fitted gaussian with .95 conf. band", 100, -3, 3);
    h->SetStats(0);
    h->FillRandom("gaus",nh);
//    h->Draw();
    TF1 *f = new TF1("fgaus","gaus",-3,3);
    f->SetLineWidth(2);
    h->Fit(f,"Q");
    h->Draw();

    TH1D *hint = new TH1D("hint","Fitted gaussian with .95 conf. band", 100, -3, 3);
    (TVirtualFitter::GetFitter())->GetConfidenceIntervals(hint, 0.95);
    hint->SetFillColor(kGreen);
    hint->Draw("e3 same");


//**** third 2d graph
    Int_t ngr2 = 100;
    Double_t z, rnd, e = 0.3;
    TGraph2D *gr2 = new TGraph2D(ngr2);
    gr2->SetName("Graph2DNoError");
    TF2 *f2 = new TF2("f2","1000*(([0]*sin(x)/x)*([1]*sin(y)/y))+250",-6,6,-6,6);
    f2->SetParameters(1,1);
    for(i=0; i<ngr2; i++)
    {
        f2->GetRandom2(x,y);
        rnd = 2 * gRandom->Rndm()*e - e;
        z = f2->Eval(x,y) * (1+rnd);
        gr2->SetPoint(i, x,y,z);
    }
    
    TGraph2DErrors *grint2 = new TGraph2DErrors(ngr2);
    for(i=0; i<ngr2; i++)
    {
        grint2->SetPoint(i, gr2->GetX()[i], gr2->GetY()[i],0);
    }
    f2->SetParameters(0.5,1.5);
    gr2->Fit(f2, "Q");

    can->cd(3);
    

}











