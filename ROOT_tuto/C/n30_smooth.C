
int ipad = 1;
TCanvas *c1 = 0;

void smooth_hist(const char *func_name, double xmin, double xmax, int n1, int n2)
{
    std::cout<<"smoothing a " << func_name << " histogram" << std::endl;
    TH1D * h1 = new TH1D("h1","h1",100,xmin,xmax);
   TH1D * h2 = new TH1D("h2","h2",100,xmin,xmax);
   h1->FillRandom(func_name,n1);

    TH1D * h1_s = new TH1D(*h1);
   h1_s->SetName("h1_s");    // THIS !!!!!!! way of setting name of histogram
    h1_s->Smooth();     ///!!!!!!!!!!! Smooth() ????? Smooth bin contents of this histogram ?????
    h1_s->Draw();

}

void n30_smooth(int n1=1000, int n2 = 1000000)
{
    TH1::AddDirectory(false);  //// !!!!!!!!! Sets the flag controlling the automatic add of histograms in memory.  By default (fAddDirectory = kTRUE), histograms are automatically added to the list of objects in memory.  histogram can be removed from its support directory by calling h->SetDirectory(0) or h->SetDirectory(dir) to add it to the list of objects in the directory dir.
    
    c1 = new TCanvas();
    
    smooth_hist("gaus",-5,5,n1,n2);


}

