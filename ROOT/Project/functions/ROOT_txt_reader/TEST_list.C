//root -l -q TEST_list.C\('"/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/data_txt/BEIJING_Aqi/Aqi_Beijing_Holi.txt"'\)

#include <vector>
#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <cstring>
#include "n1_ROW_VECTOR.h"
#include "n2_COL_VECTOR.h"

using namespace std;

void TEST_list(string file)
{
    vector<string> R_STR;
    vector<vector<string>> R_STR_split;   // Row string splited
    n1_ROW_VECTOR* row_vector = new n1_ROW_VECTOR();
    R_STR = row_vector->MAKE_ROW_VECTOR(&file);
    R_STR_split = row_vector->MAKE_ROW_VECTOR_split(R_STR);

    vector<vector<string>> C_STR_split; 
    n2_COL_VECTOR* col_vector = new n2_COL_VECTOR();
    C_STR_split = col_vector->MAKE_COL_VECTOR_split(R_STR_split);

/*
    for(int i=0; i<R_STR_split.size(); i++)
    {
        for(int j=0; j<R_STR_split.at(i).size(); j++)
        {
            cout<<R_STR_split.at(i).at(j)<<" ";
        }
        cout<<endl;
    }


    for(int i=0; i<C_STR_split.size(); i++)
    {
        for(int j=0; j<C_STR_split.at(i).size();j++)
        {
            cout<<C_STR_split.at(i).at(j)<<" ";
        }
        cout<<endl;
    }
*/
}


