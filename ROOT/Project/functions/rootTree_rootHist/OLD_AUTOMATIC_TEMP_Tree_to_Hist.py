
def T_to_H(filename, outputpath = '', NBins=100, IBin=-10, FBin=10):
    from ROOT import TFile, TCanvas, TPad, TH1D, TH1F
    import os
    import numpy

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
#    print(filename)   # path included file name
#    print(FILENAME)   # file name only

    if(outputpath==''):
        pass
    else:
        if(outputpath[0] == "/"):
            filetxt = outputpath+ "/" + FILENAME.replace(".root","")
            filetxt = filetxt.replace("//","/")
        elif(outputpath[0] == "~"):
            filetxt = outputpath.replace("~",os.environ['HOME']) + "/" + FILENAME.replace(".root","")
            filetxt = filetxt.replace("//","/")
        else:
            filetxt = os.getcwd() + "/" + outputpath+ "/" + FILENAME.replace(".root","")
            filetxt = filetxt.replace("//","/")
#    print(filetxt) 


    f = TFile(filename,"READ");             # read file
    dirlist = f.GetListOfKeys();            # make TList consisting of keys
#    print(dirlist.GetSize())                # printing the number of TTree included in the file
    ITER = dirlist.MakeIterator()   #  MakeIterator() : Return a list iterator -> TIterator
    key = ITER.Next()              #  Next() : returning TObject, but returning TKey.. why??

#    px = numpy.zeros(1, dtype=float)
    histoNum = 0
    histList = []
    NamehistList = []
    while key:
        tree = key.ReadObj()                    # TTree
#        print(tree.GetName())
        branchlist = tree.GetListOfBranches()   # TObjArray
        if(branchlist.IsEmpty()):               # continue if tree is empty
             continue
        ITER_b = branchlist.MakeIterator()      # TIterator
        key_b = ITER_b.Next()                   # TBranch
        while key_b:
            Namehist = FILENAME.replace(".root","") + "_" + tree.GetName() + "_" + key_b.GetName()
            NamehistList.append(Namehist)
            BranchName = key_b.GetName(); #print(BranchName)
            vaName = key_b.GetName();
            exec(vaName + '= numpy.zeros(1, dtype=float)')
            
            tree.SetBranchAddress(BranchName,vaName)
#            print(Namehist)
            for i in range(tree.GetEntries()):
                tree.GetEntry(i)
                
            hist = TH1D(Namehist, Namehist, NBins, IBin, FBin) 
#            hist.Fill(vaName)
            histList.append(hist)
            histoNum = histoNum + 1
#            print(key_b.GetName())
            key_b = ITER_b.Next()
        key = ITER.Next()
    #### After upper "while", all of the histograms are defined.  (Is it possible to automatically set BranchAdress???)


    dirlist = f.GetListOfKeys();            # make TList consisting of keys
#    print(dirlist.GetSize())                # printing the number of TTree included in the file
    ITER = dirlist.MakeIterator()   #  MakeIterator() : Return a list iterator -> TIterator
    key = ITER.Next()  
    while key:
        HN = 0
        tree = key.ReadObj()                    # TTree
        branchlist = tree.GetListOfBranches()   # TObjArray
        if(branchlist.IsEmpty()):               # continue if tree is empty
             continue
        ITER_b = branchlist.MakeIterator()      # TIterator
        key_b = ITER_b.Next()                   # TBranch
        while key_b:
            for i in range(tree.GetEntries()):
                tree.GetEntry(i)
            
#            histList[HN].Fill(px)
            HN=HN+1
            key_b = ITER_b.Next()
        key = ITER.Next()        


    filetxt = filetxt + "_HIST.root"
    outputROOT = TFile(filetxt,"RECREATE")
    for jj in range(len(histList)):
        histList[jj].Write()

    outputROOT.Close()    
    




