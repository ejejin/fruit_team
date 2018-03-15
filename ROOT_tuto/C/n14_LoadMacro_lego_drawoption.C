



void n14_LoadMacro_lego_drawoption()
{
    TString dir = gROOT->GetTutorialDir();
    dir.Append("/hsimple.C");
    dir.ReplaceAll("/./","/");
    if(gBenchmark->GetBench("hsimple")<0) gInterpreter->LoadMacro(dir.Data());
    TFile *example = (TFile*)gROOT->ProcessLineFast("hsimple(1)");  //!!!! after load the macro, process 
    if(!example) return;
    
    example->ls();  /// you can do this!!!!!
    TH1 *hpx = (TH1*)example->Get("hpx");
//    TNtuple *ntu = (TNtuple*)example->Get("ntuple");
//    TTree *ntut = (TTree*)example->Get("ntuple");
//    ntu->Print(); cout<<endl; ntut->Print();

    TCanvas *c1 = new TCanvas("c1", "Histogram Drawing Options", 200, 10, 700, 900);
    TPad *pad1 = new TPad("pad1", "The pad with the funciton", 0.03, 0.62, 0.50, 0.92);
    TPad *pad2 = new TPad("pad2", "The pad with the histogram", 0.51, 0.62, 0.98, 0.92);
    TPad *pad3 = new TPad("pad3", "The pad with the hisgogram", 0.03, 0.02, 0.97, 0.57);
    pad1->Draw(); pad2->Draw(); pad3->Draw();

    TPaveLabel *title = new TPaveLabel(0.1, 0.94, 0.9, 0.98, "Drawing options for one dimensional histograms");
    title->SetTextFont(52);
    title->Draw();

    pad1->cd();
    pad1->SetGridy();
    pad1->GetFrame()->SetFillColor(18);
    hpx->SetFillColor(kRed);
    hpx->DrawCopy();   // !!!!! draw copy of the histogram
    TPaveLabel *label1 = new TPaveLabel(-3.5, 700, -1, 800, "Default");
    label1->Draw();

    pad2->cd();
    hpx->DrawCopy("lego1");    // !!!!!this 
    TPaveLabel *label2 = new TPaveLabel(-0.72,0.74,-0.22,0.88,"option Lego1");
    label2->Draw();
    TPaveLabel *label2a = new TPaveLabel(-0.93,-1.08,0.25,-0.92,
      "Click on lego to rotate");
    label2a->Draw();

    // Draw hpx with its errors and a marker.

    pad3->cd();
    pad3->SetGridx();
    pad3->SetGridy();
    hpx->SetMarkerStyle(21);   /// set marker style!!!!!!
    hpx->Draw("e1p");  // !!!!! only SetMarkerStyle() is not enough, in the Draw(), need to set options
    TPaveLabel *label3 = new TPaveLabel(2,600,3.5,650,"option e1p");
    label3->Draw();


}
