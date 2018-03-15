



void n22_3D_GetBin_GetBinContent(Int_t isStack=0)
{
    TCanvas *c1 = new TCanvas;
   Int_t nbins = 20;
   TH2F *h1 = new TH2F("h1","h1",nbins,-4,4,nbins,-4,4);
   h1->SetFillColor(kBlue);
   TH2F *h2 = new TH2F("h2","h2",nbins,-4,4,nbins,-4,4);
   h2->SetFillColor(kRed);
   TH2F *h3 = new TH2F("h3","h3",nbins,-4,4,nbins,-4,4);
   h3->SetFillColor(kYellow);
   THStack *hs = new THStack("hs","three plots");
   hs->Add(h1);
   hs->Add(h2);
   hs->Add(h3);
   TRandom r;
   Int_t i;
    for(i=0;  i<20000; i++)
    {
        h1->Fill(r.Gaus(),r.Gaus());
    }
   for (i=0;i<200;i++) { 
      Int_t ix = (Int_t)r.Uniform(0,nbins);
      Int_t iy = (Int_t)r.Uniform(0,nbins);      // Uniform() from TRandom	!!!!!!
      Int_t bin = h1->GetBin(ix,iy);             // GetBin() obtain specific bin!!!!!!! (even though it is 2D)
      Double_t val = h1->GetBinContent(bin);    // !!!!!! GetBinContent(bin) to get number of specified bin
      if (val <= 0) continue;
      if (!isStack) h1->SetBinContent(bin,0);    // !!!!!!!!! ????? why do I need isStack ???
      if (r.Rndm() > 0.5) {
         if (!isStack) h2->SetBinContent(bin,0);
         h2->SetBinContent(bin,val);
      } else {
         if (!isStack) h3->SetBinContent(bin,0);
         h3->SetBinContent(bin,val);
      }  
   }
//    hs->Draw("lego1");
    hs->Draw();



}
