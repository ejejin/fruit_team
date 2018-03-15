
TCanvas *n12_cumulative_assert()
{ 
    TCanvas *c = new TCanvas();
    TH1* h = new TH1D("h","h", 100,-5,5);
    gRandom->SetSeed();     /// !!!!!!!!???????
//    h->FillRandom("gaus", 1u<<16);   //// ?????????
    h->FillRandom("gaus", 10000);
    TH1* hc = h->GetCumulative(); //////!!!!!!!! culmulative!!!!
    Double_t *integral = h->GetIntegral();
    cout<<" num of bins : "<<hc->GetNbinsX()<<endl;   

    for(Int_t i=1; i<=hc->GetNbinsX(); i++)
    {
        if(i%10 == 0) cout<<integral[i]<<endl<<h->GetEntries()<<endl<<hc->GetBinContent(i)<<endl<<endl;
        assert(std::fabs(integral[i] * h->GetEntries() - hc->GetBinContent(i)) < 1e-7);  // end the program if assert(0)
    }
    c->Divide(1,2);    
    c->cd(1); h->Draw();
    c->cd(2); hc->Draw();
    c->Update();
   
    return c;
}
