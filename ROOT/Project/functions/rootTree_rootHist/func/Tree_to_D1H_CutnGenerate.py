#Author : JUNHO LEE

from ROOT import TFile, TH1D, TH1F, TCanvas, TColor, TGaxis, TPad, gBenchmark, TTree
import os
import numpy
import collections

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
    FILE = FILENAME.replace(".root","")    #filetxt
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

    filelist = [FILE, FILENAME, filename, filename_NoRoot]
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

    

def Noti():
    print("\n")
    print(" !!!! Please check what kind of component of the tree has by running Tree_to_D1H_Components.py")
    return 

def BreakOrNot(BRANCHLISTEACHTREE):

    print("compenets below :")
    print("\n")
    for i in range(len(BRANCHLISTEACHTREE)):
        print("compenets below :")
        print("The Tree name is : ",BRANCHLISTEACHTREE.keys()[i])
        for j in range(len(BRANCHLISTEACHTREE.values()[i])):
            print("        it contains : ", BRANCHLISTEACHTREE.values()[i][j])
        print("\n")   
 
    print("Have put reasonable CUT ?")
    DETER = raw_input("(Y/N) : ")
    return DETER


def WhetherAddCut(BRANCHLISTEACHTREE):
    Noti()
    deter = BreakOrNot(BRANCHLISTEACHTREE)
    if(deter == "N"):
        return None
    elif((deter == "Y") | (deter == "y") | (deter == "yes") | (deter == "YES") | (deter == "Yes") ):
        return True 
    else: 
        return None







def REGENERATE_TREE_WITH_CUT(filename, outputpath = '.'):

  
    FileNameList = read_file_name(filename)
    BranchListAll = get_branch_list_all(FileNameList[2])
    BranchListEachTree = get_branch_list_each_tree(FileNameList[2])


    DicNumpyArray_branch = {}
    for numpyarray in BranchListAll:
        a = numpy.array([0],'d')
        DicNumpyArray_branch[numpyarray] = a
    DicNumpyArray_branch = collections.OrderedDict(sorted(DicNumpyArray_branch.items()))    #  !!!the input times are ordered!!!
    print(DicNumpyArray_branch)

    DicNumpyArray_branch_w = {}
    for numpyarray_w in BranchListAll:
        a_w = numpy.array([0],'d')
        DicNumpyArray_branch_w[numpyarray_w] = a_w
    DicNumpyArray_branch_w = collections.OrderedDict(sorted(DicNumpyArray_branch_w.items()))
    print(DicNumpyArray_branch_w)


    WCuts = WhetherAddCut(BranchListEachTree)
    if(WCuts==None):
        print("\n")
        print("*********************************************************************************************")
        print("!!!! Please check input CUT !!!!! ")
        print("     !!!! No Output File !!!!    ")
        print("\n")
        for i in range(len(BranchListEachTree)):
            print("compenets below :")
            print("The Tree name is : ",BranchListEachTree.keys()[i])
            for j in range(len(BranchListEachTree.values()[i])):
                print("        it contains : ", BranchListEachTree.values()[i][j])
            print("\n")
        print("!!!! Please check input CUT !!!!! ")
        print("     !!!! No Output File !!!!    ")
        print("*********************************************************************************************")
    else:
        print("\n")
        print("...Cut added and regenerating tree root file...")
        gBenchmark.Start("Regerating tree root")

        f = TFile(FileNameList[2],"READ")
        dirlist = f.GetListOfKeys(); 
        ITER = dirlist.MakeIterator()
        key = ITER.Next()



        if(outputpath == ''):
            outfileName = FileNameList[3] + "/" + FileNameList[0] + "_cut_tree.root"
            outfileName = outfileName.replace("//","/")
#            print("!@#!@!@#!@ ",outfileName)
        elif(outputpath[0] == "/"):
            outfileName = outputpath + "/" + FileNameList[0] + "_cut_tree.root"
            outfileName = outfileName.replace("//","/")
#            print("!@#!@!@#!@ ",outfileName)
        elif(outputpath[0] == "~"):
            outfileName = outputpath.replace("~",os.environ['HOME']) + "/" + FileNameList[0] + "_cut_tree.root"
            outfileName = outfileName.replace("//","/")
#            print("!@#!@!@#!@ ",outfileName)
        else:
            outfileName = os.getcwd() + "/" + outputpath+ "/" + FileNameList[0] + "_cut_tree.root"
            outfileName = outfileName.replace("//","/")
#            print("!@#!@!@#!@ ",outfileName)

        outfile = TFile(outfileName,"RECREATE")

        ijk = 0
        while key:
            tree = key.ReadObj()
            tree_f = TTree(tree.GetName()+"_f",tree.GetName()+"_f")
            ENTRY = tree.GetEntries();  #print(ENTRY)
            for i in range(len(DicNumpyArray_branch)):
                tree.SetBranchAddress(DicNumpyArray_branch.keys()[i],DicNumpyArray_branch.values()[i])  
                tree_f.Branch(DicNumpyArray_branch_w.keys()[i],DicNumpyArray_branch_w.values()[i],DicNumpyArray_branch_w.keys()[i]+"/D")            
            print("for tree", tree.GetName())
            for j in range(ENTRY):
                tree.GetEntry(j)
                if(j%5000 == 0):
                    print("now looping", j, "th Events, total of ", ENTRY, "events")
                for k in range(len(DicNumpyArray_branch)):
                    DicNumpyArray_branch_w.values()[k][0] = DicNumpyArray_branch.values()[k][0]
                if(                                                    #FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME
                    (DicNumpyArray_branch.values()[0][0] < 0.5)          # [i][0]  means "i"th branch of the tree, [0] don't change   #FIXME#FIXME#FIXME#FIXME
                    & (DicNumpyArray_branch.values()[1][0] < 0.5)        #FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME#FIXME
                  ):
                    ijk = ijk + 1
                    tree_f.Fill()
                else:
                    continue
            print(" Event left after filtering : ", ijk, "!!!!!!!!!")
            print("\n")
            ijk=0
            if(tree_f.GetEntries() ==0):
                print("!!!!!!! ", tree_f.GetName()," is Empty, would not be written !!!!!")
            else:
                tree_f.Write()          
 
            key = ITER.Next()


        print("")
        print("////////////////////////////////////////////////")
        print("outputfile : ")
        print(outfileName)
        print("////////////////////////////////////////////////")
        print("")
        
        outfile.Close() 
        f.Close()
        print("*********************************************************************************************")
        gBenchmark.Show("Regerating tree root") 
        print("*********************************************************************************************")

        return outfileName



def main():
    REGENERATE_TREE_WITH_CUT("../../../root_generator/tree/root2_tree.root")


if __name__=="__main__":
    main()

