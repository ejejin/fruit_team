
from ROOT import TFile, TCanvas, TPad

f1 = TFile("mpy-fillrandom.root", "READ");
#f2 = TFile("txt_180315_ROOT_to_txt.dat","RECREATE")
hist = f1.Get("h1f")
Nbins = hist.GetNbinsX()
#bins = hist.GetBinContent(1)
#print(Nbins,bins)

file1 = open("mroot_to_txe_py.txt","w") # creat a txt file ("w")

for i in range(Nbins):
    bins = hist.GetBinContent(i+1)
    file1.write(str(i+1)+" ")
    file1.write(str(bins)+"\n")


file1.close() 

