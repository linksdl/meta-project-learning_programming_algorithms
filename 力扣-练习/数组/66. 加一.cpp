
//https://leetcode.cn/problems/plus-one/


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();

        // 判断
        for(int i=n-1; i>=0; i--)
        {
            if(digits[i] != 9)
            {
               ++digits[i];
               for(int j=i+1; j<n; j++)
               {
                   digits[j] = 0;
               }
               return digits;
            }
        }

        // 所有都是9
        vector<int> ans(n + 1);
        ans[0] = 1;
        return ans;

    }
};
