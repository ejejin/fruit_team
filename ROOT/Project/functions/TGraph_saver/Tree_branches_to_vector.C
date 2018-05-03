// root -l -q Tree_branches_to_vector.C\('"Aqi.root"'\)

#include "n1_tree_to_vector.h"
#include "n2_COL_VECTOR.h"
#include "n3_TGraphs.h"
void Tree_branches_to_vector(string File)
{
    gROOT->ProcessLine("#include <vector>");
//    cout<<"test"<<endl;
    TFile *file = new TFile(File.data(),"READ");
    TIter nextkey(file->GetListOfKeys());
    TKey *key = 0;
    while((key = (TKey*)nextkey()))
    {
        TObject *obj = key->ReadObj();
        if ( obj->IsA()->InheritsFrom( TTree::Class() ) ) 
        {
            vector<vector<string>> Tree_vector;
            vector<vector<string>> colum_tree_vector;
            TTree *tree = (TTree*)obj;
            string Tree_name = tree->GetName();
            n1_tree_to_vector *TV = new n1_tree_to_vector();
            n2_COL_VECTOR *col_TV = new n2_COL_VECTOR();
            Tree_vector = TV->Tree_to_vector(tree);
            colum_tree_vector = col_TV->MAKE_COL_VECTOR_split(Tree_vector);
             

            n3_TGraphs *tgraph_plotter = new n3_TGraphs();
//            tgraph_plotter->Draw_TGraphs(colum_tree_vector, 33);
            tgraph_plotter->Draw_TGraphs_small(colum_tree_vector, 7);
        }
        else continue;
    }

    file->Close();
}
