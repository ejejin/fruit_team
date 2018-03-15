

void n27_TRatioPlot_sigmaband()
{
    gStyle->SetOptStat(0);
   auto c1 = new TCanvas("c1", "fit residual simple");
   auto h1 = new TH1D("h1", "h1", 50, -5, 5);
   h1->FillRandom("gaus", 2000);
   h1->Fit("gaus");
   h1->GetXaxis()->SetTitle("x");
   h1->GetYaxis()->SetTitle("y");
   c1->Clear();
   auto rp1 = new TRatioPlot(h1);
   rp1->SetConfidenceIntervalColors(kBlue, kRed);  //kBlue for the 1 sigma band, kRed for the 2 sigma band
   rp1->Draw();
   c1->Update();





}
