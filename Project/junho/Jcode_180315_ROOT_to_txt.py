
from ROOT import TFile, TCanvas, TPad

wf= open("py-fillrandom_via_py.txt","w+")
f = TFile("py-fillrandom.root","READ");

hist=f.Get("h1f");
Nbin = hist.GetNbinsX();
bin1 = hist.GetBinContent(1); print(bin1)

for ii in range(1,Nbin+1):
    bin1 = hist.GetBinContent(ii);
    wf.write("%d %d\n" %(ii,bin1))

#f.write("This is line %d\r\n" % (i+1))


f.Close()
