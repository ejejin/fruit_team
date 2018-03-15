


void n15_SetMarkerStyle()
{
    TCanvas *c = new TCanvas();
    gStyle->SetOptTitle(kFALSE);   // remove title
    gStyle->SetOptStat(0);         // ????

    TH1F *h1 = new TH1F("h1", "h1", 100,-4,4);
    TH1F *h2 = new TH1F("h2", "h2", 100,-4,4); 
    TH1F *h3 = new TH1F("h3", "h3", 100,-4,4);
    TH1F *h4 = new TH1F("h4", "h4", 100,-4,4);
    TH1F *h5 = new TH1F("h5", "h5", 100,-4,4);

    TRandom random;
    Double_t px,py;
    for(Int_t i=0; i<25000; i++)
    {
        random.Rannor(px,py);  // Return 2 numbers distributed following a gaussian with mean=0 and sigma=1
        h1->Fill(px,10.);      // I bet "10." is used for scaling 
        h2->Fill(px,8.);
        h3->Fill(px,6.);
        h4->Fill(px,4.);
        h5->Fill(px,2.);
    }

   h1->SetMarkerStyle(kFullCircle);
   h2->SetMarkerStyle(kFullSquare);
   h3->SetMarkerStyle(kFullTriangleUp);
   h4->SetMarkerStyle(kFullTriangleDown);
   h5->SetMarkerStyle(kOpenCircle);

   h1->Draw("PLC PMC");
   h2->Draw("SAME PLC PMC");
   h3->Draw("SAME PLC PMC");
   h4->Draw("SAME PLC PMC");
   h5->Draw("SAME PLC PMC");

    gPad->BuildLegend();

}

