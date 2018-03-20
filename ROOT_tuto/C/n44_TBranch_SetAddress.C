#include <iostream>
#include "TFile.h"
#include "TTree.h"
#include "TBrowser.h"
#include "TH2.h"
#include "TRandom.h"
#include "TCanvas.h"
#include "TMath.h"
#include "TROOT.h"
#include "TH1F.h"

using namespace std;
const Int_t MAXMEC = 3;
//  Int_t MAXMEC = 30;   !!!! this cause error for "Int_t lmec[MAXMEC];"

typedef struct {
  Float_t  vect[MAXMEC];
//  Float_t  vout[7];
//  Int_t    lmec[MAXMEC];
//  Int_t    namec[MAXMEC];
//  Float_t  upwght;
} myStruct;


void n44_makeChanges(Float_t step, Float_t *vect, Float_t *vout)
{
    enum Enumerate {kX, kY, kZ, kPP}; //!!! for default kX==0, kY==1, kZ==2, kPP==3
    vout[kPP] = vect[kPP]; 
    Float_t f1 = step * gRandom->Rndm(1);
    Float_t f2,f3=0;
    gRandom->Rannor(f2,f3);
    vout[kX] = vect[kX] + (f1*vect[kX] - f2*vect[kY]);  vout[kX] = double(vout[kX] - double(int(vout[kX])));
    vout[kY] = vect[kY] - (f1*vect[kY] + f2*vect[kX]);  vout[kY] = double(vout[kY] - double(int(vout[kY])));
    vout[kZ] = vect[kZ] + (f1*vect[kZ] - f3);           vout[kZ] = double(vout[kZ] - double(int(vout[kZ])));
}

void n44_treeWrite()
{
    TFile f("n44.root","RECREATE");
    TTree t2("t2","t2");
    myStruct data;

    t2.Branch("vect",data.vect, "vect[3]/F");   // not need "&" for data.vect because of its data type!!!!!!!    

    Float_t px, py, pz=0;
    Float_t vout[3];

    for(Int_t i=0; i<10000; i++)
    {
        if(i==0)
        {
            data.vect[0] = 0.1;
            data.vect[1] = 0.2;
            data.vect[2] = 0.3;
        }
        else
        {
            n44_makeChanges(1, data.vect, vout);
            data.vect[0] = vout[0];
            data.vect[1] = vout[1];
            data.vect[2] = vout[2];
        }
        t2.Fill();
        vout[0] = 0;
        vout[1] = 0;
        vout[2] = 0;
    }
    t2.Write();
    std::cout<<"successfully generated the root file!"<<std::endl;
}

void n44_readTree()
{
    TFile *f = new TFile("n44.root","READ");
    TTree *t2 =(TTree*)f->Get("t2");
    Float_t vect[MAXMEC];
    TBranch *b_vect = t2->GetBranch("vect");    b_vect->SetAddress(vect);  //!!!!!!!!

    TH1F *hvect0 = new TH1F("hvect0","hvect0",100,-1.1,1.1);   hvect0->SetLineColor(kRed);
    TH1F *hvect1 = new TH1F("hvect1","hvect1",100,-1.1,1.1);   hvect1->SetLineColor(kBlue);
    TH1F *hvect2 = new TH1F("hvect2","hvect2",100,-1.1,1.1);   hvect2->SetLineColor(kMagenta);
    TH1F *hvect = new TH1F("hvect","hvect",100,-1.1,1.1);   hvect->SetLineColor(kGreen);

    Long64_t nentries = t2->GetEntries();
    for(Int_t i=0; i<nentries; i++)
    {
        b_vect->GetEntry(i);   // !!!!!!!!!
        hvect0->Fill(vect[0]);
        hvect1->Fill(vect[1]);
        hvect2->Fill(vect[2]);
    }
    hvect->Add(hvect0); hvect->Add(hvect1); hvect->Add(hvect2);
    hvect->Draw();
    hvect0->Draw("same");
    hvect1->Draw("same");
    hvect2->Draw("same");
}


void n44_TBranch_SetAddress()
{
    n44_treeWrite();
    n44_readTree();


}


