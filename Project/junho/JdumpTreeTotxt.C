#include <iostream>
#include "TFile.h"
#include "TTree.h"
#include <fstream>
using namespace std;

void JdumpTreeTotxt(){
    TFile *f=new TFile("py-fillrandom.root"); // opens the root file
    TH1 *hist=(TH1*)f->Get("h1f"); // creates the TTree object
    
    Double_t Nbin, bin, count;
    
    bin = hist->GetBinContent(1);
    cout<<bin<<endl;

//   ofstream myfile;
//   myfile.open ("example.txt");
//    myfile.close();



}
