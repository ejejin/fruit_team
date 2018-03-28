from ROOT import TFile, TH2D, TH1D, gBenchmark
from Tree_to_D1H_Convert import read_file_name
import collections, numpy
import os

def GetHistoNameList(filename):
    f = TFile(filename,"READ");
    dirlist = f.GetListOfKeys();
    ITER = dirlist.MakeIterator();
    key = ITER.Next();

    LIST = []; jj=0
    while key:
        if key.GetClassName().index("TH1")>-1 :
            FILE = key.ReadObj()
            Name = FILE.GetName()
            LIST.append(Name)
            jj = jj + 1
        key = ITER.Next()
#    print(LIST)
    return LIST

def Find_Loca(histoName):
    LOCA = len(histoName)
    for i in range (1,len(histoName)+1):
        if(histoName[-i] == "_"):
            if((histoName[-i-1]=="f")&(histoName[-i-2]=="_") ):
                LOCA = i-1
                break
            else:
                continue
    return LOCA

def BranchName(histoName):
    Loca = Find_Loca(histoName); #print(Loca)
    BRANCHNAME = histoName.replace(histoName[:-Loca],"")
    return BRANCHNAME


def Exclued_BranchName(histoName):
    Loca = Find_Loca(histoName)
    EXCLUDE_BRANCHNAME = histoName.replace(histoName[len(histoName)-Loca:len(histoName)],"")
    return EXCLUDE_BRANCHNAME


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
    DicNumpyArray_branch = collections.OrderedDict(sorted(DicNumpyArray_branch.items()))    #  !!!the input times are ordered!!!
#    print(DicNumpyArray_branch)

    histo_xrange = {}
    f = TFile(FILENAME, "READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next()

    lowEdge = []
    highEdge = []
    for i in range(len(DicNumpyArray_branch)):
        lowEdge.append(0)
        highEdge.append(0)

    while key:
        tree = key.ReadObj()
        for i in range(len(DicNumpyArray_branch)):
            tree.SetBranchAddress(DicNumpyArray_branch.keys()[i], DicNumpyArray_branch.values()[i])

        tree_xrange = {}
        ENTRY = tree.GetEntries()
#        print("@EEF#$#G!#", len(DicNumpyArray_branch))
        for i in range(ENTRY):                                            #### HISTO RANGE SETTING !!!!
            tree.GetEntry(i)                                              #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME below 
            for j in range(len(DicNumpyArray_branch)):                    #### "j" corresponse to branch for one tree on one loop
                if(i==0):                                                 #### And they are in correct order !!!
                    lowEdge[j] = DicNumpyArray_branch.values()[j][0]        ####### you can set the low & high edge manually #FIXME
                    highEdge[j] = DicNumpyArray_branch.values()[j][0]      #### e.g.  "lowEdge[j] = -10", "highEdge[j] = 10"
                else:                                                       ####### and comment all if, else 
                    if(DicNumpyArray_branch.values()[j][0] < lowEdge[j]):
                        lowEdge[j] = DicNumpyArray_branch.values()[j][0]
                    if(DicNumpyArray_branch.values()[j][0] > highEdge[j]):
                        highEdge[j] = DicNumpyArray_branch.values()[j][0]
#        print(highEdge)
        for k in range(len(DicNumpyArray_branch)):
            lowEdge[k] = lowEdge[k] - (highEdge[k]-lowEdge[k])*0.05         ###### range setting  #FIXME
            highEdge[k] = highEdge[k] + (highEdge[k]-lowEdge[k])*0.05
        for l in range(len(DicNumpyArray_branch)):
            tree_xrange[DicNumpyArray_branch.keys()[l]] = [lowEdge[l], highEdge[l]]

#        print("\n")
        histo_xrange[tree.GetName()] = tree_xrange
        key = ITER.Next()

#    print(histo_xrange)
    return histo_xrange



def Fill_histograms(FILENAME,BRANCHLISTALL,DICHISTLIST):
    gBenchmark.Start("Filling & Writing 2D Histograms")    
    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a
    DicNumpyArray_branch = collections.OrderedDict(sorted(DicNumpyArray_branch.items()))    #  !!!the input times are ordered!!!
#    print(DicNumpyArray_branch)

    f = TFile(FILENAME,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key =  ITER.Next()
    while key:
        tree = key.ReadObj()
        for i in range(len(DicNumpyArray_branch)):
            tree.SetBranchAddress(DicNumpyArray_branch.keys()[i], DicNumpyArray_branch.values()[i])
        ENTRY = tree.GetEntries()
        print("for tree", tree.GetName())
#        print(len(DICHISTLIST[tree.GetName()]))
        print(len(DicNumpyArray_branch))
#        print(len(DICHISTLIST))
        print(DICHISTLIST.keys()[0]); print(DICHISTLIST.values()[0][0].GetName())
#        print(DICHISTLIST.values())
        for i in range(ENTRY):
            tree.GetEntry(i)
            if(i%5000 == 0):
                print("now looping", i, "th Events, total of ", ENTRY, "events")
            for j in range(len(DICHISTLIST)):
                if(tree.GetName() == DICHISTLIST.keys()[j]):
                    for k in range(len(DICHISTLIST.values()[j])):     # 6 rotation for histo
                        jun = 0
                        for jk in range(len(DicNumpyArray_branch)):   # 3 rotation for branch
                            if((DicNumpyArray_branch.keys()[jk] in DICHISTLIST.values()[j][k].GetName()) & (jun==0)):
                                MOMEM1 = DicNumpyArray_branch.keys()[jk] ; JUN1 = jk
                                jun = jun + 1
                            elif((DicNumpyArray_branch.keys()[jk] in DICHISTLIST.values()[j][k].GetName()) & (jun==1)):
                                MOMEM2 = DicNumpyArray_branch.keys()[jk];  JUN2 = jk
                                jun = jun + 1
                            else:
                                continue

                            if(jun==2):
                                if(("X_"+MOMEM1+"_Y_"+MOMEM2) in DICHISTLIST.values()[j][k].GetName()):
                                    DICHISTLIST[tree.GetName()][k].Fill(DicNumpyArray_branch.values()[JUN1][0],DicNumpyArray_branch.values()[JUN2][0])
                                elif(("X_"+MOMEM2+"_Y_"+MOMEM1) in DICHISTLIST.values()[j][k].GetName()):
                                    DICHISTLIST[tree.GetName()][k].Fill(DicNumpyArray_branch.values()[JUN2][0],DicNumpyArray_branch.values()[JUN1][0])

                else:
                    continue

        key = ITER.Next()

    return DICHISTLIST





def CONVERT_WORKING2D(filename, outputpath = "" ):
    FileNameList = read_file_name(filename)
    print(FileNameList)
    BranchListAll = get_branch_list_all(FileNameList[2])
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])
    histo_xrange = set_histo_xrange(FileNameList[2], BranchListAll)

    indicator = 0
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
            branchlistbb = tree.GetListOfBranches() 
            ITER_bb = branchlistbb.MakeIterator()
            key_bb = ITER_bb.Next()
            while key_bb:
                if((key_b.GetName()) != (key_bb.GetName())):
                    Name2DHist = tree.GetName()+"_X_" + BranchName(key_b.GetName()) + "_Y_" + BranchName(key_bb.GetName())
