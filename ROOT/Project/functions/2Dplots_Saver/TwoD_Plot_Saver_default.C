//root -l -q TwoD_Plot_Saver_default.C\('"/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_re_tree_cut_hist2D.root"'\)
#include "TROOT.h"
#include "TKey.h"
#include "TFile.h"
#include "TSystem.h"
#include "TTree.h"
#include "TH2D.h"
#include <vector>
#include "n1_read_2d_histos.h"
using namespace std;

void TwoD_Plot_Saver_default(string File)
{
//    string infile = "/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_day_re_tree_cut_hist2D.root";
    string infile= File;
    vector<TH2D*> TwoD_histos;
    vector<string> TwoD_histos_Name;
    n1_read_2d_histos* READ_2d = new n1_read_2d_histos();
    TwoD_histos = READ_2d->TwoD_HISTs(&infile);
    TwoD_histos_Name = READ_2d->TwoD_HISTs_Name(&infile);
    READ_2d->Draw_n_Save_Histos();
    READ_2d->Draw_n_Save_Histos_colz(70,70);
}

