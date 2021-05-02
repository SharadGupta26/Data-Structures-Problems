"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

https://leetcode.com/problems/longest-common-prefix/solution/
"""

from typing import List
class TrieNode :
    def __init__(self) :
        self.child = {}
        self.freq = 0
    def __str__(self) :
        return "freq {0} data {1}".format(self.freq, {key : str(self.child[key]) for key in self.child})
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        data = TrieNode()
        temp = data
       
        for s in strs :
            if s == "" :
                return ""
            for c in s :
                if c in temp.child :
                    temp = temp.child[c]
                    temp.freq += 1
                else :
                    node = TrieNode()
                    node.freq += 1
                    temp.child[c] = node
                    temp = node
            temp = data
        res = ""
        temp = data
        while temp.child.keys() :
            key = list(temp.child.keys())[0]
            
            if temp.child[key].freq == len(strs) :
                res += key
                temp = temp.child[key]
            else :
                break

        return res

            
"""
//devide and conquer

public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";    
        return longestCommonPrefix(strs, 0 , strs.length - 1);
}

private String longestCommonPrefix(String[] strs, int l, int r) {
    if (l == r) {
        return strs[l];
    }
    else {
        int mid = (l + r)/2;
        String lcpLeft =   longestCommonPrefix(strs, l , mid);
        String lcpRight =  longestCommonPrefix(strs, mid + 1,r);
        return commonPrefix(lcpLeft, lcpRight);
   }
}

String commonPrefix(String left,String right) {
    int min = Math.min(left.length(), right.length());       
    for (int i = 0; i < min; i++) {
        if ( left.charAt(i) != right.charAt(i) )
            return left.substring(0, i);
    }
    return left.substring(0, min);
}

"""

"""
//horzontal comparasion
//LCP(S1…Sn)=LCP(LCP(LCP(S1,S2),S3),…Sn)
 public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0) return "";
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++)
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }        
    return prefix;
}
"""