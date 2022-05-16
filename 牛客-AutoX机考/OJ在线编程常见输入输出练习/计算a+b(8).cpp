//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<string> str;
    while(n--){
        string s;
        cin>>s;
        str.push_back(s);
    }
    sort(str.begin(),str.end());
    for(auto s1:str){
        cout<<s1<<" ";
    }
    return 0;
}