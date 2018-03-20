from ROOT import TFile, TCanvas, TPad, TH1D, TLatex, TStyle, gStyle, TText, gPad, TPaveText
from inspect import currentframe, getframeinfo

#gStyle.SetOptStat(0)
can = TCanvas("can","can",200,10,500,500);
#pad = TPad("pad","pad",0,0,1,1)
#can.cd(pad)
f = open("py-fillrandom_via_py.txt","r")
#f = open("py-fillrandom_via_py2.txt","r")
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
total_e = 0
for i in range(1,Nbin+1):
    Line_string = str(f.readline())
    _,_,bin_c = Line_string.split();
    bin_c = float(bin_c)
    hist.SetBinContent(i,bin_c)
    total_e = total_e + bin_c
total_e = int(total_e)
hist.Draw()
print(hist.GetMaximumBin())
text = TText(hist.GetXaxis().GetBinCenter(2), hist.GetYaxis().GetBinCenter(1), "Recycled. Total Entry : %i" %total_e)
text.SetTextFont(10)
text.Draw()
gPad.Update()
can.Update()

'''
pave1 = TPaveText(0.1,0.1,0.9,0.98); 
pave1.SetFillColor(42);
pave1.AddText("Recycled")
pave1.Draw()
gPad.Update()
can.Update()
'''

'''
 ## I have tried to modified and upload the stats box, but failed.. is this differenct from C++??
#ps = can.GetPrimitive("stats")     # TPaveStats
ps = hist.FindObject("stats")
listOfLines = ps.GetListOfLines();  #TList
print(type(listOfLines)); listOfLines.Print(); print('\n')
tconst = ps.GetLineWith("Entries")  #TLatex 
listOfLines.Remove(tconst)
listOfLines.Print()
listOfLines = ps.GetListOfLines(); listOfLines.Print();
#ps.Draw()
hist.Draw()
can.cd(2)
hist1 = hist.Clone()
hist1.Draw()
myt = TLatex(0,0,"Entries");
myt.SetTextFont(42)
myt.SetTextSize(0.04)
myt.SetTextColor(0)
listOfLines.Add(myt)
print()
listOfLines.Print()
hist.Draw()
gPad.Update()
can.Modified()
can.Update()
'''


wf = TFile("root_from_txt2.root","RECREATE")
hist.Write()
wf.Close()
