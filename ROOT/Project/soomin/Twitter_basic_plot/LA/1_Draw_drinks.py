from ROOT import TH1D, TFile, TCanvas, gStyle, gPad, TLegend

gStyle.SetOptStat(0)

cann = TCanvas("cann","cann")
cann1 = TCanvas("cann1","cann1")
canp = TCanvas("canp","canp")
canp1 = TCanvas("canp1","canp1")
cann.cd()
gPad.SetLogy(1)


CanvasTitle =   "Monday"
FilenameTitle = "Monday"


#Monday
file_WINE = TFile("wine_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0319Mon_LA_s_tree_cut_wine_0319Mon_LA_s_f_NEGP").Clone();hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0319Mon_LA_s_tree_cut_wine_0319Mon_LA_s_f_POSP").Clone();hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0319Mon_LA_s_tree_cut_water_0319Mon_LA_s_f_NEGP").Clone();hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0319Mon_LA_s_tree_cut_water_0319Mon_LA_s_f_POSP").Clone();hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0319Mon_LA_s_tree_cut_tea_0319Mon_LA_s_f_NEGP").Clone();hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0319Mon_LA_s_tree_cut_tea_0319Mon_LA_s_f_POSP").Clone();hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0319Mon_LA_s_tree_cut_juice_0319Mon_LA_s_f_NEGP").Clone();hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0319Mon_LA_s_tree_cut_juice_0319Mon_LA_s_f_POSP").Clone();hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0319Mon_LA_s_tree_cut_coffee_0319Mon_LA_s_f_NEGP").Clone();hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0319Mon_LA_s_tree_cut_coffee_0319Mon_LA_s_f_POSP").Clone();hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0319Mon_LA_s_tree_cut_beer_0319Mon_LA_s_f_NEGP").Clone();hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0319Mon_LA_s_tree_cut_beer_0319Mon_LA_s_f_POSP").Clone();hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0319Mon_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0319Mon_LA_s_tree_cut_COLA_COKE_0319Mon_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0319Mon_LA_s_tree_cut_COLA_COKE_0319Mon_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)


