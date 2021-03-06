from ROOT import TH1D, TFile, TCanvas, gStyle, gPad, TLegend

gStyle.SetOptStat(0)

cann = TCanvas("cann","cann")
cann1 = TCanvas("cann1","cann1")
canp = TCanvas("canp","canp")
canp1 = TCanvas("canp1","canp1")
cann.cd()
gPad.SetLogy(1)


CanvasTitle = "COFFEE"
FilenameTitle = "COFFEE"


'''
file_mon19 = TFile("","READ")
hist_mon19_N = file_mon19.Get("").Clone();hist_mon19_N.SetLineColor(1); scale = hist_mon19_N.GetEntries(); scale = 1/scale; hist_mon19_N.Scale(scale); hist_mon19_N.SetBins(10,0.0,0.5)
hist_mon19_P = file_mon19.Get("").Clone();hist_mon19_P.SetLineColor(1); scale = hist_mon19_P.GetEntries(); scale = 1/scale; hist_mon19_P.Scale(scale); hist_mon19_P.SetBins(10,0.0,0.5)
'''
file_mon19 = TFile("coffee_0319Mon_newyork_s_tree_cut_hist.root","READ")
hist_mon19_N = file_mon19.Get("coffee_0319Mon_newyork_s_tree_cut_coffee_0319Mon_newyork_s_f_NEGP").Clone();hist_mon19_N.SetLineColor(1); scale = hist_mon19_N.GetEntries(); scale = 1/scale; hist_mon19_N.Scale(scale); hist_mon19_N.SetBins(10,0.0,0.5)
hist_mon19_P = file_mon19.Get("coffee_0319Mon_newyork_s_tree_cut_coffee_0319Mon_newyork_s_f_POSP").Clone();hist_mon19_P.SetLineColor(1); scale = hist_mon19_P.GetEntries(); scale = 1/scale; hist_mon19_P.Scale(scale); hist_mon19_P.SetBins(10,0.0,0.5)
#file_mon19 = TFile("beer_0319Mon_newyork_s_tree_cut_hist.root","READ")
#hist_mon19_N = file_mon19.Get("beer_0319Mon_newyork_s_tree_cut_beer_0319Mon_newyork_s_f_NEGP").Clone();hist_mon19_N.SetLineColor(1); scale = hist_mon19_N.GetEntries(); scale = 1/scale; hist_mon19_N.Scale(scale); hist_mon19_N.SetBins(10,0.0,0.5)
#hist_mon19_P = file_mon19.Get("beer_0319Mon_newyork_s_tree_cut_beer_0319Mon_newyork_s_f_POSP").Clone();hist_mon19_P.SetLineColor(1); scale = hist_mon19_P.GetEntries(); scale = 1/scale; hist_mon19_P.Scale(scale); hist_mon19_P.SetBins(10,0.0,0.5)
#file_mon19 = TFile("COLA_COKE_0319Mon_newyork_s_tree_cut_hist.root","READ")
#hist_mon19_N = file_mon19.Get("COLA_COKE_0319Mon_newyork_s_tree_cut_COLA_COKE_0319Mon_newyork_s_f_NEGP").Clone(); hist_mon19_N.SetLineColor(1); scale = hist_mon19_N.GetEntries(); scale = 1/scale; hist_mon19_N.Scale(scale); hist_mon19_N.SetBins(10,0.0,0.5)
#hist_mon19_P = file_mon19.Get("COLA_COKE_0319Mon_newyork_s_tree_cut_COLA_COKE_0319Mon_newyork_s_f_POSP").Clone(); hist_mon19_P.SetLineColor(1); scale = hist_mon19_P.GetEntries(); scale = 1/scale; hist_mon19_P.Scale(scale); hist_mon19_P.SetBins(10,0.0,0.5)



