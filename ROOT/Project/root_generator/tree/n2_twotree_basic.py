
from ROOT import *
import numpy

File = TFile("root2_tree.root","RECREATE")
tree1 = TTree("tree1","tree1")
tree2 = TTree("tree2","tree2")

px = numpy.zeros(1, dtype=float)
py = numpy.zeros(1, dtype=float)
pz = numpy.zeros(1, dtype=float)
#print(px); print(py)

tree1.Branch("px",px,"px/D"); tree2.Branch("px",px,"px/D");
tree1.Branch("py",py,"py/D"); tree2.Branch("py",py,"py/D");
tree1.Branch("pz",pz,"pz/D"); tree2.Branch("pz",pz,"pz/D");


for i in range(10000):
    px[0] = gRandom.Gaus(0,1)
    py[0] = gRandom.Uniform()
    pz[0] = px*px
    tree1.Fill()

for i in range(10000):
    px[0] = gRandom.Gaus(0.1,1.1)
    py[0] = gRandom.Uniform()
    pz[0] = px*py
    tree2.Fill()

tree1.Write()
tree2.Write()
File.Close()



