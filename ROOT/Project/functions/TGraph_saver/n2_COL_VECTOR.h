#ifndef _N4_COL_VECTOR_H_
#define _N4_COL_VECTOR_H_

#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <vector>

class n2_COL_VECTOR
{
    public:
        n2_COL_VECTOR();
        vector<vector<string>> MAKE_COL_VECTOR_split(vector<vector<string>> v_str);

};

n2_COL_VECTOR::n2_COL_VECTOR()
{
}

vector<vector<string>> n2_COL_VECTOR::MAKE_COL_VECTOR_split(vector<vector<string>> v_str)
{
    vector<vector<string>> v_str_spilt;
    for(int i=0; i<v_str.at(0).size(); i++)
    {
        vector<string> vtemp_col;
        for(int j=0; j<v_str.size(); j++)
        {
            vtemp_col.push_back(v_str.at(j).at(i));
//            cout<<v_str.at(j).at(i)<<" ";
        }
//        cout<<endl;
        v_str_spilt.push_back(vtemp_col);
        vtemp_col.clear();
    }
 
    return v_str_spilt;
}

#endif
