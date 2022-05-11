//
// Created by DAOLIN SHENG on 2022/5/10.
//



#include <iostream>
using namespace std;


long long a[101010], dp[101010];

int main()
{
    int n, i;
    cin >> n;
    for(int i=1; i<= n; i++) cin >> a[i];
    dp[0] = -1e9;
    long long res = -1e9;
    long long b = 0, c = 0;
    for(i=1; i<= n; i++)
    {
//         dp[i] = max(dp[i-1]+a[i], a[i]);
//         res = max(res, dp[i]);
        c = max(b + a[i], a[i]);
        res = max(res, c);
        b = c;
    }

    cout << res;

    return 0;
}