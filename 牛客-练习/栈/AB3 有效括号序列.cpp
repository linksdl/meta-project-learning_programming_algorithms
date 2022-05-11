//
// Created by DAOLIN SHENG on 2022/5/10.
//


class Solution {
public:
    /**
     *
     * @param s string字符串
     * @return bool布尔型
     */
    bool isValid(string s) {
        // write code here
        stack<char>  stk;
        for(int i=0; i< s.size(); i++)
        {
            if(s[i] == '(')
                stk.push(')');
            else if(s[i] == '{')
                stk.push('}');
            else if(s[i] == '[')
                stk.push(']');
            else
            {
                if(stk.empty() || s[i] != stk.top())
                    return false;
                stk.pop();
            }
        }

        return stk.empty();

    }
};
