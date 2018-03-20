#include "TFile.h"
#include "TTree.h"
#include "TRandom.h"
#include "TCanvas.h"

void n45_writeTree_n_friendTree()
{
   const Int_t kMaxTrack = 500;
   Int_t ntrack;
   Int_t stat[kMaxTrack];
   Int_t sign[kMaxTrack];
   Float_t px[kMaxTrack];
   Float_t py[kMaxTrack];
   Float_t pz[kMaxTrack];
   Float_t pt[kMaxTrack];
   Float_t zv[kMaxTrack];
   Float_t chi2[kMaxTrack];
   Double_t sumstat;

   TFile f("n45.root","recreate");
   TTree *t3 = new TTree("t3","t3");
   t3->Branch("ntrack",&ntrack,"ntrack/I");
   t3->Branch("stat",stat,"stat[ntrack]/I");   // not [kMaxTrack] but [ntrack] !!!!! no '&' on 'stat' !!!!!
   t3->Branch("sign",sign,"sign[ntrack]/I");
   t3->Branch("px",px,"px[ntrack]/F");
   t3->Branch("py",py,"py[ntrack]/F");
   t3->Branch("pz",pz,"pz[ntrack]/F");
   t3->Branch("zv",zv,"zv[ntrack]/F");
   t3->Branch("chi2",chi2,"chi2[ntrack]/F");

   TFile fr("n45f.root","recreate");
   TTree *t3f = new TTree("t3f","a friend Tree");
   t3f->Branch("ntrack",&ntrack,"ntrack/I");
   t3f->Branch("sumstat",&sumstat,"sumstat/D");
   t3f->Branch("pt",pt,"pt[ntrack]/F");

   for (Int_t i=0;i<1000;i++) {
      Int_t nt = gRandom->Rndm()*(kMaxTrack-1);
      ntrack = nt;
      sumstat = 0;
      for (Int_t n=0;n<nt;n++) {
         stat[n] = n%3;
         sign[n] = i%2;
         px[n]   = gRandom->Gaus(0,1);
         py[n]   = gRandom->Gaus(0,2);
         pz[n]   = gRandom->Gaus(10,5);
         zv[n]   = gRandom->Gaus(100,2);
         chi2[n] = gRandom->Gaus(0,.01);
         sumstat += chi2[n];
         pt[n]   = TMath::Sqrt(px[n]*px[n] + py[n]*py[n]);
      }
      t3->Fill();
      t3f->Fill();
   }
   f.cd();
   t3->Write();
   fr.cd();
   t3f->Write();
}

void n45_AddFriend1()
{
    TCanvas *c1 = new TCanvas("c1","c1");
    TFile *f = new TFile("n45.root","READ");
    TTree *t = (TTree*)f->Get("t3");
    t->AddFriend("t3f","n45f.root");    //TTree::AddFriend	(const char* treename, const char* filename = "" )		
    t->Draw("pz","pt>3");
}

void n45_AddFriend2()
{
    TPad *p = new TPad("p","p",0.6, 0.4, 0.98,0.8);
    p->Draw(); p->cd();
    TFile *f = new TFile("n45.root","READ");
    TFile *ff= new TFile("n45f.root","READ");
    TTree *t = (TTree*)f->Get("t3");
    t->AddFriend("t3f",ff);  // TTree::AddFriend  (const char* treename, TFile* file)
    t->Draw("pz","pt>3");
}

void n45_AddFriend_branchsetting()
{
    n45_writeTree_n_friendTree();
    n45_AddFriend1();
    n45_AddFriend2();
}
