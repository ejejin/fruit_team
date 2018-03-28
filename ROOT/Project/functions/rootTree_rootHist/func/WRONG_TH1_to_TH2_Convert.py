from ROOT import TFile, TH2D
from Tree_to_D1H_Convert import read_file_name

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

def TH1_to_TH2_Convert(filename, outputpath=''):
    FILELIST = read_file_name(filename)
    fn = FILELIST[0]; print(fn)
    histo_name_list = GetHistoNameList(filename); print(histo_name_list)
#    print(BranchName(histo_name_list[0]))
#    print Exclued_BranchName(histo_name_list[0])

    indicator = 0
    histList = []
    f = TFile(filename,"READ")
    dirlist = f.GetListOfKeys()
    ITER = dirlist.MakeIterator()
    key = ITER.Next(); #print(key.GetName())
    while key:
        dirlistb = f.GetListOfKeys()
        ITERb = dirlistb.MakeIterator()
        keyb = ITERb.Next()
        ijk = 0
        while keyb:
            if(Exclued_BranchName(key.GetName()) == Exclued_BranchName(keyb.GetName())):
                if(key.GetName() != keyb.GetName()):
                    Name2DHist = Exclued_BranchName(key.GetName()) + "Y_" + BranchName(key.GetName()) + "_X_" + BranchName(keyb.GetName()) 
                    
#                    hist = TH2D
                    print(Name2DHist)                   
                    indicator = indicator + 1
                    
            keyb = ITERb.Next()
        key = ITER.Next()

    print(indicator)





def main():
    filelist = read_file_name("/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/functions/rootTree_rootHist/func/root2_tree_cut_tree_hist.root")

#    print(filelist[2])
    TH1_to_TH2_Convert(filelist[2],".")


if __name__=="__main__":
    main()

