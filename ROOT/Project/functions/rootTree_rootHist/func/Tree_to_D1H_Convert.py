#Author : Junho Lee
from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad, gBenchmark
import os
import numpy
import collections
#from n6_Fill_histograms import Fill_histograms

def read_file_name(filename):             # returning [filename, filename.root, absolute path filename, absolute path filename without root file]
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
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

    filelist = [FILE, FILENAME, filename, filename_NoRoot]
#    print(filelist)
    f.Close()
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
    f.Close()
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
    f.Close()
    return DicTreeBranchNameList



def set_histo_xrange(FILENAME,BRANCHLISTALL,BranchListEachTree):
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
            if(list(DicNumpyArray_branch.keys())[i] in BranchListEachTree[tree.GetName()]):
                tree.SetBranchAddress(list(DicNumpyArray_branch.keys())[i],list(DicNumpyArray_branch.values())[i])
            else:
                continue
            tree.SetBranchAddress(list(DicNumpyArray_branch.keys())[i], list(DicNumpyArray_branch.values())[i])

        tree_xrange = {}
        ENTRY = tree.GetEntries()
#        print("@EEF#$#G!#", len(DicNumpyArray_branch))
        for i in range(ENTRY):                                            #### HISTO RANGE SETTING !!!!
            tree.GetEntry(i)                                              #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME below 
            for j in range(len(DicNumpyArray_branch)):                    #### "j" corresponse to branch for one tree on one loop
                if(list(DicNumpyArray_branch.keys())[j] in BranchListEachTree[tree.GetName()]):
                    pass
                else:
                    continue
                if(i==0):                                                 #### And they are in correct order !!!
                    lowEdge[j] = list(DicNumpyArray_branch.values())[j][0]        ####### you can set the low & high edge manually #FIXME
                    highEdge[j] = list(DicNumpyArray_branch.values())[j][0]      #### e.g.  "lowEdge[j] = -10", "highEdge[j] = 10"
                else:                                                       ####### and comment all if, else 
                    if(list(DicNumpyArray_branch.values())[j][0] < lowEdge[j]):
                        lowEdge[j] = list(DicNumpyArray_branch.values())[j][0]
                    if(list(DicNumpyArray_branch.values())[j][0] > highEdge[j]):
                        highEdge[j] = list(DicNumpyArray_branch.values())[j][0]
#        print("!!!!!",highEdge)
        for k in range(len(DicNumpyArray_branch)):
            if(list(DicNumpyArray_branch.keys())[k] in BranchListEachTree[tree.GetName()]):
                pass
            else:
                continue
            lowEdge[k] = lowEdge[k] - (highEdge[k]-lowEdge[k])*0.05         ###### range setting  #FIXME
            highEdge[k] = highEdge[k] + (highEdge[k]-lowEdge[k])*0.05      
        for l in range(len(DicNumpyArray_branch)):
            if(list(DicNumpyArray_branch.keys())[l] in BranchListEachTree[tree.GetName()]):
                pass
            else:
                continue
            tree_xrange[list(DicNumpyArray_branch.keys())[l]] = [lowEdge[l], highEdge[l]]

#        print("\n")
        histo_xrange[tree.GetName()] = tree_xrange
        key = ITER.Next()

#    print(histo_xrange)
    f.Close()
    return histo_xrange




def Fill_histograms(FILENAME,BRANCHLISTALL,DICHISTLIST, BranchListEachTree):
    gBenchmark.Start("Filling & Writing Histograms")
#    print("!@#!@#!#",DICHISTLIST.keys())
#    print("!@#!@#!",BRANCHLISTALL)
    DicNumpyArray_branch = {}
    for numpyarray in BRANCHLISTALL:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a
    DicNumpyArray_branch = collections.OrderedDict(sorted(DicNumpyArray_branch.items()))    #  !!!the input times are ordered!!!
