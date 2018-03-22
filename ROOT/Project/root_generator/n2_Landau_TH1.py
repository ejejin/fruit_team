
from ROOT import *

outFile = TFile("root2_Landau.root","RECREATE")
hist1 = TH1F("hist1","hist1",100, -1, 4)
hist2 = TH1F("hist2","hist2",100, -1, 4)
hist3 = TH1F("hist3","hist3",100, -1, 4)
hist4 = TH1F("hist4","hist4",100, -1, 4)
hist5 = TH1F("hist5","hist5",100, -1, 4)

for i in range(100000):
    hist1.Fill(gRandom.Landau(1,0.10))
    hist2.Fill(gRandom.Landau(1,0.20))
    hist3.Fill(gRandom.Landau(1,0.30))
    hist4.Fill(gRandom.Landau(1,0.40))
    hist5.Fill(gRandom.Landau(1,0.50))
hist1.Write()
hist2.Write()
hist3.Write()
hist4.Write()
hist5.Write()
outFile.Close()
