
R__LOAD_LIBRARY($ROOTSYS/test/libEvent.so)

void n36_gSystem_Event_SetBranchStatus_delete()
{
    TFile *oldfile;
    TString dir = "$ROOTSYS/test/Event.root";   // !!!!!! $ROOTSYS in TString!!!!
    gSystem->ExpandPathName(dir);      //!!!!! gSystem->ExpandPathName() 
    if(!gSystem->AccessPathName(dir))  // !!!!! AccessPathName() !!!!!!
    {  
        oldfile = new TFile("$ROOTSYS/test/Event.root");
    }
    else 
    {
        oldfile = new TFile("./Event.root");
    }
//    cout<<gSystem->pwd()<<endl;
//    cout<<gSystem->GetDynamicPath()<<endl;
//    cout<<gSystem->GetIncludePath()<<endl;

    TTree *oldtree = (TTree*)oldfile->Get("T");  // !!!! tree name is "T" !!!!!
    Event *event = new Event();     // Event !!!!! Storage class for an event.  Maybe only on Tree not on histograms 
    oldtree->SetBranchAddress("event",&event); 
    oldtree->SetBranchStatus("*",0);   // !!!! SetBranchStatus :: "*", apply to all branches, status = 1 branch will be processed, = 0 branch will not be processed
    oldtree->SetBranchStatus("event",1);  
    oldtree->SetBranchStatus("fNtrack",1);
    oldtree->SetBranchStatus("fH",1);

    TFile *newfile = new TFile("small.root","RECREATE");
    TTree *newtree = oldtree->CloneTree(); // !!!!!!!! CloneTree()

    newtree->Print();
    newfile->Write();
    delete oldfile;   ////!!!!! delete the files
    delete newfile;
}
