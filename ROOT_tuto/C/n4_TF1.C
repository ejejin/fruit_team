#include "TF1.h"
#include "TH1D.h"
#include "TVirtualFitter.h"
#include "TMath.h"
#include <assert.h>  //"assert" : if the program meet assert error, the program ends 
#include <iostream>
#include <cmath>

TF1 *fitFunc;
const int NPAR=2;

double f(double *x, double*p)
{
    return p[1]*TMath::Sin(p[0] * x[0]);
}


void n4_()
{
    fitFunc = new TF1("ff",f,0,1,NPAR);
    TH1D *h1 = new TH1D("h1","h1",50,0,1);
    
    double par[NPAR] = {3.14, 1.};
    fitFunc->SetParameters(par);     
//    fitFunc->Draw();
    h1->FillRandom("ff",1000);       // "ff" is the name of the "fitFunc"
//    h1->Draw();

//    fitFunc->SetParameter(0,3.0);    
    h1->Fit(fitFunc);               // fit the "fitFunc" to the histogram
    h1->Draw();

    




}








