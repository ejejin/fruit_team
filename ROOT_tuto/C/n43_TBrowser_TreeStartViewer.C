
void n43_writeTree()
{
    TFile f("n43.root","RECREATE");
    TTree t1("t1","t1");
    Float_t px, py, pz;
    Double_t random;
    Int_t ev;
    t1.Branch("px",&px,"px/F");
    t1.Branch("py",&py,"py/F");
    t1.Branch("pz",&pz,"pz/F");
    t1.Branch("random",&random, "random/D");
    t1.Branch("ev", &ev, "ev/I");

    for(Int_t i=0; i<10000; i++)
    {
        gRandom->Rannor(px,py);
        pz = px*px + py*py;
        random = gRandom->Rndm();
        ev = i;
        t1.Fill();
    }
    t1.Write();
}

void n43_readTree()
{
    TFile *f = TFile::Open("n43.root","READ");
    TTree *t1 = (TTree*)f->Get("t1");
    Float_t px, py, pz;
    Double_t random;
    Int_t ev;

    t1->SetBranchAddress("px",&px);
    t1->SetBranchAddress("py",&py);
    t1->SetBranchAddress("pz",&pz);
    t1->SetBranchAddress("random",&random);
    t1->SetBranchAddress("ev",&ev);
  
    TH1F *hpx = new TH1F("hpx","hpx",100,-3,3);
    TH2F *hpxpy = new TH2F("hpxpy","hpxpy",30,-3,3,30,-3,3);

    Long64_t nentries = t1->GetEntries();
    for(Long64_t i=0; i<nentries; i++)
    {
        t1->GetEntry(i);
        hpx->Fill(px);
        hpxpy->Fill(px,py);
    }
    if(gROOT->IsBatch()) return ;    // ????  in order to keep the generated histograms???
    new TBrowser();
    t1->StartViewer();

}



void n43_TBrowser_TreeStartViewer()
{
    n43_writeTree();
    n43_readTree();


}
