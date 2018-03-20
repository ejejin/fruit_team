

void n34_TTree_fill_datafile()
{
    TString dir = gROOT->GetTutorialDir();
    dir.Append("/tree/"); 
    dir.ReplaceAll("/./","/");
    
//    TFile *f = TFile::Open("basic2.root","RECREATE");   // same with below!!!!!
    TFile *f = new TFile("basic2.root","RECREATE");
    TH1F *h1 = new TH1F("h1","h1",100,-4,4);
    TTree *t = new TTree("t","t");
    Long64_t nlines = t->ReadFile(Form("%sbasic.dat",dir.Data()),"x/D:y/D:z/D");   // !!!!!!! write into tree from dat file
    
    t->Write();
    f->Close();


}
