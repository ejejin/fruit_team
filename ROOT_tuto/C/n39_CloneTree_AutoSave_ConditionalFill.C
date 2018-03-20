
R__LOAD_LIBRARY($ROOTSYS/test/libEvent.so)

void n39_CloneTree_AutoSave_ConditionalFill()
{
    TFile *oldfile;
    TString dir = "$ROOTSYS/test/Event.root";
    gSystem->ExpandPathName(dir);
    if(! gSystem->AccessPathName(dir))
    {
        oldfile = new TFile("$ROOTSYS/test/Event.root");
    }
    else
    {
        oldfile = new TFile("./Event.root");
    }
    
    TTree* oldtree = (TTree*)oldfile->Get("T");
    Long64_t nentries = oldtree->GetEntries();
    cout<<"total entry : " <<nentries<<endl;
    Event *event = 0;
    oldtree->SetBranchAddress("event",&event);
    
    TFile *newfile = new TFile("n39_small.root","recreate");
    TTree *newtree = oldtree->CloneTree(0);
//    Long64_t nentries = oldtree->GetEntries();

    for(Long64_t i=0; i<nentries; i++)
    {
        oldtree->GetEntry(i);
        if(event->GetNtrack() >605) newtree->Fill();
        event->Clear();
    }
   newtree->Print();
   newtree->AutoSave();
   delete oldfile;
   delete newfile;

}
