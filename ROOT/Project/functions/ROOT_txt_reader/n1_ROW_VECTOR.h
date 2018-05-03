#ifndef _N3_ROW_VECTOR_H_ 
#define _N3_ROW_VECTOR_H_

#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <vector>

class n1_ROW_VECTOR
{
    public:
        n1_ROW_VECTOR();
        vector<string> MAKE_ROW_VECTOR(string *file);
//        vector<string> v_str;
        vector<vector<string>> MAKE_ROW_VECTOR_split(vector<string> v_str);
//        vector<string> v_str_split;
};


n1_ROW_VECTOR::n1_ROW_VECTOR()
{
//    cout<<file->data()<<endl;
}

vector<string> n1_ROW_VECTOR::MAKE_ROW_VECTOR(string *file)
{
    ifstream infile;
//    cout<<file<<endl; 
    infile.open(file->data());   
    assert(infile.is_open());   
    vector<string> v_str; 
    string ss;
    while(getline(infile,ss))
    {
        v_str.push_back(ss);
    }
    infile.close();              
    return v_str;
}

vector<vector<string>> n1_ROW_VECTOR::MAKE_ROW_VECTOR_split(vector<string> v_str)
{
    vector<vector<string>> v_str_split;
    Int_t space_num=0;
    string space_string= " ";
    for(int i=0; i<v_str.at(0).size(); i++)
    {
        if(v_str.at(0).at(i)== space_string) space_num++;
    }
//    cout<<"test "<<space_num<<endl;

    for(int j=0; j<v_str.size(); j++)
    {
        vector<string> vtemp_str;
        istringstream is(v_str.at(j));
        for(int k=0; k<space_num+1; k++)
        {
            string temp_string;
            is>>temp_string;
//            cout<<temp_string<<endl;
            vtemp_str.push_back(temp_string);
        }
        v_str_split.push_back(vtemp_str);
        vtemp_str.clear();
    }

    return v_str_split;
}

#endif

