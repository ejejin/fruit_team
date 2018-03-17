
void n31_TPaveStats_TGaxis()
{
       TCanvas *c1 = new TCanvas("c1","transparent pad",200,10,700,500);
   TPad *pad1 = new TPad("pad1","",0,0,1,1);
   TPad *pad2 = new TPad("pad2","",0,0,1,1);
   pad2->SetFillStyle(4000); //will be transparent  !!!!!!!!!!
   pad1->Draw();
   pad1->cd();

    TH1F *h1 = new TH1F("h1","h1",100,-3,3);
   TH1F *h2 = new TH1F("h2","h2",100,-3,3);
    TRandom r; 
    for(Int_t i=0; i<100000; i++)
    {
        Double_t x1 = r.Gaus(-1,0.5);
        Double_t x2 = r.Gaus(1, 1.5);
        if(i<1000) h1->Fill(x1);
        h2->Fill(x2); 
    }
    h1->Draw();
    pad1->Modified();
    pad1->Update();   ////this will force the generation of the "stats" box!!!!!!

    TPaveStats *ps1 = (TPaveStats*)h1->GetListOfFunctions()->FindObject("stats");
//    TPaveStats *ps01 = (TPaveStats*)pad1->GetPrimitive("stats");   // this would give out same result !!!!!!
    ps1->SetX1NDC(0.4); //new x start position of stats box  !!!!!!!
    ps1->SetX2NDC(0.6); //new x end position of stats box !!!!!!!
    pad1->Modified();    
    pad1->Update();

    c1->cd(); // !!!!!! move to canvas
    Double_t ymin = 0;
    Double_t ymax = 2000;
    Double_t dy = (ymax-ymin)/0.8;
    Double_t xmin = -3;
    Double_t xmax = 3;
    Double_t dx = (xmax - xmin)/0.8;
    pad2->Range(xmin-0.1*dx,ymin-0.1*dy,xmax+0.1*dx,ymax+0.1*dy);
    pad2->Draw();
    pad2->cd();
    h2->SetLineColor(kRed);
    h2->Draw("][sames");
    pad2->Update();    
    TPaveStats *ps2 = (TPaveStats*)pad2->GetPrimitive("stats");
    ps2->SetX1NDC(0.65); ps2->SetX2NDC(0.85);
    ps2->SetTextColor(kRed);

    TGaxis *axis = new TGaxis(xmax, ymin, xmax, ymax, ymin,ymax, 50510, "+L");  //!!!!Double_t xmin, Double_t ymin, Double_t xmax, Double_t ymax,  Double_t wmin, Double_t wmax..  wmin :: Lowest value for the tick mark labels written on the axis.
    axis->SetLabelColor(kRed);
    axis->Draw();
    c1->Update();
}




