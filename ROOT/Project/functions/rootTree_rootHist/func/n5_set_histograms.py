
from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad

def set_histograms(FILENAME,S_FILENAME, HISTO_XRANGE, NBins=100):
    f = TFile(FILENAME,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()
    DichistList = {}
#    DichistList = dict()
    while key:
        histList = []
        NamehistList = []
        tree = key.ReadObj()
        branchlist = tree.GetListOfBranches()
        if(branchlist.IsEmpty()):
            continue
        ITER_b = branchlist.MakeIterator()
        key_b = ITER_b.Next()
        while key_b:
            Namehist = S_FILENAME + "_" + tree.GetName() + "_" + key_b.GetName()+"_hist"
#            print(Namehist)
            for j in range(len(HISTO_XRANGE[tree.GetName()])):
                if key_b.GetName() in HISTO_XRANGE[tree.GetName()].keys()[j]:
                     hist = TH1D(Namehist, Namehist, NBins, HISTO_XRANGE[tree.GetName()].values()[j][0], HISTO_XRANGE[tree.GetName()].values()[j][1])
                     histList.append(hist)
                else:
                    continue
            
            key_b = ITER_b.Next()
        DichistList[tree.GetName()] = histList
        key = ITER.Next()
    
    print (DichistList)
    return DichistList



def test(DicHistList):
    print(DicHistList)


