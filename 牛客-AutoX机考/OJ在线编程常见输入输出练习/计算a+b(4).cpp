//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include <iostream>

using namespace std;

int main()
{
    int n, input, sum;
    while(cin >> n && n != 0)
    {
        while(n--)
        {
            cin>>input;
            sum += input;
        }
        cout << sum << endl;
        sum = 0;
    }

    return 0;
}