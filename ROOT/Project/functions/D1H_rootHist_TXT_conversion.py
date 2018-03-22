#input/output txt format :: Nth_bin Start_of_bin End_of_bin Entry
#filename :: D1H_rootHist_TXT_conversion.py  

def D1H_roothist_to_txt(filename, outputpath = ''):
    from ROOT import TFile, TCanvas, TPad
    import os

    if(filename[0]=="/"):
        filename = filename
    else:    
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break
    
    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
#    print(FILENAME, "******")   

    filetxt = filename.replace(".root","_F.txt")
    filetxt = filetxt.replace("//","/")
    if(outputpath==''):
        wf= open(filetxt,"w+")
        print(filetxt,  " text file is generated !!!")
    else:
        if(outputpath[0] == "/"):
            filetxt = outputpath+ "/" + FILENAME.replace(".root","_F.txt")
        elif(outputpath[0] == "~"):
            filetxt = outputpath.replace("~",os.environ['HOME']) + "/" + FILENAME.replace(".txt","_F.root")
            filetxt = filetxt.replace("//","/")
        else:
            filetxt = os.getcwd() + "/" + outputpath+ "/" + FILENAME.replace(".root","_F.txt")
            filetxt = filetxt.replace("//","/")
        wf= open(filetxt,"w+")
        print(filetxt,  " text file is generated !!!")

    f = TFile(filename,"READ");

    hist=f.Get("h1f");
    Nbin = hist.GetNbinsX();

    for ii in range(1,Nbin+1):
        bin_num = ii
        bin_l = hist.GetBinLowEdge(ii)
        bin_width = hist.GetBinWidth(ii);
        bin_h = bin_l + bin_width;
        binCont = hist.GetBinContent(ii);
        wf.write("%i %f %f %f\n" %(bin_num,bin_l,bin_h,binCont))

    f.Close()
    filetxt = filetxt.replace("//","/")
    return filetxt








def D1H_txt_to_roothist(filename, outputpath=''):
    from ROOT import TFile, TCanvas, TPad, TH1D, TLatex, TStyle, gStyle, TText, gPad, TPaveText
    from inspect import currentframe, getframeinfo
    import os

    #gStyle.SetOptStat(0)
    can = TCanvas("can","can",200,10,500,500);

    if(filename[0]=="/"):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
#    print(FILENAME, "******")    

    fileroot = filename.replace(".txt","_F.root")
    fileroot = fileroot.replace("//","/")
    f = open(filename,"r")

    lineList = f.readlines()
    Nbin = (len(lineList))     # get number of bins
    Line_string = str(lineList[0])
    _,bin_init,_,_ = Line_string.split();  bin_init = float(bin_init)   # get initial bin
    Line_string = str(lineList[len(lineList)-1])
    _,_,bin_final,_ = Line_string.split();  bin_final = float(bin_final)   # get final bin
    f.seek(0)    # reset python read line

    hist = TH1D("h1f","h1f",Nbin,bin_init,bin_final)
    total_e = 0
    for i in range(1,Nbin+1):
        Line_string = str(f.readline())
        _,_,_,bin_c = Line_string.split();
        bin_c = float(bin_c)
        hist.SetBinContent(i,bin_c)
        total_e = total_e + bin_c
    total_e = int(total_e)
    hist.Draw()
    text = TText(hist.GetXaxis().GetBinCenter(2), hist.GetYaxis().GetBinCenter(1), "Recycled. Total Entry : %i" %total_e)
    text.SetTextFont(10)
    text.Draw()
    gPad.Update()
    can.Update()

    if(outputpath==''):
        wf = TFile(fileroot,"RECREATE")
        print(fileroot, " root file is generated !!!")
    else:
        if(outputpath[0] == "/"):
            fileroot = outputpath+ "/" + FILENAME.replace(".txt","_F.root")
            fileroot = fileroot.replace("//","/")
        elif(outputpath[0] == "~"):
            fileroot = outputpath.replace("~",os.environ['HOME']) + "/" + FILENAME.replace(".txt","_F.root")
            fileroot = fileroot.replace("//","/")
        else:
            fileroot = os.getcwd() + "/" + outputpath+ "/" + FILENAME.replace(".txt","_F.root")
            fileroot = fileroot.replace("//","/")
        wf = TFile(fileroot,"RECREATE")
        print(fileroot, " root file is generated !!!")
    hist.Write()
    wf.Close()
    fileroot = fileroot.replace("//","/")
    return fileroot