'''
#Tuesday
file_WINE = TFile("wine_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0320Tue_LA_s_tree_cut_wine_0320Tue_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0320Tue_LA_s_tree_cut_wine_0320Tue_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0320Tue_LA_s_tree_cut_water_0320Tue_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0320Tue_LA_s_tree_cut_water_0320Tue_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0320Tue_LA_s_tree_cut_tea_0320Tue_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0320Tue_LA_s_tree_cut_tea_0320Tue_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0320Tue_LA_s_tree_cut_juice_0320Tue_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0320Tue_LA_s_tree_cut_juice_0320Tue_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0320Tue_LA_s_tree_cut_coffee_0320Tue_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0320Tue_LA_s_tree_cut_coffee_0320Tue_LA_s_f_POSP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0320Tue_LA_s_tree_cut_beer_0320Tue_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0320Tue_LA_s_tree_cut_beer_0320Tue_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0320Tue_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0320Tue_LA_s_tree_cut_COLA_COKE_0320Tue_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0320Tue_LA_s_tree_cut_COLA_COKE_0320Tue_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''


'''
#Wednesday
file_WINE = TFile("wine_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0321Wed_LA_s_tree_cut_wine_0321Wed_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0321Wed_LA_s_tree_cut_wine_0321Wed_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0321Wed_LA_s_tree_cut_water_0321Wed_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0321Wed_LA_s_tree_cut_water_0321Wed_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0321Wed_LA_s_tree_cut_tea_0321Wed_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0321Wed_LA_s_tree_cut_tea_0321Wed_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0321Wed_LA_s_tree_cut_juice_0321Wed_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0321Wed_LA_s_tree_cut_juice_0321Wed_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0321Wed_LA_s_tree_cut_coffee_0321Wed_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0321Wed_LA_s_tree_cut_coffee_0321Wed_LA_s_f_NEGP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0321Wed_LA_s_tree_cut_beer_0321Wed_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0321Wed_LA_s_tree_cut_beer_0321Wed_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0321Wed_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0321Wed_LA_s_tree_cut_COLA_COKE_0321Wed_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0321Wed_LA_s_tree_cut_COLA_COKE_0321Wed_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''


'''
#Thursday
file_WINE = TFile("wine_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0322Thu_LA_s_tree_cut_wine_0322Thu_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0322Thu_LA_s_tree_cut_wine_0322Thu_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0322Thu_LA_s_tree_cut_water_0322Thu_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0322Thu_LA_s_tree_cut_water_0322Thu_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0322Thu_LA_s_tree_cut_tea_0322Thu_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0322Thu_LA_s_tree_cut_tea_0322Thu_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0322Thu_LA_s_tree_cut_juice_0322Thu_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0322Thu_LA_s_tree_cut_juice_0322Thu_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0322Thu_LA_s_tree_cut_coffee_0322Thu_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0322Thu_LA_s_tree_cut_coffee_0322Thu_LA_s_f_POSP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0322Thu_LA_s_tree_cut_beer_0322Thu_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0322Thu_LA_s_tree_cut_beer_0322Thu_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0322Thu_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0322Thu_LA_s_tree_cut_COLA_COKE_0322Thu_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0322Thu_LA_s_tree_cut_COLA_COKE_0322Thu_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''


'''
#Friday
file_WINE = TFile("wine_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0323Fri_LA_s_tree_cut_wine_0323Fri_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0323Fri_LA_s_tree_cut_wine_0323Fri_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0323Fri_LA_s_tree_cut_water_0323Fri_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0323Fri_LA_s_tree_cut_water_0323Fri_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0323Fri_LA_s_tree_cut_tea_0323Fri_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0323Fri_LA_s_tree_cut_tea_0323Fri_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0323Fri_LA_s_tree_cut_juice_0323Fri_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0323Fri_LA_s_tree_cut_juice_0323Fri_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0323Fri_LA_s_tree_cut_coffee_0323Fri_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0323Fri_LA_s_tree_cut_coffee_0323Fri_LA_s_f_POSP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0323Fri_LA_s_tree_cut_beer_0323Fri_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0323Fri_LA_s_tree_cut_beer_0323Fri_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0323Fri_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0323Fri_LA_s_tree_cut_COLA_COKE_0323Fri_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0323Fri_LA_s_tree_cut_COLA_COKE_0323Fri_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''


'''
#Saturday
file_WINE = TFile("wine_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0324Sat_LA_s_tree_cut_wine_0324Sat_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0324Sat_LA_s_tree_cut_wine_0324Sat_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0324Sat_LA_s_tree_cut_water_0324Sat_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0324Sat_LA_s_tree_cut_water_0324Sat_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0324Sat_LA_s_tree_cut_tea_0324Sat_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0324Sat_LA_s_tree_cut_tea_0324Sat_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0324Sat_LA_s_tree_cut_juice_0324Sat_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0324Sat_LA_s_tree_cut_juice_0324Sat_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0324Sat_LA_s_tree_cut_coffee_0324Sat_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0324Sat_LA_s_tree_cut_coffee_0324Sat_LA_s_f_POSP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0324Sat_LA_s_tree_cut_beer_0324Sat_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0324Sat_LA_s_tree_cut_beer_0324Sat_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0324Sat_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0324Sat_LA_s_tree_cut_COLA_COKE_0324Sat_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0324Sat_LA_s_tree_cut_COLA_COKE_0324Sat_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''


'''
#Sunday
file_WINE = TFile("wine_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_WINE_N = file_WINE.Get("wine_0325Sun_LA_s_tree_cut_wine_0325Sun_LA_s_f_NEGP").Clone(); hist_WINE_N.SetLineColor(1); scale = hist_WINE_N.GetEntries(); scale = 1/scale; hist_WINE_N.Scale(scale); hist_WINE_N.SetBins(10,0.0,0.5)
hist_WINE_P = file_WINE.Get("wine_0325Sun_LA_s_tree_cut_wine_0325Sun_LA_s_f_POSP").Clone(); hist_WINE_P.SetLineColor(1); scale = hist_WINE_P.GetEntries(); scale = 1/scale; hist_WINE_P.Scale(scale); hist_WINE_P.SetBins(10,0.0,0.5)

file_WATER = TFile("water_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_WATER_N = file_WATER.Get("water_0325Sun_LA_s_tree_cut_water_0325Sun_LA_s_f_NEGP").Clone(); hist_WATER_N.SetLineColor(2); scale = hist_WATER_N.GetEntries(); scale = 1/scale; hist_WATER_N.Scale(scale); hist_WATER_N.SetBins(10,0.0,0.5)
hist_WATER_P = file_WATER.Get("water_0325Sun_LA_s_tree_cut_water_0325Sun_LA_s_f_POSP").Clone(); hist_WATER_P.SetLineColor(2); scale = hist_WATER_P.GetEntries(); scale = 1/scale; hist_WATER_P.Scale(scale); hist_WATER_P.SetBins(10,0.0,0.5)

file_TEA = TFile("tea_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_TEA_N = file_TEA.Get("tea_0325Sun_LA_s_tree_cut_tea_0325Sun_LA_s_f_NEGP").Clone(); hist_TEA_N.SetLineColor(3); scale = hist_TEA_N.GetEntries(); scale = 1/scale; hist_TEA_N.Scale(scale); hist_TEA_N.SetBins(10,0.0,0.5)
hist_TEA_P = file_TEA.Get("tea_0325Sun_LA_s_tree_cut_tea_0325Sun_LA_s_f_POSP").Clone(); hist_TEA_P.SetLineColor(3); scale = hist_TEA_P.GetEntries(); scale = 1/scale; hist_TEA_P.Scale(scale); hist_TEA_P.SetBins(10,0.0,0.5)

file_JUICE = TFile("juice_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_JUICE_N = file_JUICE.Get("juice_0325Sun_LA_s_tree_cut_juice_0325Sun_LA_s_f_NEGP").Clone(); hist_JUICE_N.SetLineColor(4); scale = hist_JUICE_N.GetEntries(); scale = 1/scale; hist_JUICE_N.Scale(scale); hist_JUICE_N.SetBins(10,0.0,0.5)
hist_JUICE_P = file_JUICE.Get("juice_0325Sun_LA_s_tree_cut_juice_0325Sun_LA_s_f_POSP").Clone(); hist_JUICE_P.SetLineColor(4); scale = hist_JUICE_P.GetEntries(); scale = 1/scale; hist_JUICE_P.Scale(scale); hist_JUICE_P.SetBins(10,0.0,0.5)

file_COFFEE = TFile("coffee_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_COFFEE_N = file_COFFEE.Get("coffee_0325Sun_LA_s_tree_cut_coffee_0325Sun_LA_s_f_NEGP").Clone(); hist_COFFEE_N.SetLineColor(5); scale = hist_COFFEE_N.GetEntries(); scale = 1/scale; hist_COFFEE_N.Scale(scale); hist_COFFEE_N.SetBins(10,0.0,0.5)
hist_COFFEE_P = file_COFFEE.Get("coffee_0325Sun_LA_s_tree_cut_coffee_0325Sun_LA_s_f_POSP").Clone(); hist_COFFEE_P.SetLineColor(5); scale = hist_COFFEE_P.GetEntries(); scale = 1/scale; hist_COFFEE_P.Scale(scale); hist_COFFEE_P.SetBins(10,0.0,0.5)

file_BEER = TFile("beer_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_BEER_N = file_BEER.Get("beer_0325Sun_LA_s_tree_cut_beer_0325Sun_LA_s_f_NEGP").Clone(); hist_BEER_N.SetLineColor(6); scale = hist_BEER_N.GetEntries(); scale = 1/scale; hist_BEER_N.Scale(scale); hist_BEER_N.SetBins(10,0.0,0.5)
hist_BEER_P = file_BEER.Get("beer_0325Sun_LA_s_tree_cut_beer_0325Sun_LA_s_f_POSP").Clone(); hist_BEER_P.SetLineColor(6); scale = hist_BEER_P.GetEntries(); scale = 1/scale; hist_BEER_P.Scale(scale); hist_BEER_P.SetBins(10,0.0,0.5)

file_COLA = TFile("COLA_COKE_0325Sun_LA_s_tree_cut_hist.root","READ")
hist_COLA_N = file_COLA.Get("COLA_COKE_0325Sun_LA_s_tree_cut_COLA_COKE_0325Sun_LA_s_f_NEGP").Clone(); hist_COLA_N.SetLineColor(7); scale = hist_COLA_N.GetEntries(); scale = 1/scale; hist_COLA_N.Scale(scale); hist_COLA_N.SetBins(10,0.0,0.5)
hist_COLA_P = file_COLA.Get("COLA_COKE_0325Sun_LA_s_tree_cut_COLA_COKE_0325Sun_LA_s_f_POSP").Clone(); hist_COLA_P.SetLineColor(7); scale = hist_COLA_P.GetEntries(); scale = 1/scale; hist_COLA_P.Scale(scale); hist_COLA_P.SetBins(10,0.0,0.5)
'''



hist_COLA_N.SetTitle(CanvasTitle+", with NEGATIVE on each beverage at LA (Normalized)")
hist_COLA_N.SetXTitle("Negative words propotion of Total words on a Tweet")
hist_COLA_N.SetYTitle("Emotion propotion (Log scale)")
hist_COLA_N.Draw("hist")
hist_BEER_N.Draw("hist same")
hist_COFFEE_N.Draw("hist same")
hist_JUICE_N.Draw("hist same")
hist_TEA_N.Draw("hist same")
hist_WATER_N.Draw("hist same")
hist_WINE_N.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_COLA_N,"COLA","f")
leg_entry = leg.AddEntry(hist_BEER_N,"BEER","f")
leg_entry = leg.AddEntry(hist_COFFEE_N,"COFFEE","f")
leg_entry = leg.AddEntry(hist_JUICE_N,"JUICE","f")
leg_entry = leg.AddEntry(hist_TEA_N,"TEA","f")
leg_entry = leg.AddEntry(hist_WATER_N,"WATER","f")
leg_entry = leg.AddEntry(hist_WINE_N,"WINE","f")
leg.Draw()
cann.Modified()
cann.Update()
cann.Print(FilenameTitle+"_Drinks_Negative_log.pdf")


cann1.cd()
gPad.SetLogy(0)
hist_COLA_N.SetYTitle("Emotion propotion (Natural scale)")
hist_COLA_N.Draw("hist")
hist_BEER_N.Draw("hist same")
hist_COFFEE_N.Draw("hist same")
hist_JUICE_N.Draw("hist same")
hist_TEA_N.Draw("hist same")
hist_WATER_N.Draw("hist same")
hist_WINE_N.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_COLA_N,"COLA","f")
leg_entry = leg.AddEntry(hist_BEER_N,"BEER","f")
leg_entry = leg.AddEntry(hist_COFFEE_N,"COFFEE","f")
leg_entry = leg.AddEntry(hist_JUICE_N,"JUICE","f")
leg_entry = leg.AddEntry(hist_TEA_N,"TEA","f")
leg_entry = leg.AddEntry(hist_WATER_N,"WATER","f")
leg_entry = leg.AddEntry(hist_WINE_N,"WINE","f")
leg.Draw()
cann1.Modified()
cann1.Update()
cann1.Print(FilenameTitle+"_Drinks_Negative.pdf")


canp.cd()
gPad.SetLogy(1)
hist_COLA_P.SetTitle(CanvasTitle+", with NEGATIVE on each beverage at LA (Normalized)")
hist_COLA_P.SetXTitle("Positive words propotion of Total words on a Tweet")
hist_COLA_P.SetYTitle("Emotion propotion (Log scale)")
hist_COLA_P.Draw("hist")
hist_BEER_P.Draw("hist same")
hist_COFFEE_P.Draw("hist same")
hist_JUICE_P.Draw("hist same")
hist_TEA_P.Draw("hist same")
hist_WATER_P.Draw("hist same")
hist_WINE_P.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_COLA_P,"COLA","f")
leg_entry = leg.AddEntry(hist_BEER_P,"BEER","f")
leg_entry = leg.AddEntry(hist_COFFEE_P,"COFFEE","f")
leg_entry = leg.AddEntry(hist_JUICE_P,"JUICE","f")
leg_entry = leg.AddEntry(hist_TEA_P,"TEA","f")
leg_entry = leg.AddEntry(hist_WATER_P,"WATER","f")
leg_entry = leg.AddEntry(hist_WINE_P,"WINE","f")
leg.Draw()
canp.Modified()
canp.Update()
canp.Print(FilenameTitle+"_Drinks_Positive_log.pdf")

canp1.cd()
gPad.SetLogy(0)
hist_COLA_P.SetTitle(CanvasTitle+", with NEGATIVE on each beverage at LA (Normalized)")
hist_COLA_P.SetXTitle("Positive words propotion of Total words on a Tweet")
hist_COLA_P.SetYTitle("Emotion propotion (Natural scale)")
hist_COLA_P.Draw("hist")
hist_BEER_P.Draw("hist same")
hist_COFFEE_P.Draw("hist same")
hist_JUICE_P.Draw("hist same")
hist_TEA_P.Draw("hist same")
hist_WATER_P.Draw("hist same")
hist_WINE_P.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_COLA_P,"COLA","f")
leg_entry = leg.AddEntry(hist_BEER_P,"BEER","f")
leg_entry = leg.AddEntry(hist_COFFEE_P,"COFFEE","f")
leg_entry = leg.AddEntry(hist_JUICE_P,"JUICE","f")
leg_entry = leg.AddEntry(hist_TEA_P,"TEA","f")
leg_entry = leg.AddEntry(hist_WATER_P,"WATER","f")
leg_entry = leg.AddEntry(hist_WINE_P,"WINE","f")
leg.Draw()
canp1.Modified()
canp1.Update()
canp1.Print(FilenameTitle+"_Drinks_Positive.pdf")






