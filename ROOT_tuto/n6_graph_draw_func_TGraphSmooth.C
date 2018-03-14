
TCanvas *vC1;
TGraph *grxy, *grin, *grout;

void DrawSmooth(Int_t pad, const char *title, const char *xt, const char *yt)
{
    vC1->cd(pad);
    TH1F *vFrame = gPad->DrawFrame(0,0,15,150);   // !!!! gPad and DrawFrame !!!!!
    vFrame->SetTitle(title);
    vFrame->SetXTitle(xt);
    vFrame->SetYTitle(yt);
    grxy->SetMarkerColor(kBlue);
    grxy->SetMarkerStyle(21); 
    grxy->SetMarkerSize(0.5);
    grxy->Draw("P");
    grin->SetMarkerColor(kRed);
    grin->SetMarkerStyle(5);
    grin->SetMarkerSize(0.5);
    grin->Draw("P");
    grout->DrawClone("LP");
}



void n6_graph_draw_func_TGraphSmooth()
{
    Int_t n = 11;
    const int n1 = 11;
    Double_t x[n1] = {1,2,3,4,5,6,6,6,8,9,10};
    Double_t y[] = {1,4,9,16,25,25,36,49,64,81,100};
    grxy = new TGraph(n,x,y);
    grin = new TGraph(n,x,y);

    Int_t nout = 14;
    Double_t xout[] = {1.2,1.7,2.5,3.2,4.4,5.2,5.7,6.5,7.6,8.3,9.7,10.4,11.3,13};

    vC1 = new TCanvas("vC1","square",200,10,700,700);
    vC1->Divide(2,2);

    TGraphSmooth *gs = new TGraphSmooth("normal");     /// !!!!!!!! TGraphSmooth !!!!
    grout = gs->Approx(grin,"linear");
    DrawSmooth(1, "Approx: ties = mean", "X-axis", "Y-axis");

    grin = new TGraph(n,x,y);
    grout = gs->Approx(grin, "linear", 14, xout, 0, 130);    //setting upper limit and x-value
    DrawSmooth(2,"Approx: ties = mean", "", "");
    Double_t xOut, yOut = 0;
    grout->GetPoint(0, xOut, yOut);  cout<<xOut<<endl<<yOut<<endl;  ////// !!!!!! GetPoint() to get points
    grin->GetPoint(0, xOut, yOut);  cout<<xOut<<endl<<yOut<<endl;
    Int_t Num = grin->GetN();   // !!!!!! GetN() to get containing element number
    cout<<Num<<endl;   //dont know but only 9 remains out of 11   

    // so need to initialize the graph everytime before used
    grin = new TGraph(n, x, y);
    grout = gs->Approx(grin, "constant", 50, 0, 0, 0, 1, 0.5, "min");    // parameters ??????
    DrawSmooth(3, "Approx : ties = min","","");

    grin = new TGraph(n,x,y);
    grout = gs->Approx(grin, "linear", 14, xout, 0, 0, 2, 0,  "max");
    DrawSmooth(4, "Approx: ties = max","x","y");

    delete gs;
}
