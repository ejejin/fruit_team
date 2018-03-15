#include <iostream>
#include <sstream>

struct Person
{
    Person(std::string name);
    std::string greet(std::string other_name);
    std::string m_name;
};

Person::Person(std::string name)
{
    m_name=name;
}

std::string Person::greet(std::string other_name)
{
    return "Hi "+other_name + ", my name is " + m_name;
}


void c2_struct_function()
{
    Person m_person("JUNHO");
    std::string str = m_person.greet("Friend");
    std::cout<<str<<std::endl;
}
