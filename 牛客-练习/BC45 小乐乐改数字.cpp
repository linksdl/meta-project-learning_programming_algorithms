//
// Created by DAOLIN SHENG on 2022/5/17.
//

//#include <iostream>
//
//using namespace std;
//
//
//int main()
//{
//    long long num;
//    cin >> num;
//
//    long long ans;
//    while(num%10 != 0)
//    {
//        int temp = num%10;
//        if(temp %2 == 1)
//        {
//            ans = ans + temp*10;
//        } else
//        {
//            ans = ans;
//        }
//        num = num/10;
//    }
//    cout << ans << endl;
//
//    return 0;
//}



#include<iostream>
#include<string>

using namespace std;

int main()
{
    char c[10] = {};
    cin >> c;
    int n = strlen(c);
    for (int i = 0; i < n; i++)
    {
        if (c[i] % 2 == 0)
            c[i] = '0';
        else
            c[i] = '1';
    }
    int f = 0;
    for (int i = 0; i < n; i++)
    {
        if (c[i] != '0')
            ++f;
        if (f == 0)
            continue ;
        cout << c[i];
    }

    if (f == 0)
        cout << '0' << endl;

    cout << endl;
    return 0;
}