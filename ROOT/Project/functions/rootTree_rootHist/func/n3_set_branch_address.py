

def showcase_set_branch_address(BRANCHLISTALL, PATH_FILE_NAME):
    from ROOT import TTree, TFile
    import numpy

    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a

    
    f = TFile(PATH_FILE_NAME,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()

    while key:
        tree = key.ReadObj()
        for i in range(len(DicNumpyArray_branch)):
            tree.SetBranchAddress(DicNumpyArray_branch.keys()[i], DicNumpyArray_branch.values()[i])
            #print(DicNumpyArray_branch.keys()[i])
        key = ITER.Next()

    f.Close()
    print("!!! This is just a showcase of SetBranchAddress, not really set !!!")
    return DicNumpyArray_branch


