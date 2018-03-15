#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
void hello(int a)
{
    std::cout<<a<<std::endl;
}

void c1_for_each()
{
    hello(10);
    std::vector<int> vv;
    vv.push_back(1);
    vv.push_back(3);
    vv.push_back(3);
    vv.push_back(2);
/*
    for(auto a: vv)
    {
        hello(a);

    }
    int a[] = {3,3,3};
*/


    std::cout<<"size of vector : "<<vv.size()<<endl;
    std::cout<<typeid(vv.begin()).name()<<"!!!!"<<endl;
    std::for_each(vv.begin(),vv.end(),hello);
}