'''
file_tue20 = TFile("","READ")
hist_tue20_N = file_tue20.Get("").Clone(); hist_tue20_N.SetLineColor(2); scale = hist_tue20_N.GetEntries(); scale = 1/scale; hist_tue20_N.Scale(scale); hist_tue20_N.SetBins(10,0.0,0.5)
hist_tue20_P = file_tue20.Get("").Clone(); hist_tue20_P.SetLineColor(2); scale = hist_tue20_P.GetEntries(); scale = 1/scale; hist_tue20_P.Scale(scale); hist_tue20_P.SetBins(10,0.0,0.5)
'''
file_tue20 = TFile("coffee_0320Thu_newyork_s_tree_cut_hist.root","READ")
hist_tue20_N = file_tue20.Get("coffee_0320Thu_newyork_s_tree_cut_coffee_0320Thu_newyork_s_f_NEGP").Clone(); hist_tue20_N.SetLineColor(2); scale = hist_tue20_N.GetEntries(); scale = 1/scale; hist_tue20_N.Scale(scale); hist_tue20_N.SetBins(10,0.0,0.5)
hist_tue20_P = file_tue20.Get("coffee_0320Thu_newyork_s_tree_cut_coffee_0320Thu_newyork_s_f_POSP").Clone(); hist_tue20_P.SetLineColor(2); scale = hist_tue20_P.GetEntries(); scale = 1/scale; hist_tue20_P.Scale(scale); hist_tue20_P.SetBins(10,0.0,0.5)
#file_tue20 = TFile("beer_0320Tue_newyork_s_tree_cut_hist.root","READ")
#hist_tue20_N = file_tue20.Get("beer_0320Tue_newyork_s_tree_cut_beer_0320Tue_newyork_s_f_NEGP").Clone(); hist_tue20_N.SetLineColor(2); scale = hist_tue20_N.GetEntries(); scale = 1/scale; hist_tue20_N.Scale(scale); hist_tue20_N.SetBins(10,0.0,0.5)
#hist_tue20_P = file_tue20.Get("beer_0320Tue_newyork_s_tree_cut_beer_0320Tue_newyork_s_f_POSP").Clone(); hist_tue20_P.SetLineColor(2); scale = hist_tue20_P.GetEntries(); scale = 1/scale; hist_tue20_P.Scale(scale); hist_tue20_P.SetBins(10,0.0,0.5)
#file_tue20 = TFile("COLA_COKE_0320Tue_newyork_s_tree_cut_hist.root","READ")
#hist_tue20_N = file_tue20.Get("COLA_COKE_0320Tue_newyork_s_tree_cut_COLA_COKE_0320Tue_newyork_s_f_NEGP").Clone(); hist_tue20_N.SetLineColor(2); scale = hist_tue20_N.GetEntries(); scale = 1/scale; hist_tue20_N.Scale(scale); hist_tue20_N.SetBins(10,0.0,0.5)
#hist_tue20_P = file_tue20.Get("COLA_COKE_0320Tue_newyork_s_tree_cut_COLA_COKE_0320Tue_newyork_s_f_POSP").Clone(); hist_tue20_P.SetLineColor(2); scale = hist_tue20_P.GetEntries(); scale = 1/scale; hist_tue20_P.Scale(scale); hist_tue20_P.SetBins(10,0.0,0.5)



