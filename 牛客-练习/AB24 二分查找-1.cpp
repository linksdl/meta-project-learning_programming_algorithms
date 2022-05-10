//
// Created by DAOLIN SHENG on 2022/5/10.
//

#include <iostream>
using namespace std;

// 二分查找 O(log2n)
int binarySearch(vector<int>& nums, int target)
{
    int l = 0, r = nums.size() -1;
    while(l <= r)
    {
        int mid = (l + r) / 2;
        if(nums[mid] == target)
        {
            return mid;
        }
        else if(nums[mid] > target)
        {
            r = mid -1;
        }
        else
        {
            l = mid + 1;
        }
    }
    return -1;
}


int main()
{
    int arr[10] = {0};
    int target;
    cin >> target;
    binarySearch(arr, target);
    return 0;
}
