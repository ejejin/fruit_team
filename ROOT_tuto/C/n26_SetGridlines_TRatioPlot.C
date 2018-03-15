

void n26_SetGridlines_TRatioPlot()
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
    std::vector<double> lines = {-3, -2, 1, 0, 1, 2, 3};   // !!!!!! a way of define a vector
    cout<<lines.size()<<endl;
    
    rp1->SetGridlines(lines);  // !!!!!!! Set grid line manually!!!!!
    rp1->Draw();
    rp1->GetLowerRefGraph()->SetMinimum(-4); //!!!!!!!  ??? what is this for?????
    rp1->GetLowerRefGraph()->SetMaximum(4);
    c1->Update();
}
