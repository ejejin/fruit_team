from ROOT import TFile, TCanvas, TPad, TH1D, TLatex, TStyle, gStyle, TText, gPad, TNtuple
from inspect import currentframe, getframeinfo

can = TCanvas("can","can",200,10,700,700);
#pad = TPad("pad","pad",0,0,1,1)
#can.cd(pad)
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

hist = TH1D("h1f","h1f",Nbin,bin_init,bin_final)
ntuple = TNtuple("ntuple","ntuple","low_bin:high_bin:bin_contents")
total_e = 0
for i in range(1,Nbin+1):
    Line_string = str(f.readline())
    ss,ff,bin_c = Line_string.split();  
    ss = float(ss); ff = float(ff)
    bin_c = float(bin_c)
    hist.SetBinContent(i,bin_c)
    total_e = total_e + bin_c
    ntuple.Fill(ss,ff,bin_c)
#gStyle.SetOptStat()
hist.Draw()
gPad.Update()
can.Update()



wf = TFile("root_ntuple_from_txt.root","RECREATE")
hist.Write()
ntuple.Write()
wf.Close()
