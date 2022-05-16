//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string s;

    vector<string> str;
    while (cin >> s) {
        str.push_back(s);
        if(cin.get() == '\n'){
            sort(str.begin(), str.end());
            for (auto &s1 : str) {
                cout << s1 << " ";
            }
            cout<<endl;
            str.clear();
        }
    }
    return 0;
}