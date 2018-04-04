
from ROOT import TFile, TH1D, TH1F
import numpy

def Fill_histograms(FILENAME,BRANCHLISTALL,DICHISTLIST):
    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a

    f = TFile(FILENAME,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key =  ITER.Next()
    while key:
        tree = key.ReadObj()
        for i in range(len(DicNumpyArray_branch)):
            tree.SetBranchAddress(DicNumpyArray_branch.keys()[i], DicNumpyArray_branch.values()[i])
        ENTRY = tree.GetEntries()
        for i in range(ENTRY):
            tree.GetEntry(i)
            for j in range(len(DICHISTLIST[tree.GetName()])):
                for k in range(len(DICHISTLIST[tree.GetName()])):
                    if(DicNumpyArray_branch.keys()[j] in DICHISTLIST[tree.GetName()][k].GetName()):
                        DICHISTLIST[tree.GetName()][k].Fill(DicNumpyArray_branch.values()[j][0])
                    else:
                        continue

        key = ITER.Next()
#    print(DICHISTLIST)
       
    return DICHISTLIST
