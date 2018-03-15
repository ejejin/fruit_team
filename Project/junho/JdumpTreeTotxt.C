#include <iostream>
#include "TFile.h"
#include "TTree.h"
#include <fstream>
using namespace std;

void JdumpTreeTotxt(){
    TFile *f=new TFile("py-fillrandom.root"); // opens the root file
    TH1 *hist=(TH1*)f->Get("h1f"); // creates the TTree object
    
    Double_t Nbin, bin, count;
   
    Nbin = hist->GetNbinsX(); 
    bin = hist->GetBinContent(1);
    cout<<Nbin<<endl<<bin<<endl;
 
    ofstream myfile;
    myfile.open("example.txt");
    for(Int_t i=1; i<=Nbin; i++)
    {
        bin = hist->GetBinContent(i);
        myfile <<i<<" "<<bin<<"\n";

    }
    myfile.close();
//   ofstream myfile;
//   myfile.open ("example.txt");
//    myfile.close();



}
