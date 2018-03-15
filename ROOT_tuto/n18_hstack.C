

void n18_hstack()
{
    THStack *hs = new THStack("hs","Stacked 1D histogram");
    TH1F *h1st = new TH1F("h1st","h1st", 100,-4,4);
    h1st->FillRandom("gaus",20000);    ////!!!!!!!!!!
    h1st->SetFillColor(kRed);
    h1st->SetMarkerStyle(21);
    h1st->SetMarkerColor(kRed);
    hs->Add(h1st);
    TH1F *h2st = new TH1F("h2st","h2st",100,-4,4);
    h2st->FillRandom("gaus",15000);
    h2st->SetFillColor(kBlue);
    h2st->SetMarkerStyle(21);    
    h2st->SetMarkerColor(kBlue);
    hs->Add(h2st);
    TH1F *h3st = new TH1F("h3st","h3st",100,-4,4);
    h3st->FillRandom("gaus",10000);
    h3st->SetFillColor(kGreen);
    h3st->SetMarkerStyle(21);
    h3st->SetMarkerColor(kGreen);
    hs->Add(h3st);

    TCanvas *cst = new TCanvas("cst","stacked hists",10,10,700,700);
    cst->Divide(2,2);
    cst->cd(1);
    hs->Draw();

    cst->cd(2);
    gPad->SetGrid();
    hs->Draw("nostac, elp");

    cst->cd(3);
//    gPad->SetFrameFillColor(17);  //!!!!!!!!
    gPad->SetTheta(3.77);         // !!!!!!!  
    gPad->SetPhi(2.9);            // !!!!!!!
    hs->Draw("lego1");
 
    cst->cd(4);
    //create two 2-D histograms and draw them in stack mode
    gPad->SetFrameFillColor(17);
    THStack *a = new THStack("a","Stacked 2D histograms");

    TF2 *f1 = new TF2("F1","xygaus + xygaus(5) + xylandau(10)",-4,4,-4,4);
    Double_t params1[] = {130,-1.4,1.8,1.5,1, 150,2,0.5,-2,0.5, 3600,-2,0.7,-3,0.3};
    f1->SetParameters(params1);   //!!!!!!! no &, no * !!!! just ..
    TH2F *h2sta = new TH2F("h2sta","h2sta",20,-4,4,20,-4,4);
    h2sta->SetFillColor(kRed);
    h2sta->FillRandom("F1",4000);  /// !!!!!!!! fill with defined funciton "F1"
    
    TF2 *f2 = new TF2("f2","xygaus + xygaus(5)",-4,4,-4,4);
    Double_t params2[] = {100,-1.4,1.9,1.1,2, 80,2,0.7,-2,0.5};
    f2->SetParameters(params2);
    TH2F *h2stb = new TH2F("h2stb","h2stb",20,-4,4,20,-4,4);
    h2stb->SetFillColor(kBlue);
    h2stb->FillRandom("f2",3000);    
    a->Add(h2sta);
    a->Add(h2stb);
    a->Draw();
    return cst;
}
