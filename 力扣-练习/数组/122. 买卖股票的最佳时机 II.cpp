//class Solution {
//public:
//    int maxProfit(vector<int>& prices) {
//        int left =0, right = 1, size = prices.size();
//        // earn
//        int total = 0;
//        while(right < size)
//        {
//            if(prices[right] <= prices[left])
//            {
//                left = right;
//                right++;
//            }else
//            {
//                if(prices[++right] < prices[right])
//                {
//                    total  = total + prices[right]-prices[left];
//                    left = right;
//                }else
//                {
//                    right ++;
//                }
//
//            }
//        }
//        return total;
//    }
//};


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};
