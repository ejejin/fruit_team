from ROOT import TFile,TCanvas,TPad,TH1F


file1=open("mroot_to_txe_py.txt")

f1 = TFile("mtxt_to_root.root","recreate")
c1 = TCanvas("c1","txt to root with py",200,10,700,900)

h1f = TH1F("h1f","hist",200,0,10)

for line in file1:
    x = line.split()
   # print(float(x[0])*0.05,float(x[1]))
    for i in range(int(float(x[1]))):
        h1f.Fill(float(x[0])*0.05)

h1f.Draw()
c1.Update()
f1.Write()
f1.Close()

#   print(line.split())  

 # h1f.Fill()


#print(type(file1))




# hist_name.Fill(x,y)






#fi = TFile("mpy_txt_to_root.root","RECREATE")