'''
file_wed21 = TFile("","READ")
hist_wed21_N = file_wed21.Get("").Clone(); hist_wed21_N.SetLineColor(3); scale = hist_wed21_N.GetEntries(); scale = 1/scale; hist_wed21_N.Scale(scale); hist_wed21_N.SetBins(10,0.0,0.5)
hist_wed21_P = file_wed21.Get("").Clone(); hist_wed21_P.SetLineColor(3); scale = hist_wed21_P.GetEntries(); scale = 1/scale; hist_wed21_P.Scale(scale); hist_wed21_P.SetBins(10,0.0,0.5)
'''
file_wed21 = TFile("coffee_0321Wed_newyork_s_tree_cut_hist.root","READ")
hist_wed21_N = file_wed21.Get("coffee_0321Wed_newyork_s_tree_cut_coffee_0321Wed_newyork_s_f_NEGP").Clone(); hist_wed21_N.SetLineColor(3); scale = hist_wed21_N.GetEntries(); scale = 1/scale; hist_wed21_N.Scale(scale); hist_wed21_N.SetBins(10,0.0,0.5)
hist_wed21_P = file_wed21.Get("coffee_0321Wed_newyork_s_tree_cut_coffee_0321Wed_newyork_s_f_NEGP").Clone(); hist_wed21_P.SetLineColor(3); scale = hist_wed21_P.GetEntries(); scale = 1/scale; hist_wed21_P.Scale(scale); hist_wed21_P.SetBins(10,0.0,0.5)
#file_wed21 = TFile("beer_0321Wed_newyork_s_tree_cut_hist.root","READ")
#hist_wed21_N = file_wed21.Get("beer_0321Wed_newyork_s_tree_cut_beer_0321Wed_newyork_s_f_NEGP").Clone(); hist_wed21_N.SetLineColor(3); scale = hist_wed21_N.GetEntries(); scale = 1/scale; hist_wed21_N.Scale(scale); hist_wed21_N.SetBins(10,0.0,0.5)
#hist_wed21_P = file_wed21.Get("beer_0321Wed_newyork_s_tree_cut_beer_0321Wed_newyork_s_f_POSP").Clone(); hist_wed21_P.SetLineColor(3); scale = hist_wed21_P.GetEntries(); scale = 1/scale; hist_wed21_P.Scale(scale); hist_wed21_P.SetBins(10,0.0,0.5)
#file_wed21 = TFile("COLA_COKE_0321Wed_newyork_s_tree_cut_hist.root","READ")
#hist_wed21_N = file_wed21.Get("COLA_COKE_0321Wed_newyork_s_tree_cut_COLA_COKE_0321Wed_newyork_s_f_NEGP").Clone(); hist_wed21_N.SetLineColor(3); scale = hist_wed21_N.GetEntries(); scale = 1/scale; hist_wed21_N.Scale(scale); hist_wed21_N.SetBins(10,0.0,0.5)
#hist_wed21_P = file_wed21.Get("COLA_COKE_0321Wed_newyork_s_tree_cut_COLA_COKE_0321Wed_newyork_s_f_POSP").Clone(); hist_wed21_P.SetLineColor(3); scale = hist_wed21_P.GetEntries(); scale = 1/scale; hist_wed21_P.Scale(scale); hist_wed21_P.SetBins(10,0.0,0.5)


'''
file_thu22 = TFile("","READ")
hist_thu22_N = file_thu22.Get("").Clone(); hist_thu22_N.SetLineColor(4); scale = hist_thu22_N.GetEntries(); scale = 1/scale; hist_thu22_N.Scale(scale); hist_thu22_N.SetBins(10,0.0,0.5)
hist_thu22_P = file_thu22.Get("").Clone(); hist_thu22_P.SetLineColor(4); scale = hist_thu22_P.GetEntries(); scale = 1/scale; hist_thu22_P.Scale(scale); hist_thu22_P.SetBins(10,0.0,0.5)
'''
file_thu22 = TFile("coffee_0322Thu_newyork_s_tree_cut_hist.root","READ")
hist_thu22_N = file_thu22.Get("coffee_0322Thu_newyork_s_tree_cut_coffee_0322Thu_newyork_s_f_NEGP").Clone(); hist_thu22_N.SetLineColor(4); scale = hist_thu22_N.GetEntries(); scale = 1/scale; hist_thu22_N.Scale(scale); hist_thu22_N.SetBins(10,0.0,0.5)
hist_thu22_P = file_thu22.Get("coffee_0322Thu_newyork_s_tree_cut_coffee_0322Thu_newyork_s_f_POSP").Clone(); hist_thu22_P.SetLineColor(4); scale = hist_thu22_P.GetEntries(); scale = 1/scale; hist_thu22_P.Scale(scale); hist_thu22_P.SetBins(10,0.0,0.5)
#file_thu22 = TFile("beer_0322Thu_newyork_s_tree_cut_hist.root","READ")
#hist_thu22_N = file_thu22.Get("beer_0322Thu_newyork_s_tree_cut_beer_0322Thu_newyork_s_f_NEGP").Clone(); hist_thu22_N.SetLineColor(4); scale = hist_thu22_N.GetEntries(); scale = 1/scale; hist_thu22_N.Scale(scale); hist_thu22_N.SetBins(10,0.0,0.5)
#hist_thu22_P = file_thu22.Get("beer_0322Thu_newyork_s_tree_cut_beer_0322Thu_newyork_s_f_POSP").Clone(); hist_thu22_P.SetLineColor(4); scale = hist_thu22_P.GetEntries(); scale = 1/scale; hist_thu22_P.Scale(scale); hist_thu22_P.SetBins(10,0.0,0.5)
#file_thu22 = TFile("COLA_COKE_0322Thu_newyork_s_tree_cut_hist.root","READ")
#hist_thu22_N = file_thu22.Get("COLA_COKE_0322Thu_newyork_s_tree_cut_COLA_COKE_0322Thu_newyork_s_f_NEGP").Clone(); hist_thu22_N.SetLineColor(4); scale = hist_thu22_N.GetEntries(); scale = 1/scale; hist_thu22_N.Scale(scale); hist_thu22_N.SetBins(10,0.0,0.5)
#hist_thu22_P = file_thu22.Get("COLA_COKE_0322Thu_newyork_s_tree_cut_COLA_COKE_0322Thu_newyork_s_f_POSP").Clone(); hist_thu22_P.SetLineColor(4); scale = hist_thu22_P.GetEntries(); scale = 1/scale; hist_thu22_P.Scale(scale); hist_thu22_P.SetBins(10,0.0,0.5)



