
from ROOT import TFile, TTree
import numpy

filename = "/Users/leejunho/Desktop/git/python3Env/group_study/fruit_team/ROOT/Project/tranfer_test/data/concrete.txt"
f = open(filename,"r")

if(filename[0]=="/"):
    filename = filename
else:
    filename = os.getcwd() + "/" + filename   # get the path included filename
loca=len(filename)
for i in range (1,len(filename)+1):       # find the "/" location
    if(filename[-i] == "/"):
        loca = i-1
        break

FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename, excluded path 
Filename = FILENAME.replace(".txt","")
#print(FILENAME); print(Filename)

outName = Filename + "_tree.root"
outFile = TFile(outName,"RECREATE")
tree = TTree(Filename,Filename)

Firstline = f.readline()

LL = []
if(Firstline[-1] == "\n"):
    Firstline = Firstline.replace("\n","")
    LL = Firstline.split()
#    print(Firstline)
#print(Firstline)
#print(LL)
#print(len(LL))

List_branch = []
for branch in LL:
    branch = numpy.zeros(1, dtype=float)
    List_branch.append(branch)

#print(List_branch)
for i in range(len(List_branch)):
    tree.Branch(LL[i],List_branch[i],LL[i]+"/D")

#iii = 0
for line in f:
    LL1 = []
    LL1 = line.split()
#    print(LL1)
    for j in range(len(LL1)):
        List_branch[j][0] = float(LL1[j])
#        print(List_branch[j][0])
#    iii= iii+1
#    if(iii==3):
#        break
    tree.Fill()




tree.Write()
outFile.Close()
f.close()
 
