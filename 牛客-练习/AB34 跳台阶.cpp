//
// Created by DAOLIN SHENG on 2022/5/10.
//

#include <iostream>
using namespace  std;

int jumpFloor(int number)
{
//  1，递归 O（2^n）
     if(number==1) return 1;
     if(number==2) return 2;
     return jumpFloor(number-1) + jumpFloor(number-2);
}

int dp[50] = {0};
int jumpFloor1(int number)
{
    // 2, 递归优化（记忆搜索)
    if(number <=1) return 1;
    if(dp[number] > 0) return dp[number];
    return dp[number] = (jumpFloor1(number-1) + jumpFloor1(number-2));
}

int jumpFloor2(int number)
{
     // 3，动态规划
     dp[0] = 1; dp[1] = 1;
     for(int i =2; i <= number; i++)
     {
         dp[i] = dp[i-1] + dp[i-2];
     }
     return dp[number];
}

int jumpFloor3(int number)
{
    // 4，动态规划优化
    int a=1, b=1, c=1;
    for(int i =2; i <= number; i++)
    {
        c = a + b, a = b, b = c;
    }
    return c;
}

int main()
{
    int n;
    cin >> n;
    cout << jumpFloor3(n);
    return 0;
}