'''
file_fri23 = TFile("","READ")
hist_fri23_N = file_fri23.Get("").Clone(); hist_fri23_N.SetLineColor(5); scale = hist_fri23_N.GetEntries(); scale = 1/scale; hist_fri23_N.Scale(scale); hist_fri23_N.SetBins(10,0.0,0.5)
hist_fri23_P = file_fri23.Get("").Clone(); hist_fri23_P.SetLineColor(5); scale = hist_fri23_P.GetEntries(); scale = 1/scale; hist_fri23_P.Scale(scale); hist_fri23_P.SetBins(10,0.0,0.5)
'''
file_fri23 = TFile("coffee_0323Fri_newyork_s_tree_cut_hist.root","READ")
hist_fri23_N = file_fri23.Get("coffee_0323Fri_newyork_s_tree_cut_coffee_0323Fri_newyork_s_f_NEGP").Clone(); hist_fri23_N.SetLineColor(5); scale = hist_fri23_N.GetEntries(); scale = 1/scale; hist_fri23_N.Scale(scale); hist_fri23_N.SetBins(10,0.0,0.5)
hist_fri23_P = file_fri23.Get("coffee_0323Fri_newyork_s_tree_cut_coffee_0323Fri_newyork_s_f_POSP").Clone(); hist_fri23_P.SetLineColor(5); scale = hist_fri23_P.GetEntries(); scale = 1/scale; hist_fri23_P.Scale(scale); hist_fri23_P.SetBins(10,0.0,0.5)
#file_fri23 = TFile("beer_0323Fri_newyork_s_tree_cut_hist.root","READ")
#hist_fri23_N = file_fri23.Get("beer_0323Fri_newyork_s_tree_cut_beer_0323Fri_newyork_s_f_NEGP").Clone(); hist_fri23_N.SetLineColor(5); scale = hist_fri23_N.GetEntries(); scale = 1/scale; hist_fri23_N.Scale(scale); hist_fri23_N.SetBins(10,0.0,0.5)
#hist_fri23_P = file_fri23.Get("beer_0323Fri_newyork_s_tree_cut_beer_0323Fri_newyork_s_f_POSP").Clone(); hist_fri23_P.SetLineColor(5); scale = hist_fri23_P.GetEntries(); scale = 1/scale; hist_fri23_P.Scale(scale); hist_fri23_P.SetBins(10,0.0,0.5)
#file_fri23 = TFile("COLA_COKE_0323Fri_newyork_s_tree_cut_hist.root","READ")
#hist_fri23_N = file_fri23.Get("COLA_COKE_0323Fri_newyork_s_tree_cut_COLA_COKE_0323Fri_newyork_s_f_NEGP").Clone(); hist_fri23_N.SetLineColor(5); scale = hist_fri23_N.GetEntries(); scale = 1/scale; hist_fri23_N.Scale(scale); hist_fri23_N.SetBins(10,0.0,0.5)
#hist_fri23_P = file_fri23.Get("COLA_COKE_0323Fri_newyork_s_tree_cut_COLA_COKE_0323Fri_newyork_s_f_POSP").Clone(); hist_fri23_P.SetLineColor(5); scale = hist_fri23_P.GetEntries(); scale = 1/scale; hist_fri23_P.Scale(scale); hist_fri23_P.SetBins(10,0.0,0.5)



