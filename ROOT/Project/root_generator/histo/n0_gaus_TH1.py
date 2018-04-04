
from ROOT import *

outFile = TFile("root0_gaus.root","RECREATE")
hist1 = TH1D("hist1","hist1",100,10,10)
for i in range(5000):
    hist1.Fill(gRandom.Gaus(0,0.3))
hist1.Write()
outFile.Close()




