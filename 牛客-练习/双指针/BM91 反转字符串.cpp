//
// Created by DAOLIN SHENG on 2022/5/11.
//

class Solution {
public:
    /**
     * 反转字符串
     * @param str string字符串
     * @return string字符串
     */
    string solve(string str) {
        // write code here
        int size  = str.size();
        int i = 0, j = size-1;

//         const char* ch = str.c_str();

        while(i < j)
        {
            char t = str[j];
            str[j] = str[i];
            str[i] = t;
            i ++;
            j --;
        }

        return str;
    }
};