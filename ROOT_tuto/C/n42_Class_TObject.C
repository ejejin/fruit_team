

class Detector
{
    public:
        Double_t e;
        Double_t t;
};

class Event : public TObject    // !!!!!!!!!!?????????
{
    public:
        Detector a;
        Detector b;
        ClassDef(Event,1);
};
ClassImp(Event);


void n42_Class_TObject()
{
    TFile *f = TFile::Open("n42.root","RECREATE");
    TTree *tree = new TTree("tree","tree");
    Event *e = new Event;
    tree->Branch("event",&e);

    Int_t nevent = 10000;
    for(Int_t iev=0; iev<nevent; iev++)
    {
        if(iev%1000==0) cout<<"Processing event "<<iev<<"..."<<endl;
        Float_t ea, eb;
        gRandom->Rannor(ea,eb);
        e->a.e = ea;
        e->b.e = eb;
        e->a.t = gRandom->Rndm();
        e->b.t = e->a.t + gRandom->Gaus(0.,.1);
        tree->Fill();
    }
    tree->Write();
    TCanvas *c1 = new TCanvas();
    c1->Divide(2,2);
    c1->cd(1);
    tree->Draw("a.e");    //!!!! it will automatically find the leaf name "a.e"
    tree->Draw("a.e","3*(-0.2<b.e && b.e<0.2)","same");    
    c1->cd(2);
    tree->Draw("b.e:a.e","","colz");
    c1->cd(3);
    tree->Draw("b.t","","e");
    tree->Draw("a.t","","same");
    c1->cd(4);
    tree->Draw("b.t:a.t","","colz");

}


