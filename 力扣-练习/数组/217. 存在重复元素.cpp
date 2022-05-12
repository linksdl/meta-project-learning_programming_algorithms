class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int size = nums.size();
        // 方法1: 暴力解决 两层循环 O(n^2) O(1) 超出时间限制
        // for(int i=0; i<size; i++)
        // {
        //     for(int j=i+1; j<size; j++)
        //     {
        //         if(nums[i] == nums[j]) return true;
        //     }
        // }
        // return false;

        // 方法2: 先排序，然后判断相邻元素是否相等 O(nlogn), O(logn)
        // sort(nums.begin(), nums.end());
        // for(int i=0; i < size-1; i++)
        // {
        //     if(nums[i] == nums[i+1]) return true;
        // }
        // return false;

        // 方法3: 根据hashset 判断
//        set<int> s;
        unordered_set<int> s;
        for(int i: nums)
        {
            // set 查找一个元素方法
            if(s.find(i) != s.end()) return true;
            s.insert(i);
        }
        return false;


    }
};
