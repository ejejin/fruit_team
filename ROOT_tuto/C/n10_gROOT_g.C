


void n10_gROOT_g()
{
    TString dir = gROOT->GetTutorialDir();
    cout<<"1 : "<<dir<<"  "<<typeid(dir).name()<<endl;
    cout<<"2 : "<<dir.Data()<<"  "<<typeid(dir.Data()).name()<<endl;

    dir.Append("/hsimple.C");
//    TString xx = ".x ";
//    TString xxdir = xx + dir;
//    cout<<"3 : "<<xxdir<<"  "<<typeid(xxdir).name()<<endl;
//    cout<<"4 : "<<xxdir.Data()<<"  "<<typeid(xxdir.Data()).name()<<endl;
//    gROOT->ProcessLine(xxdir.Data());  // !!!!!!!!this will launch the process "hismple.C"
//    gSystem->Load("/Users/leejunho/Downloads/root6_cmake/tutorials/hsimple.root");   // root file could be loaded!!!!!! 
//    gROOT->ProcessLine("ntuple->Print()");     // print tree components
    
    if(!gInterpreter->IsLoaded(dir.Data()))   gInterpreter->LoadMacro(dir.Data());
//    TFile *file = (TFile*)gROOT->ProcessLine("hsimple(1)");   // ???? what is different with processLineFast????
    TFile *file = (TFile*)gROOT->ProcessLineFast("hsimple(1)");
    if(!file) return;

    TTree *ntuple = (TTree*)file->Get("ntuple");

    TCanvas *c1 = new TCanvas("c1","Contours", 10, 10, 800,800);
    ntuple->Draw("py:px","px*px+py*py < 10","contz,list");
    TCanvas *ct = new TCanvas("ct","Contours_t", 10, 10, 1200,900);
    ct->Divide(2,2);
    ct->cd(1);
    ntuple->Draw("py:px","","col");
    ct->cd(2); ct->SetGrid();
    ntuple->Draw("py:px","","cont");
    ct->cd(3);
    ntuple->Draw("py:px","","contz");
    ct->cd(4);
    ntuple->Draw("py:px","","contz,list");

    c1->Update(); ct->Update();
    // "Update()" must to be called to force the canvas to be painted. ????????


    TCanvas *c2 = new TCanvas("c2","First contour", 100,100,800,600);
    TObjArray *contours = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");  //this !!!!!!!!??????
    cout<<"Entries of contours : "<<contours->GetEntries()<<endl;
    if(!contours) return;
    TList *lcontour1 = (TList*)contours->At(0);
    if(!lcontour1) return;
    cout<<"Entries of lcontour1 : "<<lcontour1->GetEntries()<<endl;
    TGraph *gc1 = (TGraph*)lcontour1->First();   // return the first object in the TList
    if(!gc1) return;
    if(gc1->GetN()<10) return;
    gc1->SetMarkerStyle(21);
    gc1->Draw("alp");


}

