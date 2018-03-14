



void n11_hist_DrawCopy()
{
    TCanvas *c1 = new TCanvas("c1","divides",800,600);
    c1->Divide(3,2);
    
    TRandom *randnum = new TRandom();
    TH2I *h1 = new TH2I("h1","Sin", 18,0,360, 300, -1.5, 1.5);
    h1->GetXaxis()->SetTitle("Degree");
    float myRand;
    for(int i=0; i<360;  i+=10)
    {
        for(int j=0; j<100; j++)
        {
            myRand = randnum->Gaus(sin(i*3.14/180),0.2);
            h1->Fill(i,myRand);
        }
    }

//    h1->Draw();
    for(int i=1; i<7; i++)
    {
        c1->cd(i);
        char str[16];
        sprintf(str,"candlex%d",i);
        TH2I *myhist = (TH2I*)h1->DrawCopy(str);
        myhist->SetTitle(str);
    }

    TCanvas *c2 = new TCanvas("c2","candle individual", 800,600);
    c2->Divide(4,4); 
    char myopt[16][8] = {"0","1","11","21","31","30","111","311","301","1111","2321","12111","112111","212111","312111"};
    for(int i=0; i<15; i++)
    {
        c2->cd(i+1);
        char str[16];
        sprintf(str, "candlex(%s)", myopt[i]);
        TH2I *myhist = (TH2I*)h1->DrawCopy(str);
        myhist->SetTitle(str);
    }
}
