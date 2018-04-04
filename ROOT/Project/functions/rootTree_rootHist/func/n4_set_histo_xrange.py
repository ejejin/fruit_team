



def set_histo_xrange(FILENAME,BRANCHLISTALL):
    from ROOT import TFile
    import numpy

    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a

    histo_xrange = {}
    f = TFile(FILENAME, "READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()

    lowEdge = [0,0,0]
    highEdge = [0,0,0]
    while key:
        tree = key.ReadObj()
        for i in range(len(DicNumpyArray_branch)):
            tree.SetBranchAddress(DicNumpyArray_branch.keys()[i], DicNumpyArray_branch.values()[i])

        tree_xrange = {}
        ENTRY = tree.GetEntries()
        for i in range(ENTRY):
            tree.GetEntry(i)
            for j in range(len(DicNumpyArray_branch)):
                if(i==0):
                    lowEdge[j] = DicNumpyArray_branch.values()[j][0]
                    highEdge[j] = DicNumpyArray_branch.values()[j][0]
                else:
                    if(DicNumpyArray_branch.values()[j][0] < lowEdge[j]):
                        lowEdge[j] = DicNumpyArray_branch.values()[j][0]
                    if(DicNumpyArray_branch.values()[j][0] > highEdge[j]):
                        highEdge[j] = DicNumpyArray_branch.values()[j][0]
#        print(highEdge,lowEdge)
        for k in range(len(DicNumpyArray_branch)):
            lowEdge[k] = lowEdge[k] - (highEdge[k]-lowEdge[k])*0.1
            highEdge[k] = highEdge[k] + (highEdge[k]-lowEdge[k])*0.1
        for l in range(len(DicNumpyArray_branch)):
            tree_xrange[DicNumpyArray_branch.keys()[l]] = [lowEdge[l], highEdge[l]]
        
#        print("\n")
        histo_xrange[tree.GetName()] = tree_xrange
        key = ITER.Next()

#    print(histo_xrange)
    return histo_xrange





