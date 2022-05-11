//
// Created by DAOLIN SHENG on 2022/5/10.
//

#include <iostream>
#include <string>
#include <bits/stdc++.h>

using namespace std;


int main()
{
    string s;
    cin >> s;
    stack<char> stk;

    for(int i=0; i<s.size(); i++)
    {
        if(stk.empty())
        {
            stk.push(s[i]);
        }
        else
        {
            if(stk.top() == s[i])
            {
                stk.pop();
            }
            else
            {
                stk.push(s[i]);
            }
        }
    }

    if(stk.empty()) cout << 0 << endl;
    else
    {
        int n = stk.size();
        char a[n];
        for(int i=n-1; i>=0; i--)
        {
            a[i] = stk.top();
            stk.pop();
        }

        for(int i=0;i<n;i++) cout<< a[i];
    }

    return 0;
}