#    print("!@#!@#!#",DicNumpyArray_branch)

    f = TFile(FILENAME,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key =  ITER.Next()
    while key:
        it = 0
        tree = key.ReadObj()
#        print("!@#!@#!#",DICHISTLIST[tree.GetName()])
        for i in range(len(DicNumpyArray_branch)):
            if(list(DicNumpyArray_branch.keys())[i] in BranchListEachTree[tree.GetName()]):
                it = it + 1
                pass
            else:
                continue
            tree.SetBranchAddress(list(DicNumpyArray_branch.keys())[i], list(DicNumpyArray_branch.values())[i])
        
        if(it==0):
            continue

        ENTRY = tree.GetEntries()
        print("for tree", tree.GetName())
        for i in range(ENTRY):
            tree.GetEntry(i)
            if(i%1000 == 0):
                print("now looping", i, "th Events, total of ", ENTRY, "events")
            
#            for j in range(len(DICHISTLIST[tree.GetName()])):
            for j in range(len(DicNumpyArray_branch)):
                for k in range(len(DICHISTLIST[tree.GetName()])):
                    if(list(DicNumpyArray_branch.keys())[j] in DICHISTLIST[tree.GetName()][k].GetName()):
                        DICHISTLIST[tree.GetName()][k].Fill(list(DicNumpyArray_branch.values())[j][0])
                    else:
                        continue

#DICHISTLIST[tree.GetName()][k].Scale(DicNumpyArray_branch["JWeight"][j][0])


        key = ITER.Next()
#    print(DICHISTLIST)
#    gBenchmark.Show("filling")
    f.Close()
    return DICHISTLIST



################################## main code #########################

def CONVERT_WORKING(filename, outputpath = "" ):


    FileNameList = read_file_name(filename)
    print(FileNameList)
    BranchListAll = get_branch_list_all(FileNameList[2])
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])
    histo_xrange = set_histo_xrange(FileNameList[2], BranchListAll,BranchListEachTree)

#    print(BranchListEachTree)
  
 
    IJK = 0     # number of all element included in all tree.
    for i in range(len(BranchListEachTree.keys())):
        Tlist = (BranchListEachTree.keys())
        for j in range(len(BranchListEachTree[list(Tlist)[i]])):
            IJK = IJK +1 
#    print(IJK)

    NBins = []                      ### here you can enter the bin numbers of each!!!!!
    for ii in range(IJK):
        NBins.append(10)

#    print("NBins =", NBins)
#    NBins = [,,,,,]      #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME #FIXME 
#    NBins = [40,40,40,40,40]  #!!!!!for soomin

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
            Namehist = FileNameList[0] + "_"+ tree.GetName() + "_" + key_b.GetName()
            ijk = 0
            for j in range(len(histo_xrange[tree.GetName()])):
#                if key_b.GetName() in histo_xrange[tree.GetName()].keys()[j]:    ##### This is initally problem causing line... Keep this line
                if key_b.GetName() == list(histo_xrange[tree.GetName()].keys())[j]:    #### problem causing ### FIXME 
                     hist = TH1D(Namehist, Namehist, NBins[ijk], list(histo_xrange[tree.GetName()].values())[j][0], list(histo_xrange[tree.GetName()].values())[j][1])
                     histList.append(hist)
                     ijk = ijk + 1
                else:
                    continue

            key_b = ITER_b.Next()
        DichistList[tree.GetName()] = histList
        key = ITER.Next()

    dicHistList =  Fill_histograms(FileNameList[2], BranchListAll, DichistList, BranchListEachTree)

    if(outputpath == ''):
        Name_Output_File = FileNameList[3] + "/" + FileNameList[0] + "_hist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
    elif(outputpath[0] == "/"):
        Name_Output_File = outputpath + "/"+ FileNameList[0] + "_hist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    elif(outputpath[0] == "~"):
        Name_Output_File = outputpath.replace("~",os.environ['HOME']) +FileNameList[0]+ "_hist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)
    else:
        Name_Output_File = os.getcwd() + "/" + outputpath+ FileNameList[0]+"_hist.root"
        Name_Output_File = Name_Output_File.replace("//","/")
#        print("!@#!@!@#!@ ",Name_Output_File)

#    Name_Output_File = FileNameList[0] + "_hist.root"
    outfile = TFile(Name_Output_File,"RECREATE")

    for i in range(len(dicHistList)):
        for j in range(len(list(dicHistList.values())[i])):
            list(dicHistList.values())[i][j].Write()
#            dicHistList.values()[i][j].Print()
    print("")
    print("////////////////////////////////////////////////")
    print("outputfile : ")
    print(Name_Output_File)
    print("////////////////////////////////////////////////")
    print("")
    outfile.Close()

    print("*********************************************************************************************")
    gBenchmark.Show("Filling & Writing Histograms")
    print("*********************************************************************************************")

    print("NBins =", NBins)
    print("\n")
    f.Close()
    return Name_Output_File


#############################################################################

def main():
    CONVERT_WORKING("root2_tree_cut_tree.root")


if __name__=="__main__":
    main()


