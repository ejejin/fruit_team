
from ROOT import *

outFile = TFile("root1_gaus.root","RECREATE")
hist1 = TH1D("hist1","hist1",100,10,10)
hist2 = TH1D("hist2","hist2",100,-10,10)
for i in range(10000):
    hist1.Fill(gRandom.Gaus(0,3))
    hist2.Fill(gRandom.Gaus(-1,4))
hist1.Write()
hist2.Write()
outFile.Close()


# read file 
readFile = TFile("root1_gaus.root","READ")
dirlist = readFile.GetListOfKeys();  # print(type(dirlist))
ITER = dirlist.MakeIterator();       # print(type(ITER))
key = ITER.Next();                   # print(type(key))
LIST = []

td = None
jj = 0

while key:
    if ((key.GetClassName()).index("TH1") > -1):
        td = key.ReadObj()
        Name = td.GetName()
        print("name of content", Name)
        LIST.append(Name)
        jj = jj + 1
    key = ITER.Next()
print(LIST)



