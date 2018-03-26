NBins =  100         # total bin number
IBin =   -10         # lower edge of X-axis
FBin =   10          # higher edge of X-axis

from ROOT import TFile, TH1F, TH1D, TTree
import numpy

infile = TFile("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root","READ")  # Correctly input file name
outfile = TFile("outfile_please_modify_correspondingly_test1.root","RECREATE")    ### name of output file, please modify correspondingly  !!!!!
t1 = infile.Get("tree1")   # check the tree name and input...
t2 = infile.Get("tree2")   # check the tree name and input...

px = numpy.array([0],'d')
py = numpy.array([0],'d')
pz = numpy.array([0],'d')

t1.SetBranchAddress("px",px)       # SetBranchAddress for each tree
t1.SetBranchAddress("py",py)
t1.SetBranchAddress("pz",pz)

t2.SetBranchAddress("px",px)       # SetBranchAddress for each tree
t2.SetBranchAddress("py",py)
t2.SetBranchAddress("pz",pz)

hist1 = TH1F("hist1","hist1", NBins, IBin, FBin)      # define 1D histogram
hist2 = TH1F("hist2","hist2", NBins, IBin, FBin)
hist3 = TH1F("hist3","hist3", NBins, IBin, FBin)

ENUM = t1.GetEntries()
for i in range(ENUM):
    t1.GetEntry(i)
    if((px[0] >-1) & (py[0]>0.5) & (pz[0]<3.) ):
        hist1.Fill(px[0])
    else: 
        continue

ENUM = t2.GetEntries()
for i in range(ENUM):
    t2.GetEntry(i)
    if((px[0]<-0.1) & (py[0]<0.5) & (pz[0]<2)): 
        hist2.Fill(py[0])
    else:
        continue  

ENUM = t2.GetEntries()
for i in range(ENUM):
    t2.GetEntry(i)
    if((px[0]<-0.1) & (py[0]<0.5) & (pz[0]<2)):
        hist3.Fill(pz[0])
    else:
        continue

hist1.Write()
hist2.Write()
hist3.Write()
outfile.Close()




