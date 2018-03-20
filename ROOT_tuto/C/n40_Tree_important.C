
void n40_writeTree()
{
    gBenchmark->Start("hsimple");
    TFile* f = new TFile("n40_ht.root","RECREATE");
    auto T = new TTree("T","tree");
    auto hpx = new TH1F("hpx","hpx",100,-4,4);
    auto hpxpy = new TH2F("hpxpy","hpxpy",40, -4,4, 40, -4, 4);
    TProfile *hprof = new TProfile("hprof","hprof",100, -4, 4, 0, 20); //Profile histograms are used to display the mean value of Y and its error for each bin in X . standard deviation divided by the sqrt(n).
   // E(J) = sum Y  ,H(J)  =  sum Y,  L(J)  =  sum l (maybe number of entries of 'J' bin ) ,  h(J)  =  H(J)/L(J) mean of Y, s(J)  =  sqrt(E(J)/L(J)- h(J)**2) standard deviation of Y  (e.g. RMS),  e(J)  =  s(J)/sqrt(L(J)) standard error on the mean(this error will be shown). 
   
    T->Branch("hpx99","TH1F",&hpx, 32000);
//    T->Branch("hpx1","TH1F",&hpx, 32000, 1); // warns that cannot be splitted, set to 0
//    T->Branch("hpx2","TH1F",&hpx, 32000, 2); 
    T->Branch("hpx","TH1F",&hpx, 32000, 0); // (branchname, className, &p_object, bufsize, splitlevel) 
    // p_object is a pointer to an object.
    // splitlevel=0, the object is serialized in the branch buffer.
    // splitlevel=1, this branch will automatically be split into subbranches, with one subbranch for each data member or object of the object itself 
    T->Branch("hpxpy","TH2F",&hpxpy, 32000, 0);
    T->Branch("hprof","TProfile",&hprof, 32000, 0);
    Float_t px, py, pz;

    for(Int_t i=0; i<25000; i++)
    {
        if(i%1000 == 0) cout<<"at entry : "<<i<<endl;
        gRandom->Rannor(px,py);
        pz = px*px + py*py;
        hpx->Fill(px);
        hpxpy->Fill(px,py);
        hprof->Fill(px,pz);
        T->Fill();
    }
    T->Print();
    f->Write();
    delete f;
    gBenchmark->Show("hsimple");
}

void n40_CloneTree_with_specific_events()
{
    gBenchmark->Start("write 1");
    auto f = new TFile("n40_ht.root","READ");
    auto ff= new TFile("n40_ht1.root","RECREATE");
    auto T = (TTree*)f->Get("T");
    Int_t ENum = T->GetEntries() / 2;
    auto TC = T->CloneTree(ENum);

    TC->Print();
    TC->Write();
    delete f;
    delete ff;
 
    gBenchmark->Show("write 1");
}

void n40_read1_histos_from_Tree()
{
    gBenchmark->Start("read 1");
    auto f = new TFile("n40_ht.root","READ");
    auto T = (TTree*)f->Get("T");
    TH1F *hpx = nullptr;
    TH2F *hpxpy = nullptr;
    TProfile *hprof = nullptr;
    T->SetBranchAddress("hpx",&hpx);
    T->SetBranchAddress("hpxpy",&hpxpy);
    T->SetBranchAddress("hprof",&hprof);
    T->GetEntry(10000);   //!!!!!!!!!??????? error if no
    
    auto c1 = new TCanvas("c1","c1",10,10,600,1000);
    c1->Divide(1,3);
    c1->cd(1);
    hpx->Draw();
    c1->cd(2);
    hpxpy->Draw();
    c1->cd(3);
    hprof->Draw();
    c1->Print("n40_read1.png");

    delete f;
    gBenchmark->Show("read 1");
}

void n40_read2_TreeDraw()
{
    gBenchmark->Start("read 2");
    auto f = new TFile("n40_ht.root","READ");
    auto T = (TTree*)f->Get("T");
    auto c1 = new TCanvas("c2","c2",10,10, 600, 1000);
    c1->Divide(1,3);
    c1->cd(1);
    T->Draw("hpx.Draw()","","goff",25000,100); // !!!!! const char * 	varexp, const char * 	selection, Option_t * 	option = "", Long64_t 	nentries = kMaxEntries, Long64_t 	firstentry = 0   ?????
    c1->cd(2);
    T->Draw("hpxpy.Draw()","","",1,12345); // !!
    c1->cd(3);
    T->Draw("hprof.Draw()","","goff",1,12345); // !!!! If option contains the string "goff", no graphics is generated, maybe recycle???? 
    c1->Print("n40_read2.png");
}

void n40_read3_TreeDraw_gPad()
{
    auto can = new TCanvas("can","can",10,10,600,1000);
    auto f = new TFile("n40_ht.root","READ");
    auto T = (TTree*)f->Get("T");
    T->Draw("hpx.GetRMS():hprof.GetMean()"); //!!!!read all histograms and plot the RMS of hpx versus the Mean of hprof for each of the 25000 entries
    gPad->Print("n40_read3.png");

}


void n40_Tree_important()
{
    n40_writeTree();
    n40_CloneTree_with_specific_events();
    n40_read1_histos_from_Tree();
    n40_read2_TreeDraw();
    n40_read3_TreeDraw_gPad();
}
