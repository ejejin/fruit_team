



void n9_dynamic_TPad_gPad()
{
    TCanvas *c1 = new TCanvas("c1","dynamic slice example",10,10,700,500);
    TH2F *hpxpy = new TH2F("hpxpy","py vs px",40,-4,4, 40, -4,4);
    hpxpy->SetStats(0);

    float uxmin = gPad->GetUxmin();  ////Returns the minimum x-coordinate value visible on the pad  0
    float uxmax = gPad->GetUxmax();  ////Returns the maximum x-coordinate value visible on the pad  1
    int pxmin = gPad->XtoAbsPixel(uxmin);  // 0
    int pxmax = gPad->XtoAbsPixel(uxmax);  // this is related with the size of the canvas
    cout<<uxmin<<endl<<uxmax<<endl;
    cout<<pxmin<<endl<<pxmax<<endl;
    cout<<"uniqueID of gPad : "<<gPad->GetUniqueID()<<endl;

    Double_t px,py;
    for(Int_t i=0; i<50000; i++)
    {
        gRandom->Rannor(px,py);
        hpxpy->Fill(px,py);
    }
    hpxpy->Draw("col");

    int pxt = gPad->GetEventX();  // -1
    int pyt = gPad->GetEventY();  // -1
    cout<<pxt<<endl<<pyt<<endl;

    c1->AddExec("dynamic","Dynamic()");
}


void Dynamic()
{
    TObject *select = gPad->GetSelected();
    if(!select) return;
    if(!select->InheritsFrom(TH2::Class())) {gPad->SetUniqueID(0); return;}
    TH2 *h = (TH2*)select;
    gPad->GetCanvas()->FeedbackMode(kTRUE);

    //erase old position and draw a line at current position
    int pyold = gPad->GetUniqueID();
    int px = gPad->GetEventX();
    int py = gPad->GetEventY();
    float uxmin = gPad->GetUxmin();  ////Returns the minimum x-coordinate value visible on the pad
    float uxmax = gPad->GetUxmax();  ////Returns the maximum x-coordinate value visible on the pad
    int pxmin = gPad->XtoAbsPixel(uxmin);
    int pxmax = gPad->XtoAbsPixel(uxmax);

    if(pyold) gVirtualX->DrawLine(pxmin,pyold,pxmax,pyold);  // draws a line as declared in the coordinates
    gVirtualX->DrawLine(pxmin,py,pxmax,py);
    gPad->SetUniqueID(py);
    Float_t upy = gPad->AbsPixeltoY(py);
    Float_t y = gPad->PadtoY(upy);

    // create or set the neew canvas c2
    TVirtualPad *padsav = gPad;
    TCanvas *c2 = (TCanvas*)gROOT->GetListOfCanvases()->FindObject("c2"); // !!!!!!!!! this!!!!!!???????
    if(c2) delete c2->GetPrimitive("Projection");   // 
    else c2 = new TCanvas("c2","Projection Canvas",710,10, 700,500);
    c2->SetGrid();   // grid --> net ???
    c2->cd();

    // draw slice corresponding to mouse position
    Int_t biny = h->GetYaxis()->FindBin(y);  // this!!!!!!!!???
    TH1D *hp = h->ProjectionX("",biny,biny);
    hp->SetFillColor(38);
    char title[80];
    sprintf(title,"projection of biny=%d",biny);
    hp->SetName("Projection");
    hp->SetTitle(title);
//    hp->Fit("gaus","ql");
//    hp->GetFunction("gaus")->SetLineColor(kRed);
//    hp->GetFunction("gaus")->SetLineWidth(6);    
    hp->Draw();
    c2->Update();
    padsav->cd();

}








