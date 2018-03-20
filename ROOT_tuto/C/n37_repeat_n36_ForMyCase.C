
R__LOAD_LIBRARY($ROOTSYS/test/libEvent.so)

void n37_repeat_n36_ForMyCase()
{
    TFile *oldfile;
    TString dir = "$JUNHO_PATH/n43_VBSWW_LL_TT_TL_lhe/root_generator/";
    gSystem->ExpandPathName(dir);   // !!!!!! Expand a pathname getting rid of special shell characters like ~.
    if(!gSystem->AccessPathName(dir))   // !!!!! Returns FALSE if one can access a file using the specified access mode.
    {
        oldfile = new TFile("$JUNHO_PATH/n43_VBSWW_LL_TT_TL_lhe/root_generator/output_lhe_VBSWW_TT.root");
    }
    else 
    {
        oldfile = new TFile("./output_lhe_VBSWW_TT.root");
    }
    
    TTree *oldtree = (TTree*)oldfile->Get("treeE");
    Event *event = new Event();

    oldtree->SetBranchStatus("*",0);
    oldtree->SetBranchStatus("W1Pt",1);
    oldtree->SetBranchStatus("W2Pt",1);
    oldtree->SetBranchStatus("P1Pt",1);
    oldtree->SetBranchStatus("P2Pt",1);

    TFile *newfile = new TFile("n37_root.root","RECREATE");
    TTree *newtree = oldtree->CloneTree();
    
    newtree->Print();
    newtree->Write();
    delete newfile;
    delete oldfile;
}
