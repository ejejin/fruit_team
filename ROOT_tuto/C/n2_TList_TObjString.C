//STD
#include <algorithm>
#include <iostream>
#include <sstream>

//ROOT
#include "TList.h"
#include "TCollection.h"
#include "TObjString.h"
#include "TObject.h"

struct function1
{
    bool operator()(TObject *aObj)
    {
        if(!aObj) return false;
        
        TObjString *str(dynamic_cast<TObjString*>(aObj));   // tranform within class : dynamic_cast
        if(!str) return false;

        cout<<"Value : "<<str->String().Data()<<endl;
        return true;
    }
};





void n2_TList_TObjString()
{
    const Int_t size(10);    //definition 
//    cout<<size<<endl;
//    cout<<typeid(size).name()<<endl;
    TList stringList;
    ostringstream ss;
    for(int i =0; i < size; i++)    // define a TObjString and Add them into TList
    {
        ss<<" test string # " <<i;
//        TObjString *s(new TObjString(ss.str().c_str()));
        TObjString *s = new TObjString(ss.str().c_str());
//        TObjString *s(new TObjString(ss.str()));  // this causes error since it is not const char
        stringList.Add(s);        
//        cout<<ss.str()<<endl;
        ss.str("");    // empty the ostringstream ss 
    }
//    cout<<"type name of ss is "<<typeid(ss).name()<<endl;
//    cout<<"type name of stringList is : "<<typeid(stringList).name()<<endl;
//    cout<<"type name of stringList.begin() is "<<typeid(stringList.begin()).name()<<endl;

//    ss<<"test!!";
//    TObjString *stest = new TObjString(ss.str().c_str());
//    TObject *Stest = (TObject*)stest;
//    cout<<"type name of Stest is : "<<typeid(Stest).name()<<endl;
//    function1(Stest);   // I don't know why error...

    for_each(stringList.begin(),stringList.end(), function1());

//******************************** end of function1 ******************************



}





