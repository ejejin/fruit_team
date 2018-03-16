

void n35_Branch_Rannor_Rndm()
{
    TFile *f = new TFile("circular.root","RECREATE");
    auto T = new TTree("T","T");
    TRandom r;
    Float_t px, py, pz;
    Double_t randomNum;
    UShort_t i;       // ???????????

    T->Branch("px",&px,"px/F");
    T->Branch("py",&py,"py/F");
    T->Branch("pz",&pz,"pz/F");
    T->Branch("randomNum",&randomNum,"randomNum/D");
    T->Branch("i",&i,"i/s");
    T->SetCircular(20000);   //!!!!! keep a maximum of 20000 entries in memory !!!!
    
    for(i=0; i<65000; i++)
    {
        r.Rannor(px,py);
        pz = px*px + py*py;
        randomNum = r.Rndm();
        T->Fill();
    }
    T->Write();
    f->Close();
}
