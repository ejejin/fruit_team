
void n41_write_vector_update_histo()    // I don't know why error here.....
{
    TFile *f = TFile::Open("n41.root","RECREATE");
    if(!f) return;
    
    TH1F *hpx = new TH1F("hpx","hpx",100,-4,4);
    hpx->SetFillColor(48);    // !!!!! set fill color for histogram is possible..
    
    std::vector<float> vpx;
    std::vector<float> vpy;
    std::vector<float> vpz;
    vector<float> vrand;

    TTree *t = new TTree("t","t");
    t->Branch("vpx",&vpx);
    t->Branch("vpy",&vpy);
    t->Branch("vpz",&vpz);
    t->Branch("vrand",&vrand);
    
    TCanvas *c1 = new TCanvas("c1","c1",200,10, 700,500);
    gRandom->SetSeed();
    const Int_t kUPDATE = 1000;
    for(Int_t i=0; i<25000; i++)
    {
        Int_t npx = (Int_t)(gRandom->Rndm(1)*15);
        vpx.clear();
        vpy.clear();
        vpz.clear();
        vrand.clear();
        
        for(Int_t j=0; j<npx; j++)
        {
            Float_t px,py,pz;
            gRandom->Rannor(px,py);
            pz = px*px + py*py;
            Float_t random = gRandom->Rndm(1);
            hpx->Fill(px);
            vpx.emplace_back(px);     //!!!!!! fill the vector with "emplace_back()" !!!!
            vpy.emplace_back(py);
            vpz.emplace_back(pz);
            vrand.emplace_back(random);
        }
        
        if( i && (i%kUPDATE) == 0)
        {
            if(i==kUPDATE) hpx->Draw();
            c1->Modified();
            c1->Update();
            if(gSystem->ProcessEvents())   // !!!!!! Process pending events, Returns the result of TROOT::IsInterrupted()
                break;
        }
        t->Fill();
    }
    f->Write();
    delete f;
}


void n41_read()
{
    TFile *f = TFile::Open("n41.root","READ");
    if(!f) return;
     
    TTree *t;
    f->GetObject("tvec",t);   // !!!!!!!! GetObject() !!!!!
    vector<float> *vpx = 0;
    
//    TCanvas *c1 = new TCanvas("c1","c1",200,10,700,500);
    TCanvas *c2 = new TCanvas("c2","c2",200,10,700,500);
    const Int_t kUPDATE = 1000;
    TBranch *bvpx = 0;
    t->SetBranchAddress("vpx",&vpx,&bvpx);

    TH1F *h = new TH1F("h","h",100,-4,4);
    h->SetFillColor(48);
    
    for(Int_t i=0; i<25000; i++)
    {
        Long64_t tentry = t->LoadTree(i);   // Set current entry.
        bvpx->GetEntry(tentry);

        for(UInt_t j=0; j<vpx->size(); ++j)  // vpx is a vector
        {
            h->Fill(vpx->at(j));
        }
        
        if(i && (i%kUPDATE) == 0)
        {
            if(i==kUPDATE) h->Draw();
            c2->Modified();
            c2->Update();
            if(gSystem->ProcessEvents())
                break;
        }
    }
    t->ResetBranchAddresses(); //!!! Since we passed the address of a local variable we need to remove it 

}


void n41_()
{
    gBenchmark->Start("n41");
    n41_write_vector_update_histo();
    n41_read();
    gBenchmark->Show("n41");
}
