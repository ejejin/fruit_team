

void padRefresh(TPad *pad, int flag=0)
{
    if(!pad) return;
    pad->Modified();
    pad->Update();
    TList *tl = (TList*)pad->GetListOfPrimitives();
    if(!tl) return;
    
    TListIter next(tl);  // Create a new list iterator. By default the iteration direction is kIterForward. To go backward use kIterBackward.

    TObject *to;  
    while((to=next()))
    { 
        if(to->InheritsFrom(TPad::Class())) padRefresh((TPad*)to,1);
    }
    if(flag) return;
    gSystem->ProcessEvents(); //???? Process pending events, Returns the result of TROOT::IsInterrupted(). This mechanism allows macros running in tight calculating loops to be interrupted by some GUI event 

}


void n16_refresh_Ts_TH1K()
{
    TCanvas *c1 = new TCanvas("c1","Dynamic Filling Example", 200,10, 600,900);    
    TH1 *hpx[3];   // !!!!! way to define histograms
    hpx[0] = new TH1F("hp0","hp0",1000,-4,4);
    hpx[1] = new TH1K("hp1","hp1",1000,-4,4);    //!!!!!! nearest K Neighbours method, widely used in cluster analysis
    hpx[2] = new TH1K("hp2","hp2",1000,-4,4,16); // TH1K::TH1K(name,title,nbins,xlow,xup,K=0)
                                                 // K - is the order of K Neighbours method, usually >=3, default 0
                                                 // This method is especially useful for small statistics

    c1->Divide(1,3);
    Int_t j;
    for(j=0; j<3; j++)
    {
        c1->cd(j+1);
        hpx[j]->SetFillColor(48);
        hpx[j]->Draw();   // draw empty histogram
    }
    
    //Fill histo randomly
//    gRandom->SetSeed(12345);
    Float_t px, py, pz;
    const Int_t kUPDATE = 10;
    for(Int_t i=0; i<=300; i++)
    {
        gRandom->Rannor(px,py);    // !!!!!!!
        for(j=0;j<3;j++) {hpx[j]->Fill(px);}
        if(i && (i % kUPDATE) == 0)
        { padRefresh(c1);}
    }
 
    padRefresh(c1);

}
