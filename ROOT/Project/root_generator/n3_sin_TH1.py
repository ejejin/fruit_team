
from ROOT import *

outFile = TFile("root3_sin.root","RECREATE")
hist1 = TH1D("hist1","hist1",100,-10,10)
hist2 = TH1F("hist2","hist2",100,-10,10)
hist3 = TH1D("hist3","hist3",100,-10,10)

f1 = TF1("f1","x*sin(x)*exp(-0.1*x)+15",-10.,10.)
f2 = TF1("f2","(sin(x)+cos(x))**5+15",-10.,10.)
f3 = TF1("f3","(sin(x)/(x)-x*cos(x))+15",-10.,10.)

hist1.FillRandom("f1",100000)
hist2.FillRandom("f2",100000)
hist3.FillRandom("f3",100000)

hist1.Write()
hist2.Write()
hist3.Write()
outFile.Close()

