

void n33_readfile_ntuple_Fill_dat()
{
    TString dir = gROOT->GetTutorialDir();
//    TString *dir1 = gROOT->GetTutorialDir();   // !!!!! error !!!!
    cout<<"string dir : "<<dir<<" "<<endl<<"type name : "<<typeid(dir).name()<<endl;
    
    dir.Append("/tree/");  // TString Append() !!!!!
    cout<<"string dir : "<<dir<<endl;
    dir.ReplaceAll("/./","/");  //!!!!! TString, ReplaceAll() !!!!

    ifstream in;
    in.open(Form("%sbasic.dat",dir.Data()));  // !!!!!!!!! open file with "ifstream" 
    Float_t x, y, z;
    Int_t nlines = 0;
    auto f = TFile::Open("basic.root","RECREATE");   // !!!!! TFile !!!
    TH1F h1("h1","h1",100,-4,4);   // !!!!!!  define TH1F class object without *
    TNtuple ntuple("ntuple","ntuple","x:y:z");   // !!!!!! ntuple definition!!!!!
    
    while(1)
    {
        in >>x>>y>>z;    // !!!!!! read in a line
        if(!in.good()) break;   /// break !!!!!!
        if(nlines<5)  printf("x=%8f, y=%8f, z=%8f\n",x,y,z); 
        h1.Fill(x);
        ntuple.Fill(x,y,z);
        nlines++;
    }

    in.close();
    f->Write();
}
