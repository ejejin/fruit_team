#input/output txt format :: Start_of_bin End_of_bin Entry
#filename :: D1H_ROOT_TXT_conversion.py  

def D1H_root_to_txt(filename, outputpath = ''):
    from ROOT import TFile, TCanvas, TPad

    filetxt = filename.replace(".root",""); filetxt = filetxt +"_F.txt"
    if(outputpath==''):
        wf= open(filetxt,"w+")
        print(filetxt,  " text file is generated !!!")
    else:
        filetxt=outputpath+"/_processed.txt"
        wf= open(filetxt,"w+")
        print(filetxt,  " text file is generated !!!")

    f = TFile(filename,"READ");

    hist=f.Get("h1f");
    Nbin = hist.GetNbinsX();

    for ii in range(1,Nbin+1):
        bin_l = hist.GetBinLowEdge(ii)
        bin_width = hist.GetBinWidth(ii);
        bin_h = bin_l + bin_width;
        binCont = hist.GetBinContent(ii);
        wf.write("%f %f %f\n" %(bin_l,bin_h,binCont))

    f.Close()


def D1H_txt_to_root(filename, outputpath=''):
    from ROOT import TFile, TCanvas, TPad, TH1D, TLatex, TStyle, gStyle, TText, gPad, TPaveText
    from inspect import currentframe, getframeinfo

    #gStyle.SetOptStat(0)
    can = TCanvas("can","can",200,10,500,500);
    fileroot = filename.replace(".txt",""); fileroot = fileroot +"_F.root"
    f = open(filename,"r")

    lineList = f.readlines()
    Nbin = (len(lineList))     # get number of bins
    Line_string = str(lineList[0])
    bin_init,_,_ = Line_string.split();  bin_init = float(bin_init)   # get initial bin
    Line_string = str(lineList[len(lineList)-1])
    _,bin_final,_ = Line_string.split();  bin_final = float(bin_final)   # get final bin
    f.seek(0)    # reset python read line

    hist = TH1D("h1f","h1f",Nbin,bin_init,bin_final)
    total_e = 0
    for i in range(1,Nbin+1):
        Line_string = str(f.readline())
        _,_,bin_c = Line_string.split();
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
        fileroot = outputpath+"/_processed.root"
        wf = TFile(fileroot,"RECREATE")
        print(fileroot, " root file is generated !!!")
    hist.Write()
    wf.Close()
