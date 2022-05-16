//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include<iostream>
using namespace std;

int main()
{
    int value;
    int sum=0;
    while(cin >> value)
    {
        sum+=value;
        if(cin.get()=='\n')
        {
            cout << sum << endl;
            sum = 0;
        }
    }
}