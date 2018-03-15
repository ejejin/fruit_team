
from os import path
from ROOT import TCanvas, TPad, TFile, TPaveText
from ROOT import gROOT, gBenchmark

c1 = TCanvas("c1","c1",200,10,700,500)
c1.SetGrid()
c1.GetFrame().SetFillColor(21)
c1.GetFrame().SetBorderMode(-1)
c1.GetFrame().SetBorderSize(5)

gBenchmark.Start("fit1")

fill = TFile("py-fillrandom.root","READ")
fill.ls()

sqroot = gROOT.FindObject("sqroot")
sqroot.Print(); print("\n")

hist = gROOT.FindObject("h1f")
hist.Print(); print("\n"); hist.Draw()
hist.SetFillColor(45)
hist.Fit("sqroot")
c1.Update()





fill.Close()
gBenchmark.Show("fit1")


