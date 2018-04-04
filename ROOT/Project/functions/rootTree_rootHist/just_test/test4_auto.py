IBin = -2.0
FBin = 2.0
NBins = 100

from ROOT import TFile, TH1F, TH1D, TTree
import numpy

filename = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/root_generator/tree/root2_tree.root"
f = TFile(filename,"READ")
outfile = TFile("outfile_please_modify_correspondingly_test4.root","RECREATE")

if(filename[0]=="/"):
    filename = filename
else:
    filename = os.getcwd() + "/" + filename   # get the path included filename
loca=len(filename)
for i in range (1,len(filename)+1):       # find the "/" location
    if(filename[-i] == "/"):
        loca = i-1
        break

FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten input filename, excluded path 
print(FILENAME)



############################################## Getting Name list and Dictionary

DirTreeBranchNameList = {}
SetBranchNameList = set()
dirlist = f.GetListOfKeys()
#dirlist.Print(); #print(dirlist.GetSize())
ITER = dirlist.MakeIterator()
key = ITER.Next()
#key.Print(); print(key.GetName())
while key:
    BranchNameList = []
    tree = key.ReadObj()
#    print(tree.GetName())
    branchlist = tree.GetListOfBranches()
    if(branchlist.IsEmpty()):
        continue
    ITER_b = branchlist.MakeIterator() 
    key_b = ITER_b.Next() 
    while key_b:
        BranchNameList.append(key_b.GetName())
        SetBranchNameList.add(key_b.GetName())
#        print(key_b.GetName())
        key_b = ITER_b.Next()
    DirTreeBranchNameList[tree.GetName()] = BranchNameList
    key = ITER.Next()

#print(DirTreeBranchNameList)     # seperate branch of each tree
#print(SetBranchNameList)         # take advantage of no double element in set, define branch variables
#############################################################




################## prepare for SetBranchAddress for each tree. variables definiton for branch    ###########    

DirNumpyArray_branch = {}
for NumpyArray in SetBranchNameList:                ## prepare for SetBranchAddress for each tree. variables definiton for branch
#    print(NumpyArray); print(type(NumpyArray))
    a = numpy.array([0],'d')
    DirNumpyArray_branch[NumpyArray] = a                  
#print(type(DirNumpyArray_branch.values()[1][0])) 
#print(DirNumpyArray_branch)              
#############################################################



##########Need to get into tree again, for each tree, do SetBranchAddress(), Setting histograms for each branch!!!  ## below ::
dirlist = f.GetListOfKeys()
ITER = dirlist.MakeIterator()
key = ITER.Next()
DirhistList = {}                     ##### histolist for each tree
while key:
    histList = []
    NamehistList = []
    tree = key.ReadObj()
    for i in range(len(DirNumpyArray_branch)):
        tree.SetBranchAddress(DirNumpyArray_branch.keys()[i],DirNumpyArray_branch.values()[i])          #### SetBranchAddress of every branch for each tree
    branchlist = tree.GetListOfBranches()
    if(branchlist.IsEmpty()):
        continue
    ITER_b = branchlist.MakeIterator()
    key_b = ITER_b.Next()
    while key_b:
        ENTRY = tree.GetEntries() 
        Namehist = FILENAME.replace(".root","") + "_" + tree.GetName() + "_" + key_b.GetName()+"_hist"
        NamehistList.append(Namehist)
        hist = TH1D(Namehist, Namehist, NBins, IBin, FBin)
        histList.append(hist)
        KEY_B = key_b.GetName()
        key_b = ITER_b.Next()

    for i in range(ENTRY):
        tree.GetEntry(i)
        for j in range(len(histList)):
#            histList[j].Fill(DirNumpyArray_branch.values()[j][0])
            for k in range(len(histList)):
                if DirNumpyArray_branch.keys()[j] in histList[k].GetName():
                    histList[k].Fill(DirNumpyArray_branch.values()[j][0])
                else :
                    continue
    for i in range(len(histList)):
        histList[i].Write()         
#    print("\n")

    DirhistList[tree.GetName()] = histList
    key = ITER.Next()
#print(DirhistList)
#print(DirNumpyArray_branch)
################################################################

outfile.Close()

