#ifndef _N3_TGRAPHS_H_
#define _N3_TGRAPHS_H_

#include <string>
#include <vector>
#include "TCanvas.h"
#include "TGraph.h"

class n3_TGraphs
{
    public:
        n3_TGraphs();
        void Draw_TGraphs(vector<vector<string>> colum_tree_vector, int marker_style=33);
        void Draw_TGraphs_small(vector<vector<string>> colum_tree_vector, int marker_style=33);
};

n3_TGraphs::n3_TGraphs()
{
}

void n3_TGraphs::Draw_TGraphs(vector<vector<string>> colum_tree_vector, int marker_style=33)
{
    const Int_t NUM = colum_tree_vector.at(0).size();
    cout<<"Total Entry after Cut : "<<NUM-1<<endl;
    
    for(int j=0; j<colum_tree_vector.size(); j++)
    {
        for(int k=0; k<colum_tree_vector.size(); k++)
        {
            TCanvas *c1 = new TCanvas();
            c1->SetGrid();
            Double_t x[NUM], y[NUM];
            for(Int_t i=0; i<NUM; i++)
            {
                if(i==0) continue;
                x[i] = atof((colum_tree_vector.at(j).at(i)).data());
                y[i] = atof((colum_tree_vector.at(k).at(i)).data());
//                cout<<x[i]<<endl;
            }
  
            TGraph *gr = new TGraph(NUM,x,y);
            Double_t correlation_factor = gr->GetCorrelationFactor();
            Double_t covarianve = gr->GetCovariance();
//            cout<<correlation_factor<<","<<covarianve<<endl;
            string TitleName = "X_"+colum_tree_vector.at(j).at(0)+"_Y_"+colum_tree_vector.at(k).at(0);
            gr->SetTitle(TitleName.data());
            gr->SetMarkerStyle(marker_style);
            gr->Draw("AP");
            c1->Update();
            c1->GetFrame()->SetBorderSize(12);
            c1->Modified();
            string SAVENAME = "X_"+colum_tree_vector.at(j).at(0)+"_Y_"+colum_tree_vector.at(k).at(0)+"_Tgraph_basic.pdf";
            c1->SaveAs(SAVENAME.data());
            c1->Clear();
        }
    }
}

void n3_TGraphs::Draw_TGraphs_small(vector<vector<string>> colum_tree_vector, int marker_style=7)
{
    const Int_t NUM = colum_tree_vector.at(0).size();
    cout<<"Total Entry after Cut : "<<NUM-1<<endl;

    for(int j=0; j<colum_tree_vector.size(); j++)
    {
        TCanvas *c1 = new TCanvas(); 
        TCanvas *c2 = new TCanvas();
        TCanvas *c3 = new TCanvas();
        c1->SetGrid(); 
        c2->SetGrid();
        c3->SetGrid();
        c1->Divide(2,2);
        c2->Divide(2,2);
        c3->Divide(2,2); 

        for(int k=0; k<colum_tree_vector.size(); k++)
        {
            Double_t x[NUM], y[NUM];
            for(Int_t i=0; i<NUM; i++)
            {
                if(i==0) continue;
                y[i] = atof((colum_tree_vector.at(j).at(i)).data());
                x[i] = atof((colum_tree_vector.at(k).at(i)).data());
//                cout<<x[i]<<endl;
            }
            if(k<4) {c1->cd(k+1);}
            if (k>=4) 
            {
                if(k==4) {/*TCanvas *c2 = new TCanvas(); c2->Divide(2,3);*/ c2->cd(1);}
                else c2->cd(k-3); 
            }
            if (k>=8) 
            {
                if(k==8) {/*TCanvas *c3 = new TCanvas(); c3->Divide(2,3);*/ c3->cd(1);}
                else c3->cd(k-7);
            }

            TGraph *gr = new TGraph(NUM,x,y);
            Double_t correlation_factor = gr->GetCorrelationFactor();
            double corr3 = floor(correlation_factor*10000.00f + 0.5) / 10000.00f;
//            cout<<corr3<<endl;
            Double_t covarianve = gr->GetCovariance();
//            cout<<correlation_factor<<","<<covarianve<<endl;
            string TitleName = "X_"+colum_tree_vector.at(k).at(0)+"_Y_"+colum_tree_vector.at(j).at(0);
            gr->SetTitle(TitleName.data());
            gr->SetMarkerStyle(marker_style);
            gr->Draw("AP");
            if(k<4)
            {
                auto legend = new TLegend(0.5,0.8,0.88,0.88);
                legend->SetTextColor(kRed);
                legend->SetBorderSize(0);
//                legend->SetHeader("The Legend Title","C");
                string str_corr_fac = to_string(corr3);
                string corr_fac = "co-factor : "+ str_corr_fac;
                legend->AddEntry((TObject*)0,corr_fac.c_str(),"");
                legend->SetTextSize(0.05);
                legend->Draw();
                c1->Update();
                c1->GetFrame()->SetBorderSize(12);
                c1->Modified();
            }
            else if(k>=4)
            {
                auto legend = new TLegend(0.5,0.8,0.88,0.88);
                legend->SetTextColor(kRed);
                legend->SetBorderSize(0);
//                legend->SetHeader("The Legend Title","C");
                string str_corr_fac = to_string(corr3);
                string corr_fac = "co-factor : "+ str_corr_fac;
                legend->AddEntry((TObject*)0,corr_fac.c_str(),"");
                legend->SetTextSize(0.05);
                legend->Draw();
                c2->Update();
                c2->GetFrame()->SetBorderSize(12);
                c2->Modified();
            }
            else if (k>=8)
            {
                auto legend = new TLegend(0.5,0.8,0.88,0.88);
                legend->SetTextColor(kRed);
                legend->SetBorderSize(0);
//                legend->SetHeader("The Legend Title","C");
                string str_corr_fac = to_string(corr3);
                string corr_fac = "co-factor : "+ str_corr_fac;
                legend->AddEntry((TObject*)0,corr_fac.c_str(),"");
                legend->SetTextSize(0.05);
                legend->Draw();
                c3->Update();
                c3->GetFrame()->SetBorderSize(12);
                c3->Modified();
            }
//            string SAVENAME = "X_"+colum_tree_vector.at(j).at(0)+"_Y_"+colum_tree_vector.at(k).at(0)+"_Tgraph_basic.pdf";
//            c1->SaveAs(SAVENAME.data());
//            c1->Clear();
        }
        string c1_SAVENAME = "Y_"+colum_tree_vector.at(j).at(0)+"_Tgraph_basic_1.pdf";
        c1->SaveAs(c1_SAVENAME.data());
        c1->Clear();
        if(colum_tree_vector.size() >=4)
        {
            string c2_SAVENAME = "Y_"+colum_tree_vector.at(j).at(0)+"_Tgraph_basic_2.pdf";
            c2->SaveAs(c2_SAVENAME.data());
            c2->Clear();        
        }
        if(colum_tree_vector.size() >=8)
        {
            string c3_SAVENAME = "Y_"+colum_tree_vector.at(j).at(0)+"_Tgraph_basic_3.pdf";
            c3->SaveAs(c3_SAVENAME.data());
            c3->Clear();  
        }
    }
}

#endif
