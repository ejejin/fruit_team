


void n29_stats_TPaveStats_TList_TText_TLatex()
{
    TCanvas *se = new TCanvas;
    TH1F *h = new TH1F("h","test",100,-3,3);
    h->FillRandom("gaus",3000);
    gStyle->SetOptStat();
    h->Draw();
    se->Update();

    // Retrieve the stat box
    TPaveStats *ps = (TPaveStats*)se->GetPrimitive("stats");  // !!!!!! get stat box!!!!!
    ps->SetName("mystats");   //!!!!!!!! TPaveStats, SetName()
    TList *listOfLines = ps->GetListOfLines();  // !!!!!!!!!!  from TPaveStats, get list of lines???? 
    TList *listOfLines1 = (TList*)ps->GetListOfLines();  //!!!!! I think this is better way....

    listOfLines1->Print();    
//    TText *tconst = (TText*)ps->GetLineWith("RMS"); // !!!!!!! TText GetLineWith
    TText *tconst = (TText*)ps->GetLineWith("Entries");
    listOfLines1->Remove(tconst);    // !!!!! seems TList is container of TText
//    cout<<typeid(listOfLines1).name()<<"  "<<typeid(tconst).name()<<endl;
    TLatex *myt = new TLatex(0,0,"JTest");   // TLatex
    myt->SetTextFont(42);  // shape of text !!!!!!!
    myt->SetTextSize(0.04);
    myt->SetTextColor(kRed);
    listOfLines1->Add(myt);
    h->SetStats(0);   //!!!!!!!!!!!!! Need this Line to avoid that the automatic redrawing of stats

    se->Modified();  // !!!!!!!!!!!! Need this line to update the changes on Canvas
//    se->Update();  // this seems useless ......???????

}
