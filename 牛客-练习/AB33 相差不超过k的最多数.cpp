//
// Created by DAOLIN SHENG on 2022/5/10.
//


#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    long long k, sub;
    cin >> n >> k;

    long long arr[200000]{0};
    for(int i=0; i < n; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr+n);
    int max = 0;
    int left=0, right=0;
    while(right < n)
    {
        sub = arr[right] - arr[left];
        while(sub>k)
        {
            left ++;
            break;
        }
        if(max < right - left + 1 || max==0)
        {
            max = right - left + 1;
        }
        right ++;
    }

    cout << max << endl;

    return 0;
}