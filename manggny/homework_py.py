from ROOT import TCanvas,TH1D

c1 = TCanvas('c1','practice with python',200,10,700,500)

h1 = TH1D('h1','histogram!',100,-5,5)

h1.FillRandom('gaus',10000)
h1.Draw()

