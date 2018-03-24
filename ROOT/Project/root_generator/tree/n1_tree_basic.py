
from ROOT import *
import numpy

File = TFile("root1_tree.root","RECREATE")
tree = TTree("tree","tree")

px = numpy.zeros(1, dtype=float)
py = numpy.zeros(1, dtype=float)
pz = numpy.zeros(1, dtype=float)
#print(px); print(py)

tree.Branch("px",px,"px/D")
tree.Branch("py",py,"py/D")
tree.Branch("pz",pz,"pz/D")

for i in range(10000):
    px[0] = gRandom.Gaus(0,1)
    py[0] = gRandom.Uniform()
    pz[0] = px*px
    tree.Fill()

tree.Write()
File.Close()