#                    print(Name2DHist)
#                    print(type(histo_xrange[tree.GetName()][key_b.GetName()][0]))
                    hist = TH2D(Name2DHist, Name2DHist, 50, histo_xrange[tree.GetName()][key_b.GetName()][0], histo_xrange[tree.GetName()][key_b.GetName()][1], 50, histo_xrange[tree.GetName()][key_bb.GetName()][0], histo_xrange[tree.GetName()][key_bb.GetName()][1])

                    histList.append(hist)
                    indicator = indicator + 1

                key_bb = ITER_bb.Next()
            key_b = ITER_b.Next()
        DichistList[tree.GetName()] = histList
        key = ITER.Next()

#    print(DichistList)
##    print(indicator)


    dicHistList = Fill_histograms(FileNameList[2], BranchListAll, DichistList)

    if(outputpath == ''):
        Name_Output_File = FileNameList[3] + "/" + FileNameList[0] + "_2Dhist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
    elif(outputpath[0] == "/"):
        Name_Output_File = outputpath + "/"+ FileNameList[0] + "_2Dhist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    elif(outputpath[0] == "~"):
        Name_Output_File = outputpath.replace("~",os.environ['HOME']) +FileNameList[0]+ "_2Dhist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    else:
        Name_Output_File = os.getcwd() + "/" + outputpath+ FileNameList[0]+"_2Dhist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)

#    Name_Output_File = FileNameList[0] + "_2Dhist.root"
    outfile = TFile(Name_Output_File,"RECREATE")

    for i in range(len(dicHistList)):
        for j in range(len(dicHistList.values()[i])):
            dicHistList.values()[i][j].Write()
    print("")
    print("////////////////////////////////////////////////")
    print("outputfile : ")
    print(Name_Output_File)
    print("////////////////////////////////////////////////")
    print("")
    outfile.Close()


    print("*********************************************************************************************")
    gBenchmark.Show("Filling & Writing 2D Histograms")
    print("*********************************************************************************************")

    return Name_Output_File



def main():
    filename = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func/root2_tree_cut_tree.root"
    FileNameList = read_file_name(filename)
    BranchListAll = get_branch_list_all(FileNameList[2]) ; #print(BranchListAll)
    
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2]); #print(BranchListEachTree) 
    histo_xrange = set_histo_xrange(FileNameList[2], BranchListAll); #print(histo_xrange)
    print(CONVERT_WORKING2D(FileNameList[2],""))


if __name__=="__main__":
    main()