'''
file_sat24 = TFile("","READ")
hist_sat24_N = file_sat24.Get("").Clone(); hist_sat24_N.SetLineColor(6); scale = hist_sat24_N.GetEntries(); scale = 1/scale; hist_sat24_N.Scale(scale); hist_sat24_N.SetBins(10,0.0,0.5)
hist_sat24_P = file_sat24.Get("").Clone(); hist_sat24_P.SetLineColor(6); scale = hist_sat24_P.GetEntries(); scale = 1/scale; hist_sat24_P.Scale(scale); hist_sat24_P.SetBins(10,0.0,0.5)
'''
file_sat24 = TFile("coffee_0324Sat_newyork_s_tree_cut_hist.root","READ")
hist_sat24_N = file_sat24.Get("coffee_0324Sat_newyork_s_tree_cut_coffee_0324Sat_newyork_s_f_NEGP").Clone(); hist_sat24_N.SetLineColor(6); scale = hist_sat24_N.GetEntries(); scale = 1/scale; hist_sat24_N.Scale(scale); hist_sat24_N.SetBins(10,0.0,0.5)
hist_sat24_P = file_sat24.Get("coffee_0324Sat_newyork_s_tree_cut_coffee_0324Sat_newyork_s_f_POSP").Clone(); hist_sat24_P.SetLineColor(6); scale = hist_sat24_P.GetEntries(); scale = 1/scale; hist_sat24_P.Scale(scale); hist_sat24_P.SetBins(10,0.0,0.5)
#file_sat24 = TFile("beer_0324Sat_newyork_s_tree_cut_hist.root","READ")
#hist_sat24_N = file_sat24.Get("beer_0324Sat_newyork_s_tree_cut_beer_0324Sat_newyork_s_f_NEGP").Clone(); hist_sat24_N.SetLineColor(6); scale = hist_sat24_N.GetEntries(); scale = 1/scale; hist_sat24_N.Scale(scale); hist_sat24_N.SetBins(10,0.0,0.5)
#hist_sat24_P = file_sat24.Get("beer_0324Sat_newyork_s_tree_cut_beer_0324Sat_newyork_s_f_POSP").Clone(); hist_sat24_P.SetLineColor(6); scale = hist_sat24_P.GetEntries(); scale = 1/scale; hist_sat24_P.Scale(scale); hist_sat24_P.SetBins(10,0.0,0.5)
#file_sat24 = TFile("COLA_COKE_0324Sat_newyork_s_tree_cut_hist.root","READ")
#hist_sat24_N = file_sat24.Get("COLA_COKE_0324Sat_newyork_s_tree_cut_COLA_COKE_0324Sat_newyork_s_f_NEGP").Clone(); hist_sat24_N.SetLineColor(6); scale = hist_sat24_N.GetEntries(); scale = 1/scale; hist_sat24_N.Scale(scale); hist_sat24_N.SetBins(10,0.0,0.5)
#hist_sat24_P = file_sat24.Get("COLA_COKE_0324Sat_newyork_s_tree_cut_COLA_COKE_0324Sat_newyork_s_f_POSP").Clone(); hist_sat24_P.SetLineColor(6); scale = hist_sat24_P.GetEntries(); scale = 1/scale; hist_sat24_P.Scale(scale); hist_sat24_P.SetBins(10,0.0,0.5)



