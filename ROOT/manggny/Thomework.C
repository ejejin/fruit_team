#include "TGraph.h"

void Thomework()
{
    TCanvas *c1 = new TCanvas("c1","Thomework1",200,10,700,500);
    TH1D *h1 = new TH1D("h1","first hist!!",100,-5,5);
    h1 -> FillRandom("gaus",10000);
    h1 -> Draw();
    
    return c1;
}
