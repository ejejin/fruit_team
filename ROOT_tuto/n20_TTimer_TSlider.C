
Float_t progressRatio;
TSlider *slider;
TCanvas *c1;

void hsumUpdate()
{
    if(slider) slider->SetRange(0, ::progressRatio);
    c1->Modified();
    c1->Update();
}


void n20_TTimer_TSlider(Int_t nfill = 100000)  // !!!!!! set maximum
{
    c1 = new TCanvas("c1", "The HSUM example", 200, 10, 600, 400);
    c1->SetGrid();

   auto total  = new TH1F("total","This is the total distribution",100,-4,4);
   auto main   = new TH1F("main","Main contributor",100,-4,4);
   auto s1     = new TH1F("s1","This is the first signal",100,-4,4);
   auto s2     = new TH1F("s2","This is the second signal",100,-4,4);

   total->Sumw2();   // store the sum of squares of weights
   total->SetMarkerStyle(21);
   total->SetMarkerSize(0.7);
   main->SetFillColor(16);
   s1->SetFillColor(42);
   s2->SetFillColor(46);    
   total->SetMaximum(nfill/20.);
   total->Draw("e1p");
   main->Draw("same");
   s1->Draw("same");
   s2->Draw("same");
   c1->Update();
   slider = new TSlider("slider","test",4.2,0,4.6,0.8*total->GetMaximum(),38);  // !!!!!!
   slider->SetFillColor(kBlue);

   TTimer timer("hsumUpdate()",100);  // !!!!!!!!!!! unit : ms
   timer.TurnOn();    // !!!!!!!

   Float_t xs1, xs2, xmain;
   gRandom->SetSeed();
   for (Int_t i=0; i<nfill; i++) {
      ::progressRatio = Float_t(i)/Float_t(nfill);  //   ???????????????
      if (gSystem->ProcessEvents()) break;
      xmain = gRandom->Gaus(-1,1.5);
      xs1   = gRandom->Gaus(-0.5,0.5);
      xs2   = gRandom->Landau(1,0.15);
      main->Fill(xmain);
      s1->Fill(xs1,0.3);
      s2->Fill(xs2,0.2);
      total->Fill(xmain);
      total->Fill(xs1,0.3);
      total->Fill(xs2,0.2);
   }
   timer.TurnOff();      //!!!!!!!!!!
   hsumUpdate();

}
