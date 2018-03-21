
R__LOAD_LIBRARY($ROOTSYS/test/libEvent.so)

void n38_GetBranch_SetFile_CopyEntries_CloneTree()
{
    TFile *oldfile;
    TString dir = "$JUNHO_PATH/n43_VBSWW_LL_TT_TL_lhe/root_generator/";
    gSystem->ExpandPathName(dir);
    if(!gSystem->AccessPathName(dir))
    {
        oldfile = new TFile("$JUNHO_PATH/n43_VBSWW_LL_TT_TL_lhe/root_generator/output_lhe_VBSWW_TL.root");
    }
    else 
    {
        oldfile = new TFile("./output_lhe_VBSWW_TL.root");
    }
    Event *event = new Event();
    TTree *oldtree = (TTree*)oldfile->Get("treeE");
    oldtree->SetBranchStatus("*",0);
    oldtree->SetBranchStatus("W1Pt",1);
    oldtree->SetBranchStatus("W2Pt",1);

    TFile *newfile = new TFile("n38_small.root","RECREATE");
    TTree *newtree = oldtree->CloneTree(0);  // !!!!!!!! Clone the tree with '0' entries !!!!
    newtree->GetBranch("W1Pt")->SetFile("n38_small_W1Pt.root");// ??????? why is empty ???
    newtree->CopyEntries(oldtree,-1);   // copy entries !!!!!!! 
    
    newtree->Print();
    newtree->Write();
    
    delete newfile;
    delete oldfile;
}





