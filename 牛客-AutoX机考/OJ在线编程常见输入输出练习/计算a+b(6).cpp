//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include<iostream>
using namespace std;

int main()
{
    int num,value;
    int sum;
    while(cin >> num)
    {
        sum = 0;

        for(int i=0;i<num;i++)
        {
            cin >> value;
            sum+=value;
        }
        cout << sum << endl;
    }
}