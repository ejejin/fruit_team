#include "TBenchmark.h"
#include "TPad.h"
#include "TCanvas.h"
#include "TFormula.h"
#include "TF1.h"
#include "TFrame.h"
#include "TPaveLabel.h"

void n13_gPad_gBanchmark_TF1_TFormula_fill()
{
    TCanvas *c1 = new TCanvas("c1","the fill random example",200,10,700,900);
    TPad *pad1 = new TPad("pad1","the pad with the function", 0.05, 0.50, 0.95, 0.95);
    auto pad2 = new TPad("pad2","the pad with the histogram", 0.05, 0.05, 0.95, 0.45);
    pad1->Draw();
    pad2->Draw();
    
    pad1->cd();
   
    gBenchmark->Start("fillrandom"); 
    auto form1 = new TFormula("form1","abs(sin(x)/x)");                //// TFormula !!!!!!
    auto sqroot = new TF1("sqroot","x*gaus(0) + [3]*form1", 0, 10);  /// interfacing TFormula, gaus(0) is a substitute for [0]*exp(-0.5*((x-[1])/[2])**2)
    sqroot->SetParameters(10,4,1,20); // ??????? 4 params, 3 from gaus(0) ? 
    pad1->SetGridx();    // !!!! adding gridline for x axis
    pad1->SetGridy(); 
    pad1->GetFrame()->SetBorderMode(-1);
    pad1->GetFrame()->SetBorderSize(5);
//    pad1->Modified(); pad1->Update();   // it is said need this line, but why?????
    sqroot->SetLineColor(4);
    sqroot->SetLineWidth(6);
    sqroot->Draw();
//    pad2->cd();
//    pad2->SetGridy();
//    sqroot->Draw(); 

    auto lfunction = new TPaveLabel(5,39,9.8,46,"The sqroot function");
    lfunction->Draw();
    c1->Update();    // ??????????????

    pad2->cd();
    pad2->GetFrame()->SetBorderMode(-1);
    pad2->GetFrame()->SetBorderSize(5);
    auto h1f = new TH1F("h1f","Test random numbers",200,0,10);
    h1f->SetFillColor(45);
    h1f->FillRandom("sqroot",10000);   // !!!!!!!??????!!!!!!! inducing "TF1", name with sqroot
    h1f->Draw();
    c1->Update();   // ??????

    TFile myfile("n13.root","RECREATE");
    form1->Write();  // calling with variable name.. not "~" name... ?????!!!!
    sqroot->Write();
    h1f->Write();
    gBenchmark->Show("fillrandom");
}
