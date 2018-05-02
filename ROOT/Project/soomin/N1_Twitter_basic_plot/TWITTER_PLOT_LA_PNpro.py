import os 
from ROOT import TCanvas, TMultiGraph, TGraph, gPad, TLegend, TGaxis
from array import array
from math import sin

def read_file_name(filename):             # returning [filename, filename.root, absolute path filename, absolute path filename without root file]
    f = open(filename,"r")

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
    FILE = FILENAME.replace(".txt","")
    filename_NoRoot = filename.replace(filename[len(filename)-loca:len(filename)],"")

    filelist = [FILE, FILENAME, filename, filename_NoRoot]
#    print(filelist)
    return(filelist)


def Find_Loca(histoName):
    LOCA = len(histoName)
    for i in range (1,len(histoName)+1):
        if(histoName[i] == "_"):
            LOCA = i
            break
        else:
            continue
    return LOCA





def main():
    filename = read_file_name("OUTPUT_TWITTER_TXT_generator/LA_OUTPUT_week1n2n3n4.txt")   ##FIXME
    can = TCanvas("can","can")
    can.SetGrid()
    mg = TMultiGraph()
    nn = 7

    GR = []
    NAME = []
    px,py = array('d'), array('d')
    f = open(filename[2],'r')
    indicator = 0


    for line in f:
        if(indicator == 0):
            indicator = indicator + 1
            continue
           
        Name, Total, Pos, Neg, TNum = line.split()
        name = Find_Loca(Name)
        name = Name.replace(Name[name:],"")
#        print(name)
       
        px.append((indicator-1)%7); py.append(float(Pos)/float(Neg))
        if((indicator)%7 == 0):
            NAME.append(name)
            gr = TGraph( nn, px, py )
            GR.append(gr)
            px,py = array('d'), array('d')
        indicator = indicator + 1

#    print(GR); print(len(GR))
    for i in range(len(GR)):
        GR[i].SetLineWidth(2)
        if "water" in NAME[i]:
            GR[i].SetLineWidth(5); GR[i].SetLineColor(1) ;GR[i].SetMarkerColor(1)
        if "wine" in NAME[i]:
            GR[i].SetMarkerColor(2);GR[i].SetLineColor(2)
        if "beer" in NAME[i]:
            GR[i].SetMarkerColor(5);GR[i].SetLineColor(5)
        if "tea" in NAME[i]:
            GR[i].SetMarkerColor(4);GR[i].SetLineColor(4)
        if "coffee" in NAME[i]:
            GR[i].SetMarkerColor(3);GR[i].SetLineColor(3)
        if "juice" in NAME[i]:
            GR[i].SetMarkerColor(7);GR[i].SetLineColor(7)
        if "COLA" in NAME[i]:
            GR[i].SetMarkerColor(6);GR[i].SetLineColor(6)
        GR[i].GetXaxis().SetTitle("days")
        GR[i].SetMarkerStyle(20)
#        GR[i].Fit("pol4","q")
        mg.Add(GR[i])

    mg.Draw("ALP")

    leg = TLegend(0.75, 0.82, 0.95, 0.95)
    leg.SetBorderSize(0)
    leg.SetFillColor(10)
    for i in range(len(GR)):
        leg_entry = leg.AddEntry(GR[i], NAME[i],"l")
    leg.Draw()
    mg.SetTitle("Positive/Negative words propotion at LA(week 1&2&3&4)")    ##FIXME
    mg.GetHistogram().GetXaxis().SetTitle("days")
    mg.GetHistogram().GetXaxis().SetTitleOffset(1)
    mg.GetHistogram().GetXaxis().SetLabelSize(0.03)
    mg.GetHistogram().GetYaxis().SetTitle("Emotion proportion(Pos/Neg)")
    mg.GetHistogram().GetYaxis().SetTitleOffset(1.3)
    mg.GetHistogram().GetYaxis().SetLabelSize(0.03)
    mg.GetHistogram().GetXaxis().SetBinLabel(5,"Mon")
    mg.GetHistogram().GetXaxis().SetBinLabel(20,"Tue")
    mg.GetHistogram().GetXaxis().SetBinLabel(35,"Wed")
    mg.GetHistogram().GetXaxis().SetBinLabel(51,"Thu")
    mg.GetHistogram().GetXaxis().SetBinLabel(66,"Fri")
    mg.GetHistogram().GetXaxis().SetBinLabel(81,"Sat")
    mg.GetHistogram().GetXaxis().SetBinLabel(96,"Sun")
#    mg.GetHistogram().GetXaxis().SetBinLabel(84,"Mon")
#    mg.GetHistogram().GetXaxis().SetBinLabel(96,"Tue")
#    for i in range(len(GR)):
#        mg.GetHistogram().GetXaxis().SetBinLabel(i,DAYS)
#    mg.GetHistogram().GetXaxis().SetLabel("tt")
    
    can.Modified()
    can.Update()
   # can.GetFrame().SetBorderSize( 12 )
    can.Print("PNpro_LA_week1n2n3n4.pdf")    ##FIXME



if __name__=="__main__":
    main()






