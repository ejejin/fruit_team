from ROOT import TFile, TCanvas, TPad, TH1D
from inspect import currentframe, getframeinfo

f = open("py-fillrandom_via_py.txt","r")
#Line_string = str(f.readline())
#bin_init,_,_ = Line_string.split();   bin_init = float(bin_init)   # get initial bin 

lineList = f.readlines()
Nbin = (len(lineList))     # get number of bins
Line_string = str(lineList[0])
bin_init,_,_ = Line_string.split();  bin_init = float(bin_init)   # get initial bin
Line_string = str(lineList[len(lineList)-1])
_,bin_final,_ = Line_string.split();  bin_final = float(bin_final)   # get final bin
f.seek(0)    # reset python read line


wf = TFile("root_from_txt.root","RECREATE")
hist = TH1D("h1f","h1f",Nbin,bin_init,bin_final)
for i in range(1,Nbin+1):
    Line_string = str(f.readline())
    bin_s,bin_e,bin_c = Line_string.split();
    bin_s = float(bin_s); bin_e = float(bin_e); bin_c = float(bin_c)
    hist.SetBinContent(i,bin_c)

hist.Write()

wf.Close()