'''
file_sun25 = TFile("","READ")
hist_sun25_N = file_sun25.Get("").Clone(); hist_sun25_N.SetLineColor(7); scale = hist_sun25_N.GetEntries(); scale = 1/scale; hist_sun25_N.Scale(scale); hist_sun25_N.SetBins(10,0.0,0.5)
hist_sun25_P = file_sun25.Get("").Clone(); hist_sun25_P.SetLineColor(7); scale = hist_sun25_P.GetEntries(); scale = 1/scale; hist_sun25_P.Scale(scale); hist_sun25_P.SetBins(10,0.0,0.5)
'''
file_sun25 = TFile("coffee_0325Sun_newyork_s_tree_cut_hist.root","READ")
hist_sun25_N = file_sun25.Get("coffee_0325Sun_newyork_s_tree_cut_coffee_0325Sun_newyork_s_f_NEGP").Clone(); hist_sun25_N.SetLineColor(7); scale = hist_sun25_N.GetEntries(); scale = 1/scale; hist_sun25_N.Scale(scale); hist_sun25_N.SetBins(10,0.0,0.5)
hist_sun25_P = file_sun25.Get("coffee_0325Sun_newyork_s_tree_cut_coffee_0325Sun_newyork_s_f_POSP").Clone(); hist_sun25_P.SetLineColor(7); scale = hist_sun25_P.GetEntries(); scale = 1/scale; hist_sun25_P.Scale(scale); hist_sun25_P.SetBins(10,0.0,0.5)
#file_sun25 = TFile("beer_0325Sun_newyork_s_tree_cut_hist.root","READ")
#hist_sun25_N = file_sun25.Get("beer_0325Sun_newyork_s_tree_cut_beer_0325Sun_newyork_s_f_NEGP").Clone(); hist_sun25_N.SetLineColor(7); scale = hist_sun25_N.GetEntries(); scale = 1/scale; hist_sun25_N.Scale(scale); hist_sun25_N.SetBins(10,0.0,0.5)
#hist_sun25_P = file_sun25.Get("beer_0325Sun_newyork_s_tree_cut_beer_0325Sun_newyork_s_f_POSP").Clone(); hist_sun25_P.SetLineColor(7); scale = hist_sun25_P.GetEntries(); scale = 1/scale; hist_sun25_P.Scale(scale); hist_sun25_P.SetBins(10,0.0,0.5)
#file_sun25 = TFile("COLA_COKE_0325Sun_newyork_s_tree_cut_hist.root","READ")
#hist_sun25_N = file_sun25.Get("COLA_COKE_0325Sun_newyork_s_tree_cut_COLA_COKE_0325Sun_newyork_s_f_NEGP").Clone(); hist_sun25_N.SetLineColor(7); scale = hist_sun25_N.GetEntries(); scale = 1/scale; hist_sun25_N.Scale(scale); hist_sun25_N.SetBins(10,0.0,0.5)
#hist_sun25_P = file_sun25.Get("COLA_COKE_0325Sun_newyork_s_tree_cut_COLA_COKE_0325Sun_newyork_s_f_POSP").Clone(); hist_sun25_P.SetLineColor(7); scale = hist_sun25_P.GetEntries(); scale = 1/scale; hist_sun25_P.Scale(scale); hist_sun25_P.SetBins(10,0.0,0.5)



hist_mon19_N.SetTitle(CanvasTitle+" with NEGATIVE from Monday to Sunday at Newyork (Normalized)")
hist_mon19_N.SetXTitle("Negative words propotion of Total words on a Tweet")
hist_mon19_N.SetYTitle("Emotion propotion (Log scale)")
hist_mon19_N.Draw("hist")
hist_tue20_N.Draw("hist same")
hist_wed21_N.Draw("hist same")
hist_thu22_N.Draw("hist same")
hist_fri23_N.Draw("hist same")
hist_sat24_N.Draw("hist same")
hist_sun25_N.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_mon19_N,"Mon","f")
leg_entry = leg.AddEntry(hist_tue20_N,"Tue","f")
leg_entry = leg.AddEntry(hist_wed21_N,"Wed","f")
leg_entry = leg.AddEntry(hist_thu22_N,"Thu","f")
leg_entry = leg.AddEntry(hist_fri23_N,"Fri","f")
leg_entry = leg.AddEntry(hist_sat24_N,"Sat","f")
leg_entry = leg.AddEntry(hist_sun25_N,"Sun","f")
leg.Draw()
cann.Modified()
cann.Update()
cann.Print(FilenameTitle+"_DAYS_Negative_log.pdf")


