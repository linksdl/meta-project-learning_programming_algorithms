//
// Created by DAOLIN SHENG on 2022/5/15.
//


#include <iostream>

using namespace std;

int main(){
    int t,a,b,sum=0;
    cin>>t;
    while(t--){
        cin>>a;
        while(a--){
            cin>>b;
            sum+=b;
        }
        cout<<sum<<endl;
        sum=0;
    }

    return 0;
}