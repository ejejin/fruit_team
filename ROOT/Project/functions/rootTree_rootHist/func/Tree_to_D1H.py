
from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad
import os
import numpy
#from n6_Fill_histograms import Fill_histograms

def read_file_name(filename):             # returning [filename, filename.root, absolute path filename]
    f = TFile(filename,"READ")

    if(filename[0] == '/'):                 # 'filename' of absoulte location 
        filename = filename
    elif(filename[0] == '~'):
        filename = filename.replace("~",os.environ['HOME'])
    else:
        filename = os.getcwd() + "/" + filename

    loca = len(filename)
    for i in range(1,len(filename)+1):       # find the "/" location
        if(filename[-i] == '/'):
            loca = i-1
            break
    FILENAME = filename.replace(filename[:-loca],"")
    FILE = FILENAME.replace(".root","")

    filelist = [FILE, FILENAME, filename]
    return(filelist)


def get_branch_list_all(PATH_included_root):
    from ROOT import TTree, TFile

    SetBranchNameList = set()               # make a set of branchNameList
    f = TFile(PATH_included_root,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()

    while key:
        tree = key.ReadObj()
        branchlist = tree.GetListOfBranches()
        if(branchlist.IsEmpty()):
            continue

        ITER_b = branchlist.MakeIterator()
        key_b = ITER_b.Next()
        while key_b:
            SetBranchNameList.add(key_b.GetName())
            key_b = ITER_b.Next()
        key = ITER.Next()

    return SetBranchNameList



def get_branch_list_each_tree(PATH_included_root):
    from ROOT import TTree, TFile

    DicTreeBranchNameList = {}

    f = TFile(PATH_included_root,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()

    while key:
        BranchNameList = []
        tree = key.ReadObj()
        branchlist = tree.GetListOfBranches()
        if(branchlist.IsEmpty()):
            continue

        ITER_b = branchlist.MakeIterator()
        key_b = ITER_b.Next()
        while key_b:
            BranchNameList.append(key_b.GetName())
            key_b = ITER_b.Next()
        DicTreeBranchNameList[tree.GetName()] = BranchNameList
        key = ITER.Next()

    return DicTreeBranchNameList



def set_histo_xrange(FILENAME,BRANCHLISTALL):
    from ROOT import TFile
    import numpy

    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a
#    print(DicNumpyArray_branch)

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
#        print(highEdge)
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





def main():
    FileNameList = read_file_name("../../../root_generator/tree/root2_tree.root")
    BranchListAll = get_branch_list_all(FileNameList[2])
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])
    histo_xrange = set_histo_xrange(FileNameList[2], BranchListAll)

    NBins = 100
    f = TFile(FileNameList[2],"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()
    DichistList = {}
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
            Namehist = FileNameList[0] + "_" + tree.GetName() + "_" + key_b.GetName()
#            print(Namehist)
            for j in range(len(histo_xrange[tree.GetName()])):
                if key_b.GetName() in histo_xrange[tree.GetName()].keys()[j]:
                     hist = TH1D(Namehist, Namehist, NBins, histo_xrange[tree.GetName()].values()[j][0], histo_xrange[tree.GetName()].values()[j][1])
                     histList.append(hist)
                else:
                    continue

            key_b = ITER_b.Next()
        DichistList[tree.GetName()] = histList
        key = ITER.Next()

#    print (DichistList)

    dicHistList =  Fill_histograms(FileNameList[2], BranchListAll, DichistList)
#    print(dicHistList)

    Name_Output_File = FileNameList[0] + "_hist.root"
    outfile = TFile(Name_Output_File,"RECREATE")
    for i in range(len(dicHistList)):
        for j in range(len(dicHistList.values()[i])):
            dicHistList.values()[i][j].Write()

    print(Name_Output_File)
    outfile.Close()



if __name__=="__main__":
    main()


