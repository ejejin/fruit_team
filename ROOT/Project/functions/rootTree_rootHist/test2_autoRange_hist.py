

from ROOT import TFile, TH1F, TH1D, TTree
import numpy

infile = TFile("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root","READ")
outfile = TFile("outfile_please_modify_correspondingly_test2.root","RECREATE")

t1 = infile.Get("tree1")

px = numpy.array([0],'d')
py = numpy.array([0],'d')
pz = numpy.array([0],'d')

t1.SetBranchAddress("px",px)       # SetBranchAddress for each tree
t1.SetBranchAddress("py",py)
t1.SetBranchAddress("pz",pz)

ENUM = t1.GetEntries()
#print(ENUM)
for i in range(ENUM):
    t1.GetEntry(i)
#### you can put condition here
#    if(i<3):
#        print(px[0])
    if(i==0):
        lowEdge = px[0]
        highEdge = px[0]
    if(px[0] < lowEdge):
        lowEdge = px[0]
    if(px[0] > highEdge):
        highEdge = px[0]

print(lowEdge);print(highEdge)
lowEdge = lowEdge - (highEdge-lowEdge)*0.1
highEdge = highEdge + (highEdge-lowEdge)*0.1
print(lowEdge);print(highEdge)

hist1 = TH1F("hist1","hist1", 100, lowEdge, highEdge)
for i in range(ENUM):
###### you can put condition here
    t1.GetEntry(i)
    hist1.Fill(px[0])

hist1.Write()
infile.Close()
outfile.Close()

