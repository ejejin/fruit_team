
NBins = 100

from ROOT import TFile, TH1F, TH1D, TTree
import numpy

infile = TFile("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root","READ")
outfile = TFile("outfile_please_modify_correspondingly_test3.root","RECREATE")

t1 = infile.Get("tree1")   # check the tree name and input...
#t2 = infile.Get("tree2")   # check the tree name and input...

px = numpy.array([0],'d')
py = numpy.array([0],'d')
pz = numpy.array([0],'d')
content_list = {}
content_list["px"]=px
content_list["py"]=py
content_list["pz"]=pz
#print(content_list)            ######### directionary dosen't add element in the order of input
#print(len(content_list))
#print(content_list.keys())
#print(content_list.keys()[0]); print(type(content_list.keys()[0]));
#print(content_list.values()[0]); 
#print(type(content_list.values()[1][0]))

for i in range(len(content_list)):
    t1.SetBranchAddress(content_list.keys()[i],content_list.values()[i])
#    print(content_list.keys()[i])
#    print(content_list.values()[i])

ENUM = t1.GetEntries()
lowEdge, highEdge = 0,0
for i in range(ENUM):
    t1.GetEntry(i)
#    if(i<3):
#        print(content_list.values()[1][0])
    if(i==0):
        lowEdge = content_list.values()[1][0]
        highEdge = content_list.values()[1][0]
    if(content_list.values()[1][0] < lowEdge):
        lowEdge = content_list.values()[1][0]
    if(content_list.values()[1][0] > highEdge):
        highEdge = content_list.values()[1][0]

#print(lowEdge);print(highEdge)
lowEdge = lowEdge - (highEdge-lowEdge)*0.1
highEdge = highEdge + (highEdge-lowEdge)*0.1
#print(lowEdge);print(highEdge)


hist1 = TH1F("hist1","hist1", 100, lowEdge, highEdge)
for i in range(ENUM):
    t1.GetEntry(i)
###### you can put condition here
    hist1.Fill(content_list.values()[1][0])
#    if(i<3):
#        print(content_list.values()); print(type(content_list.values()[1][0]))

hist1.Write()
infile.Close()
outfile.Close()














