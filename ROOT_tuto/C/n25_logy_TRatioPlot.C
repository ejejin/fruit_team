

void n25_logy_TRatioPlot()
{
    gStyle->SetOptStat(0);
    auto c1 = new TCanvas("c1", "fit residual simple");
    c1->SetLogy();   ///!!!!!!! set log Y on canvas!!! 
    auto h1 = new TH1D("h1", "h1", 50, -5, 5);
    h1->FillRandom("gaus", 2000);
    h1->Fit("gaus");
    h1->SetMinimum(0.001);
    h1->GetXaxis()->SetTitle("x");
    h1->GetYaxis()->SetTitle("y");
    c1->Clear();
    auto rp1 = new TRatioPlot(h1);
    rp1->Draw();
    rp1->GetLowerRefGraph()->SetMinimum(-2);
    rp1->GetLowerRefGraph()->SetMaximum(2);
    c1->Update();


}
