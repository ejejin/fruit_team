


void n19_sum()
{
    TCanvas *c1 = new TCanvas("c1","The HSUM example",200,10,600,400);
    c1->SetGrid();

    gBenchmark->Start("hsum");

    TH1F* total = new TH1F("total", "This is the total distribution",100,-4,4);
    auto main   = new TH1F("main","Main contributor",100,-4,4);
    auto s1     = new TH1F("s1","This is the first signal",100,-4,4);
    auto s2     = new TH1F("s2","This is the second signal",100,-4,4);

    total->Sumw2();  // store the sum of squares of weights !!!!!!!
    total->SetMarkerStyle(21);
    total->SetMarkerSize(0.7);
    main->SetFillColor(16);
    s1->SetFillColor(42);
    s2->SetFillColor(46);
    TSlider *slider = 0;  //The TSliderBox can be moved in the pad.Slider drawing options include the possibility to change the slider starting and ending positions or only one of them.
    
    gRandom->SetSeed();
    const Int_t kUPDATE = 500;
    Float_t xs1, xs2, xmain;
    for ( Int_t i=0; i<10000; i++)
    {
        xmain = gRandom->Gaus(-1, 1.5);  //!!!!!!!!!! gRandom->Gaus
        xs1 = gRandom->Gaus(-0.5, 1.5);
        xs2 = gRandom->Landau(1, 0.5);
        main->Fill(xmain);
        s1->Fill(xs1, 0.3);
        s2->Fill(xs2, 0.2);

        total->Fill(xmain);
        total->Fill(xs1, 0.3);
        total->Fill(xs2, 0.2);

//        if( i && (i%kUPDATE) == 0) 
//        {
     }
     total->Draw("e1p");       
     main->Draw("same");
     s1->Draw("same");
     s2->Draw("same");

     gBenchmark->Show("hsum");
}