cann1.cd()
gPad.SetLogy(0)
hist_mon19_N.SetYTitle("Emotion propotion (Natural scale)")
hist_mon19_N.Draw("hist")
hist_tue20_N.Draw("hist same")
hist_wed21_N.Draw("hist same")
hist_thu22_N.Draw("hist same")
hist_fri23_N.Draw("hist same")
hist_sat24_N.Draw("hist same")
hist_sun25_N.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_mon19_N,"Mon","f")
leg_entry = leg.AddEntry(hist_tue20_N,"Tue","f")
leg_entry = leg.AddEntry(hist_wed21_N,"Wed","f")
leg_entry = leg.AddEntry(hist_thu22_N,"Thu","f")
leg_entry = leg.AddEntry(hist_fri23_N,"Fri","f")
leg_entry = leg.AddEntry(hist_sat24_N,"Sat","f")
leg_entry = leg.AddEntry(hist_sun25_N,"Sun","f")
leg.Draw()
cann1.Modified()
cann1.Update()
cann1.Print(FilenameTitle+"_DAYS_Negative.pdf")


canp.cd()
gPad.SetLogy(1)
hist_mon19_P.SetTitle(CanvasTitle+" with POSITIVE from Monday to Sunday at Newyork (Normalized)")
hist_mon19_P.SetXTitle("Positive words propotion of Total words on a Tweet")
hist_mon19_P.SetYTitle("Emotion propotion (Log scale)")
hist_mon19_P.Draw("hist")
hist_tue20_P.Draw("hist same")
hist_wed21_P.Draw("hist same")
hist_thu22_P.Draw("hist same")
hist_fri23_P.Draw("hist same")
hist_sat24_P.Draw("hist same")
hist_sun25_P.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_mon19_P,"Mon","f")
leg_entry = leg.AddEntry(hist_tue20_P,"Tue","f")
leg_entry = leg.AddEntry(hist_wed21_P,"Wed","f")
leg_entry = leg.AddEntry(hist_thu22_P,"Thu","f")
leg_entry = leg.AddEntry(hist_fri23_P,"Fri","f")
leg_entry = leg.AddEntry(hist_sat24_P,"Sat","f")
leg_entry = leg.AddEntry(hist_sun25_P,"Sun","f")
leg.Draw()
canp.Modified()
canp.Update()
canp.Print(FilenameTitle+"_DAYS_Positive_log.pdf")

canp1.cd()
gPad.SetLogy(0)
hist_mon19_P.SetTitle(CanvasTitle+" with POSITIVE from Monday to Sunday at Newyork (Normalized)")
hist_mon19_P.SetXTitle("Positive words propotion of Total words on a Tweet")
hist_mon19_P.SetYTitle("Emotion propotion (Natural scale)")
hist_mon19_P.Draw("hist")
hist_tue20_P.Draw("hist same")
hist_wed21_P.Draw("hist same")
hist_thu22_P.Draw("hist same")
hist_fri23_P.Draw("hist same")
hist_sat24_P.Draw("hist same")
hist_sun25_P.Draw("hist same")
leg = TLegend(0.65, 0.65, 0.85, 0.85)
leg.SetBorderSize(0)
leg.SetFillColor(10)
leg_entry = leg.AddEntry(hist_mon19_P,"Mon","f")
leg_entry = leg.AddEntry(hist_tue20_P,"Tue","f")
leg_entry = leg.AddEntry(hist_wed21_P,"Wed","f")
leg_entry = leg.AddEntry(hist_thu22_P,"Thu","f")
leg_entry = leg.AddEntry(hist_fri23_P,"Fri","f")
leg_entry = leg.AddEntry(hist_sat24_P,"Sat","f")
leg_entry = leg.AddEntry(hist_sun25_P,"Sun","f")
leg.Draw()
canp1.Modified()
canp1.Update()
canp1.Print(FilenameTitle+"_DAYS_Positive.pdf")






