//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;
int main() {
    string s;
    vector<string> str;
    while (cin >> s) {
        string temp;
        istringstream sst(s);
        while (getline(sst, temp, ',')){
            str.push_back(temp);
        }
        sort(str.begin(), str.end());
        for (int i =0;i<str.size()-1;i++) {
            cout << str[i] << ',';
        }
        cout <<str[str.size()-1]<< endl;
        str.clear();
    }
    return 0;
}
