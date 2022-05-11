//
// Created by DAOLIN SHENG on 2022/5/11.
//

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        // A 尾部指针
        int i = m-1;
        // B 尾部指针
        int j = n-1;
        // A 最后的位置
        int k = m + n - 1;

        while(i >= 0 && j >= 0)
        {
            if(A[i] > B[j])
                A[k--] = A[i--];
            else
                A[k--] = B[j--];
        }
        if(i < 0)
        {
            while(j>=0)
            {
                A[k--] = B[j--];
            }
        }

    }
};