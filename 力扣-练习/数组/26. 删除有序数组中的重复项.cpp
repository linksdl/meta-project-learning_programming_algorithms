class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        if(size < 2) return size;
        int left=0, right=1;
        while(right < size)
        {
            if(nums[left] == nums[right])
            {
                right++;
            }
            else
            {
                // left ++;
                nums[++left] = nums[right++];
                // right ++;
            }
        }
        return (left+1);
    }
};
