
from ROOT import TCanvas, TPad, TFormula, TF1, TPaveLabel, TH1F, TFile
from ROOT import gROOT, gBenchmark

c1 = TCanvas("c1,","c1",200, 10 , 700,900)
c1.SetFillColor(18)

pad1 = TPad("pad1","pad1",0.05, 0.50, 0.95, 0.95, 21)
pad2 = TPad("pad2","pad2",0.05, 0.05, 0.95, 0.45, 21)
pad1.Draw()
pad2.Draw()

gBenchmark.Start("fillrandom")

form1 = TFormula("form1","abs(sin(x)/x)")
sqroot = TF1("sqroot","x*gaus(0) + [3]*form1", 0 ,10)
sqroot.SetParameters(10, 4, 1, 20)
#pad1.SetGridx()
pad2.SetGridy()
pad1.SetGrid()
c1.Update()
pad1.cd()
sqroot.Draw()
pad1.Modified(); pad1.Update()

pad2.cd()
pad2.GetFrame().SetFillColor(42)
pad2.GetFrame().SetBorderMode(-1)
pad2.GetFrame().SetBorderSize(5)
h1f = TH1F("h1f","h1f", 200, 0 ,10)
h1f.FillRandom("sqroot",10000)
h1f.Draw()
pad2.Update()

myfile = TFile("py-fillrandom.root", "recreate")
form1.Write()
sqroot.Write()
h1f.Write()
myfile.Close()


gBenchmark.Show("fillrandom")




