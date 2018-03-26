

void test1_FRAME()
{

    Float_t NBins =  100;         // total bin number
    Float_t IBin =   0.3;        // lower edge of X-axis
    Float_t FBin =   1.1;          // higher edge of X-axis

    TFile *infile = new TFile("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root","READ");  //Correctly input file name
    TFile *outfile = new TFile("outfile_please_modify_correspondingly_C.root","RECREATE");  // name of output file, please modify correspondingly  !!!!!

    TTree *t1 = (TTree*)infile->Get("tree1");// check the tree name 
    TTree *t2 = (TTree*)infile->Get("tree2");

    Double_t px, py, pz;

    t1->SetBranchAddress("px",&px);  // SetBranchAddress for each tree
    t1->SetBranchAddress("py",&py);
    t1->SetBranchAddress("pz",&pz);
    t2->SetBranchAddress("px",&px);
    t2->SetBranchAddress("py",&py);
    t2->SetBranchAddress("pz",&pz);

    TH1F *hist1 = new TH1F("hist1","hist1",NBins, IBin, FBin);    // define 1D histogram
    TH1F *hist2 = new TH1F("hist2","hist2",NBins, IBin, FBin);   
    TH1F *hist3 = new TH1F("hist3","hist3",NBins, IBin, FBin);

    Long64_t ENTRY = t1->GetEntries();
    for(Int_t i =0; i<ENTRY; i++)
    {
        t1->GetEntry(i);
        if(px>-1 && py>-0.5 && pz< 3.0)             //  add condition !!!! IMPORTANT !!!!!
        {
            hist1->Fill(px);                          //  Select parameter and fill histos
        }
        else continue;
    }

    ENTRY = t2->GetEntries();
    for(Int_t i =0; i<ENTRY; i++)
    {
        t2->GetEntry(i);
        if(px>-1 && py>0.5 && pz< 3.0)             //  add condition !!!! IMPORTANT !!!!!
        {
            hist2->Fill(py);                          //  Select parameter and fill histos
        }
        else continue;
    }

    ENTRY = t2->GetEntries();
    for(Int_t i =0; i<ENTRY; i++)
    {
        t2->GetEntry(i);
        if(py>0.5)             //  add condition !!!! IMPORTANT !!!!!
        {
            hist3->Fill(py);                          //  Select parameter and fill histos
        }
        else continue;
    }
    
    hist1->Write();
    hist2->Write();
    hist3->Write();
    infile->Close();
    delete infile;
}


