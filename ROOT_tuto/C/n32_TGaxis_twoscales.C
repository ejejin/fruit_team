


void n32_TGaxis_twoscales()
{
    TCanvas *c1 = new TCanvas("c1","hists with different scales",600,400);
   
   //create/fill draw h1
   gStyle->SetOptStat(kFALSE);
   TH1F *h1 = new TH1F("h1","my histogram",100,-3,3);
   Int_t i; 
    h1->FillRandom("gaus",10000);
//    h1->Scale(0.0001);   // !!!!!! error if 1/1000 ....
    h1->Draw("hist");   // !!!!! draw in fashion of histogram
    c1->Update();

    TH1F *hint1 = new TH1F("hint1","h1 bins integral",100,-3,3);
   Float_t sum = 0;
   for (i=1;i<=100;i++)    // !!!!!!! Bin number is starting from 1 !!!!!!!
   {
      sum += h1->GetBinContent(i);    // GetBinContent()
      hint1->SetBinContent(i,sum);    // SetBinContent()
   }
//    hint1->Draw("same");   // !!!!! this is not what we wanted !!!!!
    
    // scale hint1 to the pad coordinates
    Float_t rightmax = 1.1*hint1->GetMaximum();
    Float_t scale = gPad->GetUymax()/rightmax;
    hint1->SetLineColor(kRed);
    hint1->Scale(scale);
    hint1->Draw("same");
    
    // draw an axis on the right side
    TGaxis *axis = new TGaxis(gPad->GetUxmax(), gPad->GetUymin(), gPad->GetUxmax(), gPad->GetUymax(), 0, rightmax, 510, "+L");    // !!!!!!!!!!!!!!!!!! TGaxis to set yaxis for log cumulative function
    axis->SetLineColor(kRed);
    axis->SetLabelColor(kRed);
    axis->Draw();
    c1->Modified();
    c1->Update();
}
